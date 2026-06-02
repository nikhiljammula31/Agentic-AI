#streamlit
#pip3 install streamlit

import streamlit as st
st.title("Ai Agnet with groq ")
st.header("Welcome to thee AI agent powered by Groq")
st.subheader("Capabilites")
st.write("this is the simple streamlit applicationn app that demonstarate the use of an AI")
st.text("To get started simpply enter a prompt in the text box below and convert ")
st.markdown("### Example prompt")
st.markdown("-**General Query: ** What is capital of france")
st.header("try it out")
user_input= st.text_input("Enter ur name here..")
st.write("hello,{user_input} welcome to the Ai agent with groq")
number_input=st.number_input("Enter a number a to see it ssquare",min_value=0)
if number_input:
    st.write(f"The square of {number_input} is {number_input ** 2} ")
user_password=st.text_input("Enter a pass",type="password")
if user_password:
    st.write("password recived . your pasword is secure with us")
gender=st.radio("select ur gender",["Male","Female"])
st.write(f"you selected : {gender}")
agrement= st.checkbox("I acept the terms and conditions")
if agrement:
    st.write("Thank u for agreing the terms and conditions")
if st.button("Submit"):
    st.write("Generating response...")