# LMC (Language Model Connectivity)
idea: *it's like odbc but for llms*
```
lmc:[api]://[url]@[model]
```

## examples:
OpenAI API with OpenAI servers
```
lmc:openai://@gpt-4o
```
Deepseek
```
lmc:openai://api.deepseek.com@deepseek-chat
```
OpenRouter
```
lmc:openai://openrouter.ai/api/v1@google/gemini-2.0-flash-lite-001
```

ollama
```
lmc:ollama://localhost:11434@llama3.2
```
llama.cpp
```
lmc:llamacpp://./models/7B/llama-model.gguf
```
