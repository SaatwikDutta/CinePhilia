import streamlit as st
import base64


tab1, tab2= st.tabs(["Github", 'LinkedIn'])

with tab1:
   st.subheader('https://github.com/SaatwikDutta')
   st.image('https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png', width=350)


with tab2:
   st.subheader('https://www.linkedin.com/in/saatwik-dutta-6271b31b4/')
   st.image('https://www.freeiconspng.com/thumbs/linkedin-logo-png/linkedin-logo-3.png', width=350)

# remove the menu and footer
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



# # remove the header
# hide_decoration_bar_style = '''
#     <style>
#         header {visibility: hidden;}
#     </style>
# '''
# st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
