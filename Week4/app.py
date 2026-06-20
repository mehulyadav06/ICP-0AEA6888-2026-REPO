import streamlit as st

from summarizer import summarize_text
from pdf_reader import extract_text

st.title("AI Content Summarizer")

option = st.radio(
    "Choose Input Type",
    ["Text", "PDF"]
)

length = st.selectbox(
    "Summary Length",
    ["Short", "Medium", "Detailed"]
)

content = ""

if option == "Text":

    content = st.text_area(
        "Paste Your Content"
    )

else:

    pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if pdf:
        content = extract_text(pdf)

if st.button("Generate Summary"):

    if content:

        with st.spinner("Generating..."):

            summary = summarize_text(
                content,
                length
            )

            st.subheader("Summary")

            st.write(summary)

    else:

        st.warning(
            "Please provide content"
        )
