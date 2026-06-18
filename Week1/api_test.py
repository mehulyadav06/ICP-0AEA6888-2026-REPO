import google.generativeai as genai

API_KEY = "AQ.Ab8RN6Lk2SnRbwVEW1XsNdUk2njRixZ0AWMf0RE50ael6iBtBA"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash-lite")
user_input = "Hello! Introduce yourself"
response = model.generate_content(user_input)
print("Bot:", response.text)
