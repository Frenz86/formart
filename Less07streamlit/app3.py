import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st 


df = sns.load_dataset("titanic")

fig = plt.figure(figsize=(10, 4))
sns.countplot(x="class", data=df)

st.pyplot(fig)