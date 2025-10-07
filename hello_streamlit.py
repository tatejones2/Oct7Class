"""
Simple Hello World Streamlit App

A minimal example demonstrating basic Streamlit components.
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

def main():
    """Simple hello world app."""
    
    # Page config
    st.set_page_config(page_title="Hello Streamlit", page_icon="👋")
    
    # Title
    st.title("👋 Hello, Streamlit!")
    st.write("Welcome to your first Streamlit app!")
    
    # User input
    name = st.text_input("What's your name?", placeholder="Enter your name here")
    
    if name:
        st.write(f"Hello, **{name}**! Nice to meet you! 🎉")
    
    # Interactive widgets
    st.header("🎛️ Interactive Widgets")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider("How old are you?", 0, 100, 25)
        favorite_color = st.selectbox("What's your favorite color?", 
                                    ["Red", "Green", "Blue", "Yellow", "Purple"])
        
    with col2:
        hobbies = st.multiselect("What are your hobbies?", 
                               ["Reading", "Gaming", "Sports", "Music", "Cooking", "Travel"])
        agree = st.checkbox("I love Streamlit!")
    
    # Display results
    if name and agree:
        st.success(f"Awesome, {name}! Here's what we know about you:")
        st.write(f"- **Age:** {age} years old")
        st.write(f"- **Favorite Color:** {favorite_color}")
        if hobbies:
            st.write(f"- **Hobbies:** {', '.join(hobbies)}")
    
    # Data visualization
    st.header("📊 Data Visualization")
    
    # Generate sample data
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    # Display different chart types
    tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])
    
    with tab1:
        st.line_chart(chart_data)
    
    with tab2:
        st.bar_chart(chart_data)
    
    with tab3:
        st.area_chart(chart_data)
    
    # Sample dataframe
    st.header("📋 Sample Data")
    sample_df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'London', 'Tokyo', 'Paris'],
        'Score': [85, 90, 78, 92]
    })
    
    st.dataframe(sample_df, use_container_width=True)
    
    # Interactive button
    if st.button("🎉 Click me for a surprise!"):
        st.balloons()
        st.success("Surprise! You found the balloons! 🎈")
    
    # Progress bar demo
    if st.button("⏳ Show Progress Bar"):
        progress_text = "Operation in progress..."
        my_bar = st.progress(0, text=progress_text)
        
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, 
                          text=f"{progress_text} {percent_complete + 1}%")
        
        st.success("Operation completed! ✅")
    
    # Sidebar
    st.sidebar.header("🔧 App Settings")
    st.sidebar.write("This is the sidebar!")
    
    theme = st.sidebar.radio("Choose a theme:", ["Light", "Dark", "Auto"])
    st.sidebar.write(f"Selected theme: {theme}")
    
    # Footer
    st.markdown("---")
    st.markdown("Built with ❤️ using Streamlit")

if __name__ == "__main__":
    main()