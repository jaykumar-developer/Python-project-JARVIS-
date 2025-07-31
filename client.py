from openai import OpenAI


client = OpenAI(
        api_key="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"
)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
     messages=[
            {"role": "system", "content": "You are a virtual assistant name jarvis skilled in general tasks."},
            {"role": "user", "content": "what is AI"}
            ],
)
print( response.choices[0].message.content)

   
