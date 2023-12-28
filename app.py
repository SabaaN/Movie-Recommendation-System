import pickle
import streamlit as st
import requests

st.markdown(
    """
    <style>
    .two-line-text {
        overflow-wrap: anywhere;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        max-height: 3.6em;
        padding-bottom: 34px;
        }

    </style>
    """,
    unsafe_allow_html=True
)


def fetch_poster(id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similar[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:7]:
        # fetch the movie poster
        id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender')
movies = pickle.load(open('movie_recs.pkl','rb'))
similar = pickle.load(open('similar.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Search Here",
    movie_list
)

if st.button('View Recommendation', ):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5, col6 = st.columns(6)




    with col1:
        st.markdown('<p class="two-line-text">{}</p>'.format(recommended_movie_names[0]), unsafe_allow_html=True)
        st.image(recommended_movie_posters[0])
    with col2:
        st.markdown('<p class="two-line-text">{}</p>'.format(recommended_movie_names[1]), unsafe_allow_html=True)
        st.image(recommended_movie_posters[1])

    with col3:
        st.markdown('<p class="two-line-text">{}</p>'.format(recommended_movie_names[2]), unsafe_allow_html=True)
        st.image(recommended_movie_posters[2])
    with col4:
        st.markdown('<p class="two-line-text">{}</p>'.format(recommended_movie_names[3]), unsafe_allow_html=True)
        st.image(recommended_movie_posters[3])
    with col5:
        st.markdown('<p class="two-line-text">{}</p>'.format(recommended_movie_names[4]), unsafe_allow_html=True)
        st.image(recommended_movie_posters[4])
    with col6:
        st.markdown('<p class="two-line-text">{}</p>'.format(recommended_movie_names[5]), unsafe_allow_html=True)
        st.image(recommended_movie_posters[5])





