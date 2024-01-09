import streamlit as st
import pickle
import pandas as pd
import requests
import sklearn

st.set_page_config(
    page_title='CinePhilia', page_icon='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgwyGJxccQ8JdQZ4biEZIozjHRnfINIKX9aQ&usqp=CAU',
    layout="centered", 
    initial_sidebar_state="collapsed")


st.markdown("<h1 style='text-align: center; color: #00FFF4;'>CinePhilia</h1>", unsafe_allow_html=True)  # using as title
st.markdown("<h6 style='text-align: center; color: #00FFF4;'>For the Cinephiles, by the Cinephiles!</h6>", unsafe_allow_html=True)


# setting the background image  
def set_bg_hack_url():
 
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://images.unsplash.com/photo-1606870655612-8eacd813984d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8ZmlsbSUyMGFlc3RoZXRpY3xlbnwwfHwwfHx8MA%3D%3D");
             background-size: fit
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()


# remove the menu and footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



# remove the header
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)




df_pickle=pickle.load(open('df_dataframe_dict.pkl',mode='rb'))  # the dataframe
df_dataframe=pd.DataFrame(df_pickle)

similarity=pickle.load(open('similarity.pkl',mode='rb')) # the cosine similarity dataframe

def get_poster(movie_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=6f2bf08da475f307c72d4a0d0ccc286f')
    data=response.json()
    return "https://image.tmdb.org/t/p/w185/"+data['poster_path']



def recommend(movie_title):
    movie_title=movie_title.lower()
    index=df_dataframe[df_dataframe['title']==movie_title].index[0]
    distances=similarity[index]
    movie_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[:15]
    
    recommendations=[]
    recommended_poster=[]
    for i in movie_list: 
        movieID=df_dataframe.iloc[i[0]].id
        recommended_poster.append(get_poster(movieID))
        recommendations.append(df_dataframe.iloc[i[0]].title.title())
        
    return recommendations, recommended_poster



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    


local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')


selected = st.text_input("", "Search...")
button_clicked = st.button("Get recommendations")


st.header('')


if button_clicked:
    try:
        recommendations, poster=recommend(selected)

        col1, col2, col3, col4, col5 = st.columns(5)
        col6, col7, col8, col9, col10 = st.columns(5)
        col11, col12, col13, col14, col15 = st.columns(5)

        with col1:
            st.image(poster[0])
            st.write(recommendations[0])


        with col2:
            st.image(poster[1])
            st.write(recommendations[1])

        with col3:
            st.image(poster[2])
            st.write(recommendations[2])

        with col4:
            st.image(poster[3])
            st.write(recommendations[3])

        with col5:
            st.image(poster[4])
            st.write(recommendations[4])

        with col6:
            st.image(poster[5])
            st.write(recommendations[5])

        with col7:
            st.image(poster[6])
            st.write(recommendations[6])

        with col8:
            st.image(poster[7])
            st.write(recommendations[7])

        with col9:
            st.image(poster[8])
            st.write(recommendations[8])

        with col10:
            st.image(poster[9])
            st.write(recommendations[9])


        st.markdown("<h6 style='text-align: center; color: #00FFF7;'>AND YEAH, THANKS FOR USING.</h6>", unsafe_allow_html=True)
    
    except Exception as e:
        print('')
        st.markdown("<h4 style='text-align: center; color: #00FFF7;'>Oops no movie found!</h4>", unsafe_allow_html=True)
