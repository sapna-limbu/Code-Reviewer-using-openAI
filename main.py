import streamlit as st
import os
from openai import OpenAI

# Load OpenAI API key
def load_api_key():
    try:
        # Specify the directory path
        directory = r"C:\Users\RATNADEEP\Desktop\backend\openAi"
        file_name = '.openai_api_key.txt'
        
        # Combine the directory path with the file name
        file_path = os.path.join(directory, file_name)

        # Open the file
        with open(file_path) as f:
            # Read the API key
            OPENAI_API_KEY = f.read().strip()  # Remove leading/trailing whitespace
        
        return OPENAI_API_KEY
    
    except FileNotFoundError:
        st.error(f"File '{file_path}' not found. Please make sure the file exists in the specified directory.")
        st.stop()
    except Exception as e:
        st.error("An error occurred:", e)
        st.stop()

# Initialize OpenAI client
def initialize_openai_client():
    OPENAI_API_KEY = load_api_key()
    return OpenAI(api_key=OPENAI_API_KEY)

# Main function for code review
def code_rev(prompt, client):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
           {"role": "system", "content": """you are a helpful AI Assistant. 
                                      Given a Python code review app for bug detection and fixes"""},  
           {"role": "user", "content": prompt}
       ]
   )

    return response.choices[0].message.content

# Streamlit app
def main():
    st.title("Python Code Review App")
    prompt = st.text_area("Enter your code:")

    if st.button("Submit"):
        client = initialize_openai_client()
        if client:
            response = code_rev(prompt, client)
            st.write("Review Feedback:")
            st.write(response)

if __name__ == "__main__":
    main()
