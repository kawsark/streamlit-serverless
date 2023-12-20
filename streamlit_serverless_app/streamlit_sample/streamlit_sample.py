import streamlit as st

# Streamlit configuration
st.title("Streamlit Serverless example with ECS Fargate")

# Create a column with two rows
col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.image("assets/assistant_logo.png", width=50)
with col2:
    st.text("You have successfully accessed a Streamlit serverless app")
    st.text("Continue to build your app here and run cdk deploy")
