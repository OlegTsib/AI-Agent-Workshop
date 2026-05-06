# AI Agent Workshop \- Preparation

# Python

First, need to check if you have installed Python 3

In Terminal run 

```
python3 --version
```

You should see the response 3…

```
Python 3.13.7
```

If not, you need to install Python 3 using the CLI or from the [Download Python](https://www.python.org/downloads/) 

**CLI**  
If you haven’t installed Homebrew, [Install Homebrew](https://brew.sh/) 

```
brew install python
```

Relaunch Terminal and try again to check the Python 3 version 

# Code Editor

I will use [Cursor](https://cursor.com/)

# Ollama

Install [Ollama](https://ollama.com/)   
The full list of available LLM models can be found [here](https://ollama.com/library?sort=popular)  
For this workshop, we will use **qwen2.5:7b**  
After installing Ollama, we need to move to the Terminal and install 2 models, **LLM** and **Embedding** (don’t worry if you are not familiar with this, I will talk about this on the workshop)  
1\. 

```
ollama pull qwen2.5:7b
```

2\.

```
ollama pull mxbai-embed-large
```

After run

```
ollama list
```

You should see 

```
NAME                        ID              SIZE      MODIFIED
qwen2.5:7b                  845dbda0ea48    4.7 GB    7 hours ago
mxbai-embed-large:latest    468836162de7    669 MB    4 days ago

```

