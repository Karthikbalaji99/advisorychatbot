import streamlit as st
from openai import AzureOpenAI
import time
import os

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint="your-azure-endpoint-here",
    api_key="your-api-key-here",
    api_version="your-api-version-here"
)

# Title of the app
st.title("Chatbot")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "current_chat" not in st.session_state:
    st.session_state.current_chat = []
if "current_chat_index" not in st.session_state:
    st.session_state.current_chat_index = -1

# Function to start a new chat
def start_new_chat():
    if st.session_state.current_chat:
        if st.session_state.current_chat_index == -1:
            st.session_state.chat_history.append(st.session_state.current_chat)
        else:
            st.session_state.chat_history[st.session_state.current_chat_index] = st.session_state.current_chat
    st.session_state.current_chat = []
    st.session_state.current_chat_index = -1

# Function to generate the system prompt structure
def generate_system_prompt():
    return """\
Task: Respond accurately to the user's query based on Preferhub content.

Role: Assume the role of a specialized assistant with a deep understanding of Preferhub Solutions.

Instructions: Provide precise, factual answers that reflect the content. If the query is unrelated to Preferhub, politely decline to answer.

Critical Instructions: Only use the provided content about Preferhub Solutions. Do not speculate or provide information beyond the available content.
"""

# Sidebar for chat history
with st.sidebar:
    st.subheader("Chat History")
    for i, chat in enumerate(st.session_state.chat_history):
        if st.button(f"Chat {i+1}", key=f"history_{i}"):
            st.session_state.current_chat = chat
            st.session_state.current_chat_index = i
            st.rerun()

    if st.button("➕ New Chat", key="new_chat_sidebar"):
        start_new_chat()
        st.rerun()

# Load the scraped content
file_path = os.path.join("scraped.txt")
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        website_content = file.read()
except FileNotFoundError:
    st.error(f"Error: File not found at {file_path}")
    website_content = "Content not available."

# Display current chat
for message in st.session_state.current_chat:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input area
prompt = st.chat_input("Ask me anything about Preferhub")

# Process the user's input
if prompt:
    # Display user's question
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user's question to the current chat
    st.session_state.current_chat.append({"role": "user", "content": prompt})
    
    # Display "Analyzing..." message
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Analyzing...")
    
    # Generate the system prompt
    system_prompt = generate_system_prompt()

    # OpenAI call using AzureOpenAI client
    response = client.chat.completions.create(
        model="your-model-name-here",
        temperature=0,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": website_content}
        ]
    )
    assistant_message = response.choices[0].message.content

    # Short delay to simulate analysis time
    time.sleep(1)

    # Update the message placeholder with the actual response
    message_placeholder.markdown(assistant_message)

    # Add assistant's response to the current chat
    st.session_state.current_chat.append({"role": "assistant", "content": assistant_message})

    # If we're modifying a chat from history, update it
    if st.session_state.current_chat_index != -1:
        st.session_state.chat_history[st.session_state.current_chat_index] = st.session_state.current_chat

    # Rerun the app to update the display
    st.rerun()
