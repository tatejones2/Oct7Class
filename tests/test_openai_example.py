"""
Tests for OpenAI integration example.
"""

import os
import pytest
from unittest.mock import patch, Mock
from src.openai_example import get_openai_client, simple_chat_completion


class TestOpenAIIntegration:
    """Test cases for OpenAI integration."""
    
    @patch.dict(os.environ, {}, clear=True)
    def test_get_openai_client_missing_api_key(self):
        """Test that missing API key raises ValueError."""
        with pytest.raises(ValueError, match="OPENAI_API_KEY not found"):
            get_openai_client()
    
    @patch.dict(os.environ, {"OPENAI_API_KEY": "your_actual_api_key_here"})
    def test_get_openai_client_placeholder_api_key(self):
        """Test that placeholder API key raises ValueError."""
        with pytest.raises(ValueError, match="OPENAI_API_KEY not found"):
            get_openai_client()
    
    @patch.dict(os.environ, {"OPENAI_API_KEY": "sk-test123"})
    @patch('src.openai_example.OpenAI')
    def test_get_openai_client_success(self, mock_openai):
        """Test successful client creation with valid API key."""
        mock_client = Mock()
        mock_openai.return_value = mock_client
        
        result = get_openai_client()
        
        mock_openai.assert_called_once_with(api_key="sk-test123")
        assert result == mock_client
    
    @patch('src.openai_example.get_openai_client')
    def test_simple_chat_completion(self, mock_get_client):
        """Test simple chat completion function."""
        # Mock the client and response
        mock_client = Mock()
        mock_choice = Mock()
        mock_choice.message.content = "Hello! I'm doing well, thank you!"
        mock_response = Mock()
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        mock_get_client.return_value = mock_client
        
        result = simple_chat_completion("Hello! How are you?")
        
        assert result == "Hello! I'm doing well, thank you!"
        mock_client.chat.completions.create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello! How are you?"}],
            max_tokens=150
        )