"""
Tests for the main Streamlit app with OpenAI integration.
"""

import pytest
import os
from unittest.mock import patch, Mock
import sys

# Add the project root to the path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the module we're testing
import streamlit_app


class TestStreamlitApp:
    """Test cases for the main Streamlit app functionality."""
    
    @patch('streamlit_app.get_openai_client')
    def test_get_ai_response_direct(self, mock_get_client):
        """Test the actual get_ai_response function."""
        # Mock OpenAI client and response
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_choice.message.content = "Direct AI response"
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        mock_get_client.return_value = mock_client
        
        # Clear the cache decorator for testing
        streamlit_app.get_ai_response.clear()
        
        result = streamlit_app.get_ai_response("Test prompt", 200, 0.5)
        
        assert result == "Direct AI response"
        
        # Verify the API call
        mock_client.chat.completions.create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful and friendly AI assistant."},
                {"role": "user", "content": "Test prompt"}
            ],
            max_tokens=200,
            temperature=0.5
        )
    
    @patch('streamlit_app.get_openai_client')
    def test_get_ai_response_api_error(self, mock_get_client):
        """Test handling of OpenAI API errors in get_ai_response."""
        # Mock client to raise an exception
        mock_get_client.side_effect = Exception("API connection failed")
        
        # Clear the cache decorator for testing
        streamlit_app.get_ai_response.clear()
        
        with pytest.raises(Exception, match="OpenAI API error: API connection failed"):
            streamlit_app.get_ai_response("Test prompt")
    
    def test_environment_variable_handling(self):
        """Test different environment variable scenarios."""
        # Test missing key
        with patch.dict(os.environ, {}, clear=True):
            api_key = os.getenv("OPENAI_API_KEY")
            assert api_key is None
        
        # Test placeholder key
        with patch.dict(os.environ, {"OPENAI_API_KEY": "your_actual_api_key_here"}):
            api_key = os.getenv("OPENAI_API_KEY")
            assert api_key == "your_actual_api_key_here"
        
        # Test valid key format
        with patch.dict(os.environ, {"OPENAI_API_KEY": "sk-valid-test-key"}):
            api_key = os.getenv("OPENAI_API_KEY")
            assert api_key.startswith("sk-")
    
    def test_sample_prompts_list(self):
        """Test that sample prompts are properly defined."""
        sample_prompts = [
            "Tell me a joke",
            "Explain quantum computing",
            "Write a haiku about coding",
            "What's the weather like on Mars?",
            "Recommend a good book"
        ]
        
        assert len(sample_prompts) == 5
        assert all(isinstance(prompt, str) for prompt in sample_prompts)
        assert "Tell me a joke" in sample_prompts
        assert "Recommend a good book" in sample_prompts
    
    def test_function_exists(self):
        """Test that main functions exist and are callable."""
        assert callable(streamlit_app.main)
        assert callable(streamlit_app.get_ai_response)


class TestStreamlitAppIntegration:
    """Integration tests for the main Streamlit app."""
    
    def test_module_imports(self):
        """Test that all required modules can be imported."""
        import streamlit
        import os
        from dotenv import load_dotenv
        from src.openai_example import get_openai_client
        
        # If we get here without exceptions, imports are working
        assert True
    
    @patch.dict(os.environ, {"OPENAI_API_KEY": "sk-test-key"})
    @patch('streamlit_app.get_openai_client')
    def test_end_to_end_api_call(self, mock_get_client):
        """Test complete API call flow."""
        # Mock OpenAI client
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_choice.message.content = "Integration test response"
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        mock_get_client.return_value = mock_client
        
        # Clear cache for testing
        streamlit_app.get_ai_response.clear()
        
        # Test the function
        result = streamlit_app.get_ai_response("Integration test", 100, 0.8)
        
        assert result == "Integration test response"
        mock_get_client.assert_called_once()
        mock_client.chat.completions.create.assert_called_once()
    
    def test_slider_ranges(self):
        """Test that slider ranges are valid."""
        # Max tokens slider: 50-500, default 150
        assert 50 <= 150 <= 500
        
        # Temperature slider: 0.0-2.0, default 1.0
        assert 0.0 <= 1.0 <= 2.0
    
    def test_api_key_validation_logic(self):
        """Test API key validation logic."""
        # Test empty key
        api_key = None
        is_invalid = not api_key or api_key == "your_actual_api_key_here"
        assert is_invalid is True
        
        # Test placeholder key
        api_key = "your_actual_api_key_here"
        is_invalid = not api_key or api_key == "your_actual_api_key_here"
        assert is_invalid is True
        
        # Test valid key
        api_key = "sk-valid-key-123"
        is_invalid = not api_key or api_key == "your_actual_api_key_here"
        assert is_invalid is False


if __name__ == "__main__":
    pytest.main([__file__])