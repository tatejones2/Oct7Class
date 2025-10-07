"""
Simple ChatGPT-like Interface

A minimal chat interface that mimics ChatGPT's core functionality.
Clean, simple, and focused on conversation.
"""

import streamlit as st
import os
from dotenv import load_dotenv
from src.openai_example import get_openai_client

# Load environment variables
load_dotenv()

def main():
    """Main chat application."""
    
    # Page config - minimal and clean
    st.set_page_config(
        page_title="ChatGPT Clone",
        page_icon="💬",
        layout="centered"
    )
    
    # Header with clear button
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title("💬 ChatGPT")
    with col2:
        if st.button("🗑️ Clear Chat", type="secondary"):
            st.session_state.messages = []
            st.rerun()
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Message ChatGPT..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner(""):
                try:
                    response = get_chat_response(prompt)
                    st.markdown(response)
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    error_msg = f"I'm sorry, I encountered an error: {str(e)}"
                    st.markdown(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})

def get_chat_response(prompt: str) -> str:
    """
    Get response from OpenAI API.
    
    Args:
        prompt: User input
        
    Returns:
        AI response
    """
    client = get_openai_client()
    
    # Build message history for context
    messages = [{"role": "system", "content": "You are ChatGPT, a helpful AI assistant."}]
    
    # Add conversation history (last 10 messages for context)
    recent_messages = st.session_state.messages[-10:] if len(st.session_state.messages) > 10 else st.session_state.messages
    for msg in recent_messages:
        messages.append({"role": msg["role"], "content": msg["content"]})
    
    # Add current prompt
    messages.append({"role": "user", "content": prompt})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000,
        temperature=0.7
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    main()