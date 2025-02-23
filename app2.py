import streamlit as st
import google.generativeai as genai

# Configure Gemini AI with API Key
genai.configure(api_key="")

# Define System Prompt for AI Model
sys_prompt = """
You are an advanced Python code reviewer. Your task is to analyze the given Python code, 
identify potential bugs, logical errors, and areas of improvement, and suggest fixes.
Your response should be structured as follows:

1. **Issues Detected**: List any errors, inefficiencies, or improvements needed.
2. **Fixed Code**: Provide the corrected version of the code.
3. **Explanation**: Explain why the changes were made concisely.

If the code is already optimal, acknowledge it and suggest best practices.
"""

# Load Gemini AI Model
model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=sys_prompt)

# Streamlit App UI
st.set_page_config(page_title="Python Code Reviewer", page_icon="🔍", layout="centered")

st.title("🚀 AI-Powered Python Code Reviewer")
st.write("Analyze your Python code with **Gemini AI** and get instant feedback on potential issues, errors, and improvements.")

st.markdown("### 📝 Paste your Python code below:")

# User Input
user_prompt = st.text_area("Enter your Python code:", height=200, placeholder="Write or paste your Python code here...")

# Submit Button
if st.button("🔍 Review Code"):
    if user_prompt.strip():
        # Generate AI Response
        response = model.generate_content(user_prompt)
        
        st.subheader("📌 AI Review & Suggestions")
        st.markdown(response.text)  # Display AI's response
    else:
        st.warning("⚠ Please enter some Python code before submitting.")
