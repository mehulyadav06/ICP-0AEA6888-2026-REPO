import google.generativeai as genai

# Replace with your Gemini API Key
API_KEY = "YOUR_API_KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": ["You are a helpful AI assistant."]
        }
    ]
)

print("=== Gemini Chatbot ===")
print("Type 'exit' to quit.\n")

while True:
    try:
        user_input = input("You: ")

        # Empty input handling
        if user_input.strip() == "":
            print("Bot: Please enter a message.")
            continue

        # Exit command
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        response = chat.send_message(user_input)

        print("Bot:", response.text)

    except Exception as e:
        print("Error:", e)
