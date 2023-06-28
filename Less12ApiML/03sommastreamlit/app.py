import streamlit as st
import requests
import json

def main():
    st.title("API Frontend - POST-GET Debugger")
    url_API =st.text_input("inserisci url dell'api","http://localhost:8000/sum")
    num1x = st.number_input("Inserisci num1")
    num2x = st.number_input("Inserisci num2")

    ############## GET REQUEST #################
    if st.button("Predict with GET"):
        url = url_API
        url2 = f"?num1={num1x}&num2={num2x}"
        link = url+url2
        st.write('"{}"'.format(link))
        response = requests.get(link)
        result =response.json()
        result = result['result']
        st.success(f"The result is: {result}")

    ############## POST REQUEST #################
    if st.button("Predict with POST"):
        url = url_API
        response =requests.post(url,
                                headers={"Content-Type": "application/json"},
                                data = json.dumps({"num1":num1x,"num2":num2x})
                                )
        result =response.json()
        result = result['result']
        st.success(f"The result is: {result}")


if __name__ == '__main__':
    main()