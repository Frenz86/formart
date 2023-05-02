import streamlit as st
import json

with open("users.json") as f:
    users = json.load(f)
    print(users)

def authenticate(username, password):
    """Check if username and Passw."""
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False


st.header('Login')
username = st.text_input('Username')
password = st.text_input('Password', type='password')

if st.button('Login'):
    if authenticate(username, password):
        st.success('Logged in as {}'.format(username))
    else:
        st.error('Invalid username or password')