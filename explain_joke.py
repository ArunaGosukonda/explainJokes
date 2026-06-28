import openai
import streamlit as st
import os
from openai import OpenAI

token = os.environ.get("GITHUB_TOKEN")
endpoint = "https://models.inference.ai.azure.com"
modelName = "gpt-4o-mini"

client = OpenAI(api_key=token, base_url=endpoint)

def explain_joke(joke):
    try:
        response = client.chat.completions.create(
            model=modelName,
            messages=[
                {"role": "user", "content": f"Explain the joke: {joke}"}
            ]
        )
        explanation = response.choices[0].message.content
        return explanation
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit application
st.title("Joke Explainer")

# Text input for the joke
joke_input = st.text_area("Enter your joke here:")

# Submit button
if st.button("Submit"):
    if joke_input:
        explanation = explain_joke(joke_input)
        st.subheader("Joke Explanation:")
        st.write(explanation)
    else:
        st.warning("Please enter a joke before submitting.")