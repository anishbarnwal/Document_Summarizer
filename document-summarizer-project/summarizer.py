# OpenAI summarization logic placeholder
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_OPENAI_API_KEY"
)


def summarize_document(text):

    if len(text) > 15000:
        text = text[:15000]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content":
                "Summarize the document in 5-10 sentences."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content
