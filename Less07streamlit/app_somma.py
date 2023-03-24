import streamlit as st

st.text("Ciao questo front-end funziona")


# ###################################################
# #markdown
# st.markdown('Streamlit is **_really_ cool**.')
# st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
# st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

# ###################################################
# #title
# st.title('This is a title')
# st.title('A title with _italics_ :blue[colors] and emojis :sunglasses:')

# ###################################################
# #header
# st.header('This is a header')
# st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')

# ###################################################
# #subheader
# st.subheader('This is a subheader')
# st.subheader('A subheader with _italics_ :blue[colors] and emojis :sunglasses:')

# ###################################################
# #caption
# st.caption('This is a string that explains something above.')
# st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

# ###################################################
# #code
# code = '''def hello():
#     print("Hello, Streamlit!")'''
# st.code(code, language='python')

# ###################################################
# #latex
# st.latex(r'''
#     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#     \sum_{k=0}^{n-1} ar^k =
#     a \left(\frac{1-r^{n}}{1-r}\right)
#     ''')

#######################################################

# st.title('La mia prima App in python')

# #####################################################à
# from PIL import Image

# image = Image.open('spiaggia.jpg')
# st.image(image, caption='Mare mare!!!',width=860)

# ######################################################

# # button
# if st.button('Streamlit Button', help="Click here"):
#     st.write('Hai cliccato')
 
# # check box
# st.checkbox('Check Box')
 
# # radio button
# lang = st.radio(
#     "What's your favorite programming language?",
#     ('C++', 'Python'))
# if lang == 'C++':
#     st.write('You selected C++.')
# else:
#     st.write('You selected Python')
 
# # slider
# l1 = st.slider('Please inserisci lato1 rettangolo', 0, 100, 25)
# l2 = st.slider('Please inserisci lato2 rettangolo', 0, 100, 35)

# def area(l1:float,l2:float):
#     a = l1*l2
#     return a 

# st.write("l'area rettangolo è ", area(l1,l2))
 
# # # Using object notation
# # add_selectbox = st.sidebar.radio(
# #     "Please choose an option",
# #     ("Option 1", "Option 2", "Option 3")
# # )

# ##################################################
# ############## Plot ############################
# import matplotlib.pyplot as plt 
# from numpy.random import rand

# fig = plt.figure(figsize=(18,10)) 
# plt.scatter([1,2,3,4,5],[1,2,3,4,5])
# st.pyplot(fig)

####################

# rn = st.slider('Please inserisci il numero ci punti da visualizzare', 0, 100, 88)
# x = rand(rn)
# y = rand(rn)
# fig2 = plt.figure(figsize=(18,10)) 
# plt.plot(x,y,'or')
# st.pyplot(fig2)

#####################################################

# input1 = 'customerID'
# input2 = st.text_input("Please write gender",'Female')
# input3 = st.text_input("Please write SeniorCitizen",0)
# input4 = st.text_input("Please write Partner","Yes")
# input5 = st.text_input("Please write Dependents","No")


# ##############################################
# ### Audio ###################################
# audio_file = open("snoop.mp3", "rb")
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format="audio/mp3")

# #############################################
# ###### CSS BACKGROUND #######################
# def add_bg_from_url():
#     st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
#              background-attachment: fixed;
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )

# add_bg_from_url() 

# #####################
# ### Footer #########
# def show_footer():
#     st.markdown("***")
#     st.markdown(""" **Do you like this example app?** Follow me on
#                 [Linkedin](https://www.linkedin.com/in/daniele-grotti-38681146/).""")

# show_footer()