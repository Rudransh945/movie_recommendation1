import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_posters(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=a57cb3489e4ef97371d5d373e4f301aa". format(movie_id)

    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters =[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_posters(movie_id))
    return recommended_movies, recommended_movies_posters


movie_dict= pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('models/similarity.pkl', 'rb'))

st.title('Movie Recommendation')
Selected_movie_name= st.selectbox('how would you like to cotacted?',movies['title'].values)
#jf

if st.button("Recommend"):
    names,posters =recommend(Selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])