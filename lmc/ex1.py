lmc_urls = ['lmc:openai://@gpt-4o', 
            'lmc:openai://api.deepseek.com@deepseek-chat',
            'lmc:openai://openrouter.ai/api/v1@google/gemini-2.0-flash-lite-001',
            'lmc:ollama://localhost:11434@llama3.2',
            'lmc:llamacpp://./models/7B/llama-model.gguf',
]

import enum
class APIType(enum.Enum):
    #case conventions?
    OpenAI = 'openai'
    ollama = 'ollama'
    llamaCPP = 'llamacpp'

class Connection:
    api_type: APIType
    url: str
    model: str

    def __init__(self, api_type: APIType, url: str, model: str):
        self.api_type = api_type
        self.url = url
        self.model = model

    def __str__(self):
        return f"api_type: {self.api_type.name}, url: {self.url}, model: {self.model}"
    
    def __iter__(self):
        yield self.api_type
        yield self.url
        yield self.model

def parser(url: str):
    if not url.startswith('lmc:'):
        raise ValueError('URL must start with lmc:')
    
    url = url[4:]
    
    a = url.replace('://', '@').split('@')
    if a[1] == '':
        a[1] = 'api.openai.com'
    if len(a) != 3:
        a.append("LLaMA_CPP")
    return Connection(api_type=APIType(a[0]), url=a[1], model=a[2])

def tests():
    print("tests:")
    for url in lmc_urls:
        print(parser(url))
    print("-----------------------------")


def generate(conn: Connection, api_key: str, messages: list):
    if conn.api_type == APIType.OpenAI:
        from openai import OpenAI

        client = OpenAI(api_key=api_key, base_url="https://" + conn.url)

        response = client.chat.completions.create(
            model=conn.model,
            messages=messages,
            stream=False,
        )

        return response.choices[0].message.content
    # etc etc etc


def parse_env_file() -> str:
    with open('.env', 'r') as f:
        return f.read().replace('\n', '').replace('API_KEY=', '')

def main():
    api_key = parse_env_file()
    messages = [
        {"role": "system", "content": "you're an language translator to French. respond in ONLY translated text, in the same formality and with the same punctuation."},
        {"role": "user", "content": "i ate my dad"},
    ]
    conn = parser("lmc:openai://openrouter.ai/api/v1@cognitivecomputations/dolphin3.0-r1-mistral-24b:free")
    resp = generate(conn, api_key, messages)

    print(resp)
 

if __name__ == "__main__":
    main()
    