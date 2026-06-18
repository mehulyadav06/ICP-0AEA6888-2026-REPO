import google.generativeai as genai

API_KEY = "YOUR API KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash-lite")
user_input = "Hello! Introduce yourself"
response = model.generate_content(user_input)
print("Bot:", response.text)
