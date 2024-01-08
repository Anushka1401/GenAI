import openai
import streamlit as st
import os

# Set your OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = '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'

# Create OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    st.title("Article Writer")
    notes = st.text_area("Enter Topic Information:")
    content = "I want you to write a short literature review on the topic " + notes
    if st.button("Generate Article"):
        with st.spinner("Generating Article..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{'role': 'system', 'content': 'You are a helpful assistant.'},
                          {'role': 'user', 'content': content}]
            )
        description = response['choices'][0]['message']['content']
        st.subheader("Generated Writeup:")
        st.write(description)

if __name__ == '__main__':
    main()
