from typing import Dict, Any
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, ToolMessage, SystemMessage
from tools_provider import get_available_tools
import importlib


class AIAgent:
    def __init__(self, model_name: str = "qwen2.5:7b"):
        self.model_name = model_name
        self.client = ChatOllama(model=model_name)
        self.tools = get_available_tools()
        self.client_with_tools = self.client.bind_tools(self.tools)

    async def llm_call(self, prompt: str) -> str:
        messages = [
            SystemMessage(content="""You are a helpful data assistant. When you receive data from tools:
            - If asked for details, summarize the relevant information
            - Respond in simple, natural language as if talking to a person
            """),
            HumanMessage(content=prompt),
        ]

        try:
            response = await self.client_with_tools.ainvoke(messages)

            """
            TOOL CALLS RESPONSE EXAMPLE:
            {
                "tool_calls": [
                    {
                        "id": "call_001",
                        "name": "get_weather",
                        "args": {"location": "Paris"}
                    }
                ]
            }
            """

            if response.tool_calls:
                messages.append(response)

                for tool_call in response.tool_calls:
                    function_name = tool_call["name"]
                    arguments = tool_call["args"]
                    print(f"🔍 Executing function: {function_name} with arguments: {arguments}")
                    tool_response = self.execute_function(function_name, arguments)
                    messages.append(ToolMessage(
                        content=tool_response,
                        tool_call_id=tool_call["id"]
                    ))
                try:
                    final_response = await self.client_with_tools.ainvoke(messages)
                    return final_response.content
                except Exception as e:
                    return f"Error in final LLM call: {str(e)}"

            return response.content

        except Exception as e:
            return f"Error in LLM call: {str(e)}"

    def execute_function(self, function_name: str, arguments: Dict[str, Any]) -> str:
        try:
            module = importlib.import_module(f"tools.{function_name}")
            func = getattr(module, function_name, None)
            if func is None:
                return f"Error: Function '{function_name}' not found in module"
            result = func(**arguments)
            return str(result)
        except ImportError as e:
            return f"Error: Could not import module 'tools.{function_name}': {str(e)}"
        except Exception as e:
            return f"Error: Function execution failed - {str(e)}"
