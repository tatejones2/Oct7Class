"""
Example of using OpenAI API with environment variables.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()


def get_openai_client():
    """
    Create and return an OpenAI client using API key from environment.
    
    Returns:
        OpenAI: Configured OpenAI client
        
    Raises:
        ValueError: If OPENAI_API_KEY is not set
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_actual_api_key_here":
        raise ValueError(
            "OPENAI_API_KEY not found or not set properly. "
            "Please set it in your .env file."
        )
    
    return OpenAI(api_key=api_key)


def simple_chat_completion(prompt: str) -> str:
    """
    Get a simple chat completion from OpenAI.
    
    Args:
        prompt: The user prompt
        
    Returns:
        The AI response
    """
    client = get_openai_client()
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    
    return response.choices[0].message.content


if __name__ == "__main__":
    try:
        # Example usage
        result = simple_chat_completion("Hello! How are you?")
        print(f"AI Response: {result}")
    except ValueError as e:
        print(f"Configuration Error: {e}")
    except Exception as e:
        print(f"Error: {e}")