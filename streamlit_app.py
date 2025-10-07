"""
Hello World Streamlit App with OpenAI Integration

A simple Streamlit application demonstrating basic UI components
and OpenAI API integration for chat completions.
"""

import streamlit as st
import os
from dotenv import load_dotenv
from src.openai_example import get_openai_client, simple_chat_completion

# Load environment variables
load_dotenv()

def main():
    """Main application function."""
    
    # Page configuration
    st.set_page_config(
        page_title="Hello World - OpenAI Chat",
        page_icon="🤖",
        layout="wide"
    )
    
    # Title and description
    st.title("🤖 Hello World - OpenAI Chat App")
    st.markdown("""
    Welcome to your first Streamlit app with OpenAI integration! 
    This app demonstrates basic Streamlit components and AI-powered chat.
    """)
    
    # Sidebar for configuration
    st.sidebar.header("⚙️ Configuration")
    
    # Check API key status
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_actual_api_key_here":
        st.sidebar.error("🔑 OpenAI API Key not configured!")
        st.sidebar.markdown("""
        **To use this app:**
        1. Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
        2. Add it to your `.env` file
        3. Restart the app
        """)
        api_configured = False
    else:
        st.sidebar.success("🔑 OpenAI API Key configured!")
        api_configured = True
    
    # App settings in sidebar
    st.sidebar.subheader("🎛️ Chat Settings")
    max_tokens = st.sidebar.slider("Max Response Length", 50, 500, 150)
    temperature = st.sidebar.slider("Creativity (Temperature)", 0.0, 2.0, 1.0, 0.1)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("💬 Chat with AI")
        
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []
            st.session_state.messages.append({
                "role": "assistant", 
                "content": "Hello! I'm your AI assistant. How can I help you today?"
            })
        
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Type your message here..."):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generate AI response
            if api_configured:
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        try:
                            # Get response from OpenAI
                            response = get_ai_response(prompt, max_tokens, temperature)
                            st.markdown(response)
                            
                            # Add assistant response to chat history
                            st.session_state.messages.append({
                                "role": "assistant", 
                                "content": response
                            })
                        except Exception as e:
                            error_msg = f"Sorry, I encountered an error: {str(e)}"
                            st.error(error_msg)
                            st.session_state.messages.append({
                                "role": "assistant", 
                                "content": error_msg
                            })
            else:
                with st.chat_message("assistant"):
                    error_msg = "Please configure your OpenAI API key to use chat functionality."
                    st.error(error_msg)
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": error_msg
                    })
    
    with col2:
        st.header("📊 App Info")
        
        # Display some metrics
        st.metric("Messages in Chat", len(st.session_state.messages))
        st.metric("API Status", "✅ Ready" if api_configured else "❌ Not Ready")
        
        # Sample prompts
        st.subheader("💡 Try These Prompts")
        sample_prompts = [
            "Tell me a joke",
            "Explain quantum computing",
            "Write a haiku about coding",
            "What's the weather like on Mars?",
            "Recommend a good book"
        ]
        
        for prompt in sample_prompts:
            if st.button(prompt, key=f"sample_{prompt}"):
                if api_configured:
                    # Add to chat
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    st.rerun()
        
        # Clear chat button
        if st.button("🗑️ Clear Chat", type="secondary"):
            st.session_state.messages = [{
                "role": "assistant", 
                "content": "Hello! I'm your AI assistant. How can I help you today?"
            }]
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    **Built with:** Streamlit 🚀 | **Powered by:** OpenAI GPT 🤖 | **Language:** Python 🐍
    
    *This is a demo application showing Streamlit + OpenAI integration.*
    """)

@st.cache_data
def get_ai_response(prompt: str, max_tokens: int = 150, temperature: float = 1.0) -> str:
    """
    Get response from OpenAI API with caching.
    
    Args:
        prompt: User input prompt
        max_tokens: Maximum tokens in response
        temperature: Creativity level (0.0 to 2.0)
    
    Returns:
        AI response string
    """
    try:
        client = get_openai_client()
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful and friendly AI assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"OpenAI API error: {str(e)}")

if __name__ == "__main__":
    main()