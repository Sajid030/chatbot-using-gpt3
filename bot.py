import openai
import gradio

openai.api_key = "sk-"

message = [{"role":"system", "content":"You are a Data Scientist"}]

def mygpt(user_input):
    message.append({"role":"user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message
    )
    reply = response["choices"][0]["message"]["content"]
    message.append({"role": "assistant", "content": reply})
    return reply

demo = gradio. Interface(fn=mygpt, inputs = "text", outputs ="text", title= "Data Scientist")

demo.launch(share=True)
