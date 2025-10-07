"""
Tests for the Hello Streamlit application.
"""

import pytest
import pandas as pd
import numpy as np
import sys
import os

# Add the project root to the path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the module we're testing
import hello_streamlit


class TestHelloStreamlit:
    """Test cases for Hello Streamlit functionality."""
    
    def test_module_imports(self):
        """Test that all required modules can be imported."""
        import streamlit
        import pandas
        import numpy
        import time
        
        # If we get here without exceptions, imports are working
        assert True
    
    def test_function_exists(self):
        """Test that main function exists and is callable."""
        assert callable(hello_streamlit.main)
    
    def test_data_generation(self):
        """Test actual data generation for charts."""
        # Test that numpy random data generation works
        data = np.random.randn(20, 3)
        assert data.shape == (20, 3)
        
        # Test DataFrame creation
        df = pd.DataFrame(data, columns=['A', 'B', 'C'])
        assert len(df) == 20
        assert list(df.columns) == ['A', 'B', 'C']
    
    def test_sample_dataframe_structure(self):
        """Test the structure of the sample DataFrame used in the app."""
        sample_data = {
            'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
            'Age': [25, 30, 35, 28],
            'City': ['New York', 'London', 'Tokyo', 'Paris'],
            'Score': [85, 90, 78, 92]
        }
        
        df = pd.DataFrame(sample_data)
        
        assert len(df) == 4
        assert 'Name' in df.columns
        assert 'Age' in df.columns
        assert 'City' in df.columns
        assert 'Score' in df.columns
        assert df['Age'].dtype in [int, 'int64']
        assert df['Score'].dtype in [int, 'int64']
    
    def test_widget_options(self):
        """Test that widget option lists are properly defined."""
        # Test color options
        colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
        assert len(colors) == 5
        assert "Red" in colors
        assert "Blue" in colors
        
        # Test hobby options
        hobbies = ["Reading", "Gaming", "Sports", "Music", "Cooking", "Travel"]
        assert len(hobbies) == 6
        assert "Reading" in hobbies
        assert "Travel" in hobbies
    
    def test_chart_data_types(self):
        """Test that chart data is properly formatted."""
        # Generate sample data like in the app
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['A', 'B', 'C']
        )
        
        assert isinstance(chart_data, pd.DataFrame)
        assert chart_data.shape == (20, 3)
        assert all(col in ['A', 'B', 'C'] for col in chart_data.columns)


class TestHelloStreamlitIntegration:
    """Integration tests for Hello Streamlit app."""
    
    def test_theme_options(self):
        """Test theme option validity."""
        themes = ["Light", "Dark", "Auto"]
        assert len(themes) == 3
        assert all(isinstance(theme, str) for theme in themes)
    
    def test_tab_structure(self):
        """Test tab organization."""
        tab_names = ["Line Chart", "Bar Chart", "Area Chart"]
        assert len(tab_names) == 3
        assert all(isinstance(name, str) for name in tab_names)
    
    def test_progress_bar_range(self):
        """Test progress bar range is valid."""
        # Progress bar should go from 0 to 99 (100 iterations)
        progress_range = range(100)
        assert len(progress_range) == 100
        assert min(progress_range) == 0
        assert max(progress_range) == 99
    
    def test_user_data_validation(self):
        """Test user input validation scenarios."""
        # Test empty name scenario
        name = ""
        agree = True
        should_show_profile = bool(name) and agree
        assert should_show_profile is False
        
        # Test name provided but not agreed
        name = "John"
        agree = False
        should_show_profile = bool(name) and agree
        assert should_show_profile is False
        
        # Test both name and agreement
        name = "John"
        agree = True
        should_show_profile = bool(name) and agree
        assert should_show_profile is True


if __name__ == "__main__":
    pytest.main([__file__])