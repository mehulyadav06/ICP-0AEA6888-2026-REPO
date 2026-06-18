import google.generativeai as genai

API_KEY = "YOUR API KEY"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash-lite")

chat = model.start_chat(history=[])

while True:

    try:

        user_input = input("You: ")

        if user_input.lower() == "exit":

            break

        response = chat.send_message(user_input)

        print("Bot:", response.text)

    except Exception as e:

        print("Error:", e)
