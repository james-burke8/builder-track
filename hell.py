from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

msg = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=200,
    messages=[{"role": "user", "content": "In one sentence, what is prompt injection?"}],
)

print(msg.content[0].text)
print(f"tokens in: {msg.usage.input_tokens} | tokens out: {msg.usage.output_tokens}")
