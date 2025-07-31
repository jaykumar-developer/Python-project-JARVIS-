from openai import OpenAI


client = OpenAI(
        api_key="your api key"
)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
     messages=[
            {"role": "system", "content": "You are a virtual assistant name jarvis skilled in general tasks."},
            {"role": "user", "content": "what is AI"}
            ],
)
print( response.choices[0].message.content)

   
