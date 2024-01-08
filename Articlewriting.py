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
                model="text-davinci-003",
                prompt=content,
                temperature=0.7,
                max_tokens=300,
            )
        description = response.choices[0].text.strip()
        st.subheader("Generated Writeup:")
        st.write(description)

if __name__ == '__main__':
    main()
