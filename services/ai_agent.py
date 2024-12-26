from openai import OpenAI
client = OpenAI()

# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant and only reply in Korean."},
#         {
#             "role": "user",
#             "content": "프롬프트 엔지니어링에 대해 설명해줘."
#         }
#     ]
# )

# print(completion.choices[0].message)

# response = client.embeddings.create(
#     model="text-embedding-3-small",
#     input="The food was delicious and the waiter..."
# )

# print(response)

