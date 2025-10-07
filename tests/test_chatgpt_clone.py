"""
Tests for the ChatGPT clone Streamlit application.
"""

import pytest
import os
from unittest.mock import patch, Mock
import sys

# Add the project root to the path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the module we're testing
import chatgpt_clone


class TestChatGPTClone:
    """Test cases for ChatGPT clone functionality."""
    
    @patch('chatgpt_clone.get_openai_client')
    def test_get_chat_response_success(self, mock_get_client):
        """Test successful chat response generation."""
        # Mock OpenAI client and response
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_choice.message.content = "AI response"
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        mock_get_client.return_value = mock_client
        
        # Mock session state with proper object structure
        mock_session_state = Mock()
        mock_session_state.messages = [
            {"role": "user", "content": "Previous question"},
            {"role": "assistant", "content": "Previous answer"}
        ]
        
        with patch('chatgpt_clone.st') as mock_st:
            mock_st.session_state = mock_session_state
            
            result = chatgpt_clone.get_chat_response("Test prompt")
            
            assert result == "AI response"
            
            # Verify the API call was made with correct parameters
            mock_client.chat.completions.create.assert_called_once()
            call_args = mock_client.chat.completions.create.call_args
            
            assert call_args[1]["model"] == "gpt-3.5-turbo"
            assert call_args[1]["max_tokens"] == 1000
            assert call_args[1]["temperature"] == 0.7
            
            # Check that messages include system message, history, and new prompt
            messages = call_args[1]["messages"]
            assert len(messages) >= 4  # system + 2 history + 1 new prompt
            assert messages[0]["role"] == "system"
            assert messages[0]["content"] == "You are ChatGPT, a helpful AI assistant."
    
    @patch('chatgpt_clone.get_openai_client')
    def test_get_chat_response_with_long_history(self, mock_get_client):
        """Test chat response with long conversation history (should limit to last 10)."""
        # Create a long message history (15 messages)
        long_history = []
        for i in range(15):
            long_history.append({"role": "user", "content": f"Message {i}"})
            long_history.append({"role": "assistant", "content": f"Response {i}"})
        
        # Mock OpenAI client
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_choice.message.content = "AI response"
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        mock_get_client.return_value = mock_client
        
        # Mock session state with proper object structure
        mock_session_state = Mock()
        mock_session_state.messages = long_history
        
        with patch('chatgpt_clone.st') as mock_st:
            mock_st.session_state = mock_session_state
            
            chatgpt_clone.get_chat_response("New prompt")
            
            # Verify the API call
            call_args = mock_client.chat.completions.create.call_args
            messages = call_args[1]["messages"]
            
            # Should have system message + last 10 history messages + new prompt = 12 total
            assert len(messages) == 12
            assert messages[0]["role"] == "system"
            assert messages[-1]["content"] == "New prompt"
    
    @patch('chatgpt_clone.get_openai_client')
    def test_get_chat_response_api_error(self, mock_get_client):
        """Test handling of OpenAI API errors."""
        # Mock client to raise an exception
        mock_get_client.side_effect = Exception("API Error")
        
        # Mock session state with proper object structure
        mock_session_state = Mock()
        mock_session_state.messages = []
        
        with patch('chatgpt_clone.st') as mock_st:
            mock_st.session_state = mock_session_state
            
            with pytest.raises(Exception, match="API Error"):
                chatgpt_clone.get_chat_response("Test prompt")
    
    @patch('chatgpt_clone.get_openai_client')
    def test_get_chat_response_empty_history(self, mock_get_client):
        """Test chat response with empty conversation history."""
        # Mock OpenAI client
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_choice.message.content = "Hello! How can I help you?"
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        mock_get_client.return_value = mock_client
        
        # Mock session state with proper object structure
        mock_session_state = Mock()
        mock_session_state.messages = []
        
        with patch('chatgpt_clone.st') as mock_st:
            mock_st.session_state = mock_session_state
            
            result = chatgpt_clone.get_chat_response("Hello")
            
            assert result == "Hello! How can I help you?"
            
            # Verify the API call
            call_args = mock_client.chat.completions.create.call_args
            messages = call_args[1]["messages"]
            
            # Should have system message + new prompt = 2 total
            assert len(messages) == 2
            assert messages[0]["role"] == "system"
            assert messages[1]["content"] == "Hello"


class TestChatGPTCloneIntegration:
    """Integration tests for ChatGPT clone."""
    
    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"})
    @patch('chatgpt_clone.get_openai_client')
    def test_end_to_end_conversation(self, mock_get_client):
        """Test a complete conversation flow."""
        # Mock OpenAI client
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_choice.message.content = "Hello! How can I help you?"
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        mock_get_client.return_value = mock_client
        
        # Mock session state with proper object structure
        mock_session_state = Mock()
        mock_session_state.messages = []
        
        with patch('chatgpt_clone.st') as mock_st:
            mock_st.session_state = mock_session_state
            
            # Test the response function
            response = chatgpt_clone.get_chat_response("Hello")
            
            assert response == "Hello! How can I help you?"
            mock_get_client.assert_called_once()
            mock_client.chat.completions.create.assert_called_once()
    
    def test_module_imports(self):
        """Test that all required modules can be imported."""
        import streamlit
        import os
        from dotenv import load_dotenv
        from src.openai_example import get_openai_client
        
        # If we get here without exceptions, imports are working
        assert True
    
    def test_function_exists(self):
        """Test that main functions exist and are callable."""
        assert callable(chatgpt_clone.main)
        assert callable(chatgpt_clone.get_chat_response)


if __name__ == "__main__":
    pytest.main([__file__])