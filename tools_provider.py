def get_available_tools(): 
        return [
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": """
                        Get current weather for a location. This tool returns natural, conversational 
                        weather information. The response includes temperature, conditions, and friendly advice.
                    """,
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "City name or location"
                            },
                            "unit": {
                                "type": "string", 
                                "enum": ["celsius", "fahrenheit"],
                                "description": "Temperature unit"
                            }
                        },
                        "required": ["location"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "annual_report",
                    "description": """
                        Use this tool to search the FastFeast Annual Report 2025 for business information.
                        IMPORTANT: After receiving results, analyze the content and respond in NATURAL LANGUAGE.
                        - Answer questions about revenue, growth, performance, strategy, etc.
                        - Summarize findings from the report sections
                        - Provide specific data points when asked
                    """,
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Natural language query about the annual report. Can include questions about revenue, profits, growth, strategy, performance, quarters, etc."
                            }
                        },
                        "required": ["query"]
                    }
                }
            }
        ]