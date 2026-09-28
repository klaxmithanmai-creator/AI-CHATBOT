import streamlit as st
import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    "Name": ["Laxmi", "Ravi", "Anu"],
    "Age": [20, 22, 21],
    "City": ["Hyderabad", "Delhi", "Chennai"]
})

# Example dictionary for JSON
data = {
    "Name": "Laxmi",
    "Age": 20,
    "Skills": ["Python", "AutoCAD"]
}

st.title("AI CHATBOT")
st.header("ABOUT")
st.subheader("DETAILS")
st.text("HELLO WORLD")
st.markdown("**Hello World**")
st.caption("This is Caption")
st.code("print('Hello')", language="python")
st.latex(r"E=mc^2")
st.divider()

name = st.text_input("Enter your Name")
message = st.text_area("Enter your Message")
age = st.number_input("Enter your age", min_value=0)
value = st.slider("Select a value", 0, 100)
option = st.selectbox("Choose an Option", ["A", "B", "C"])
options = st.multiselect("Choose options", ["A", "B", "C"])
choice = st.radio("Select your Gender", ["male", "female"])
agree = st.checkbox("I agree")
status = st.toggle("Enable feature")

date = st.date_input("Select a date")
time = st.time_input("Select a time")
file = st.file_uploader("Upload a file")
color = st.color_picker("Choose a color", "#000000")

if st.button("Click me"):
    st.success("Operation Completed Successfully!")
    st.info("This is some information")
    st.warning("Please Be Careful")

    st.dataframe(df)
    st.table(df)
    st.metric("Sales", "50,000 Rs")
    st.json(data)
    st.write("Hello World")

# Custom CSS
st.markdown(
    """
    <style>
    .stApp h1 {
        color: #4CAF50;
        text-align: center;
        font-family: 'Arial Black', sans-serif;
    }

    .stApp h2 {
        color: #2196F3;
        font-family: 'Verdana', sans-serif;
    }

    .stApp h3 {
        color: #FF5722;
        font-style: italic;
    }

    .stButton>button {
        background-color: #673AB7;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
    }

    .stButton>button:hover {
        background-color: #9575CD;
        color: #000;
    }

    .stCheckbox>label {
        color: #009688;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
) 