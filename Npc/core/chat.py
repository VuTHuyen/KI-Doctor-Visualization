from openai import OpenAI

client = OpenAI()
chat_log = []

# This function takes a text-based question as input
# Interacts with a language AI API OpenAI to generate a response using the gpt-3.5-turbo model.
# Returns the AI's response to be used in further processing or displayed to the user.
def chat(question):
    query_dict = {"role": "user", "content": question}
    chat_log.append(query_dict)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=chat_log
    )

    assistant = completion.choices[0].message.content

    query_dict = {"role": "assistant", "content": assistant}
    chat_log.append(query_dict)

    print("answer from API: " + assistant)
    return assistant