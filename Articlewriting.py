import openai
import streamlit as st

openai.api_key = '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'

def main():
    st.title("Article Writer")
    notes = st.text_area("Enter Topic Information:")
    content = "I want you to write a short literature review on the topic " + notes
    if st.button("Generate Article"):
        with st.spinner("Generating Article..."):
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=content,
                max_tokens=200
            )
        description = response["choices"][0]["text"]
        st.subheader("Generated Writeup:")
        st.write(description)

if __name__ == '__main__':
   main()
