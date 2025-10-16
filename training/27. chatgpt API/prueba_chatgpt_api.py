from openai import OpenAI

client = OpenAI(
    api_key="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"
)

response = client.responses.create(
    model="gpt-oss-120b",
    input="write a haiku about ai",
    store=True,
)

print(response.output_text)
