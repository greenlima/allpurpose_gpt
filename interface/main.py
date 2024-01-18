import chainlit as cl
import openai
from chainlit import user_session
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []

# Continuously on a loop
@cl.on_message
async def main(message:str):

    # logic
    # Wellcome message
    if len(messages)==1:
        msg = f"I am your new assistant! How can I help?"
        await cl.Message(content = msg).send()
        messages.append({"role": "assistant", "content": msg})

    # LLM
    else:
        messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            #model="gpt-4-1106-preview",
            max_tokens=1500,
            messages=messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        # send a response back to the user
        await cl.Message(content = reply).send()


# At start
# Define system prompt
@cl.on_chat_start
async def start():
    system_msg = "What type of assistant would you like to create?"
    await cl.Message(content=system_msg).send()
    messages.append({"role": "system", "content": system_msg})
