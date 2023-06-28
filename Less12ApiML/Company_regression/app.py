import streamlit as st
import requests
import json

def main():
    st.title("API Frontend - POST-GET Debugger")
    url_API =st.text_input("inserisci url dell'api","http://localhost:8000/predict")
    tv = st.number_input("Inserisci tv")
    radio = st.number_input("Inserisci radio")
    newspaper = st.number_input("Inserisci newspaper")

    ############## GET REQUEST #################
    if st.button("Predict with GET"):
        url = url_API
        url2 = f"?tv={tv}&radio={radio}&newspaper={newspaper}"
        link = url+url2
        st.write('"{}"'.format(link))
        response = requests.get(link)
        result =response.json()
        st.success(f"The result is: {result}")

    ############## POST REQUEST #################
    if st.button("Predict with POST"):
        url = url_API
        response =requests.post(url,
                                headers={"Content-Type": "application/json"},
                                data = json.dumps({
                                                   "tv":tv,
                                                   "radio":radio,
                                                   "newspaper":newspaper,
                                                   })
                                )
        result =response.json()
        st.success(f"The result is: {result}")

if __name__ == '__main__':
    main()