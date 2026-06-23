import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

st.title("AI Content Summarizer")

text = st.text_area(
    "Paste Article Content",
    height=300
)

summary_type = st.selectbox(
    "Summary Type",
    ["Short", "Detailed", "Bullet Points"]
)

if st.button("Generate Summary"):

    if text:

        prompt = f"""
        Summarize the following content.

        Type: {summary_type}

        Content:
        {text}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        st.subheader("Summary")

        st.write(
            response.choices[0].message.content
        )
