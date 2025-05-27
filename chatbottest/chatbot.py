import tkinter as tk
from openai import OpenAI

#OpenAI API 키
client = OpenAI(api_key="YOUR_API_KEY")

def get_gpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1024,
    )
    return response.choices[0].message.content.strip()

def send_message():
    user_message = entry.get()
    if user_message.strip() == "":
        return
    chat_box.insert(tk.END, "User: " + user_message + "\n")
    entry.delete(0, tk.END)
    window.update()
    try:
        gpt_response = get_gpt_response(user_message)
    except Exception as e:
        gpt_response = f"Error: {e}"
    chat_box.insert(tk.END, "ChatGPT: " + gpt_response + "\n")

#GUI
window = tk.Tk()
window.title("ChatGPT")
window.geometry("600x500")

chat_box = tk.Text(window, width=70, height=25)
chat_box.pack(padx=10, pady=10)

entry = tk.Entry(window, width=60)
entry.pack(side=tk.LEFT, padx=(10,0), pady=(0,10))

send_button = tk.Button(window, text="Send", width=10, command=send_message)
send_button.pack(side=tk.LEFT, padx=(5,10), pady=(0,10))

window.mainloop()
