# Streamlit Guide

A comprehensive guide to building web applications with Streamlit.

## What is Streamlit?

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. You can build interactive dashboards, data visualizations, and AI-powered applications with just a few lines of Python code.

## Key Features

- **Simple Python syntax** - No HTML, CSS, or JavaScript required
- **Interactive widgets** - Sliders, buttons, text inputs, file uploads, etc.
- **Real-time updates** - Apps automatically update when you change the code
- **Built-in data visualization** - Charts, maps, and tables
- **Easy deployment** - Share your apps with one command

## Basic Streamlit Components

### 1. Text and Markdown
```python
import streamlit as st

# Title
st.title("My Streamlit App")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Regular text
st.text("This is regular text")

# Markdown
st.markdown("**Bold text** and *italic text*")

# Code
st.code("print('Hello, World!')", language='python')
```

### 2. Data Display
```python
import pandas as pd
import numpy as np

# DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
})
st.dataframe(df)

# Table (static)
st.table(df)

# Metrics
st.metric("Temperature", "25°C", "2°C")

# JSON
st.json({"name": "John", "age": 30})
```

### 3. Interactive Widgets
```python
# Text input
name = st.text_input("Enter your name:")

# Number input
age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)

# Slider
score = st.slider("Rate your experience:", 0, 10, 5)

# Selectbox
city = st.selectbox("Choose your city:", ["New York", "London", "Tokyo"])

# Multiselect
colors = st.multiselect("Choose colors:", ["Red", "Green", "Blue", "Yellow"])

# Button
if st.button("Click me!"):
    st.write("Button was clicked!")

# Checkbox
if st.checkbox("Show details"):
    st.write("Here are the details...")

# Radio buttons
option = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
```

### 4. Charts and Visualizations
```python
import matplotlib.pyplot as plt
import plotly.express as px

# Line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

# Bar chart
st.bar_chart(chart_data)

# Area chart
st.area_chart(chart_data)

# Matplotlib
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
st.pyplot(fig)

# Plotly
fig = px.scatter(df, x="Age", y="Name")
st.plotly_chart(fig)
```

### 5. Layout and Organization
```python
# Columns
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")
with col3:
    st.write("Column 3")

# Sidebar
st.sidebar.title("Sidebar")
sidebar_input = st.sidebar.text_input("Sidebar input:")

# Expander
with st.expander("Click to expand"):
    st.write("Hidden content here!")

# Tabs
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.write("Content for tab 1")
with tab2:
    st.write("Content for tab 2")
with tab3:
    st.write("Content for tab 3")

# Container
container = st.container()
container.write("This is inside a container")
```

### 6. Status Elements
```python
# Success message
st.success("Success! Operation completed.")

# Error message
st.error("Error! Something went wrong.")

# Warning message
st.warning("Warning! Please check your input.")

# Info message
st.info("Info: This is additional information.")

# Progress bar
import time
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
    time.sleep(0.01)

# Spinner
with st.spinner("Processing..."):
    time.sleep(3)
st.success("Done!")
```

### 7. Session State
```python
# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Use session state
if st.button("Increment"):
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")
```

## Running Streamlit Apps

### 1. Create your app
Save your Streamlit code in a `.py` file (e.g., `app.py`)

### 2. Run the app
```bash
streamlit run app.py
```

### 3. View in browser
The app will open automatically in your browser at `http://localhost:8501`

## Best Practices

1. **Use caching** for expensive operations:
   ```python
   @st.cache_data
   def load_data():
       # Expensive data loading operation
       return data
   ```

2. **Organize with functions**:
   ```python
   def main():
       st.title("My App")
       # App logic here
   
   if __name__ == "__main__":
       main()
   ```

3. **Handle errors gracefully**:
   ```python
   try:
       # Your code here
       pass
   except Exception as e:
       st.error(f"An error occurred: {e}")
   ```

4. **Use session state** for maintaining state across reruns

5. **Keep apps responsive** - avoid blocking operations in the main thread

## Deployment Options

1. **Streamlit Cloud** (Free)
2. **Heroku**
3. **AWS/GCP/Azure**
4. **Docker containers**

## Common Patterns

### Form Handling
```python
with st.form("my_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.write(f"Hello {name}! Email: {email}")
```

### File Processing
```python
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Process the file
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
```

### API Integration
```python
if st.button("Fetch Data"):
    with st.spinner("Loading..."):
        response = requests.get("https://api.example.com/data")
        data = response.json()
        st.json(data)
```

## Next Steps

1. **Practice** with the basic components
2. **Build** a simple app with your data
3. **Explore** advanced features like custom components
4. **Deploy** your app to share with others
5. **Learn** about performance optimization and caching

For more information, visit the [official Streamlit documentation](https://docs.streamlit.io/).