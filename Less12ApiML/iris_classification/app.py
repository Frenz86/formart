import streamlit as st
import requests
import json

def main():
    st.title("API Frontend - POST-GET Debugger")
    url_API =st.text_input("inserisci url dell'api","http://localhost:8000/predict2")
    sepal_length = st.number_input("Inserisci sepal_len",0,10,3)
    sepal_width = st.number_input("Inserisci sepal_wid",0,10,3)
    petal_length = st.number_input("Inserisci petal_len",0,10,3)
    petal_width = st.number_input("Inserisci petal_wid",0,10,3)

    ############## GET REQUEST #################
    if st.button("Predict with GET"):
        url = url_API
        url2 = f"sepal_length={sepal_length}&sepal_width={sepal_width}&petal_length={petal_length}&petal_width={petal_width}"
        link = url+"?"+url2
        st.write('"{}"'.format(link))
        response = requests.get(link)
        result =response.json()
        st.success(f"The result is: {result}")

    ############## POST REQUEST #################
    if st.button("Predict with POST"):
        response =requests.post(url_API,
                                headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
                                data = json.dumps({
                                                    'sepal_length': sepal_length, 
                                                    'sepal_width': sepal_width, 
                                                    'petal_length': petal_length, 
                                                    'petal_width': petal_width
                                                    }),
                                )
        result =response.json()
        st.success(f"The result is: {result.upper()}")

if __name__ == '__main__':
    main()