import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Home - zhaelly", page_icon="headphone", layout="centered")


def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
             return None
        return r.json()


gif = "https://lottie.host/a11fff5d-541f-4c72-82e4-85391ae4b66a/67Bu1rWcS9.json"


with st.container():
    st.subheader("Hi, I am Leonazil C. Bagabaldo :wave:")
    st.header("17-year old Music Producer")
    st.write("A young music producer from the Philippines creating energetic EDM tracks with a fun vibe. Skilled in guitar, piano, drums, and songwriting. Shares original music on TikTok and Spotify.")
    st.write("[Know Me Personally >](https://web.facebook.com/zhaellyzhae)")

with st.container():
    st.write("---")
    
    col1, col2, col3, col4 = st.columns([1, 4, 4, 1])
    with col3:
        st.header("🎵 Things I Do")
        st.write(
            """
            - Songwriting 

            - Beat production (EDM, pop)

            - Vocal demos & jingles

            - FL Studio templates & sound packs

            """
        )

    with col2:
         st.lottie(gif, height=350, key="music")

with st.container():
    st.write("---")
    st.header("My Projects")

    # First Project
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("images/project christmas.jpg", use_container_width=True)

    with col2:
        st.markdown("### [HOW I PRODUCED A CHRISTMAS TRACK IN 2024](https://www.youtube.com/watch?v=KbLGTxJFpaY)")
        st.subheader("Made a Christmas Track with Just Passion and Limited Resources")
        st.write("In 2024, I produced a full Christmas track despite being a student with a tight budget, limited gear, and barely any time. With nothing but my determination, creativity, and a love for music, I made it happen—one beat at a time.")

    st.write("###")

    # Second Project
    col3, col4 = st.columns([1, 2])

    with col3:
        st.image("images/project prog.png", use_container_width=True)

    with col4:
        st.markdown("### [How I Made A Progressive House Track Like Martin Garrix](https://www.youtube.com/watch?v=-0MqhnY5VgA&t=29s)")
        st.subheader("Made a Progressive House Track Like Martin Garrix with Just My Laptop and Passion")
        st.write("As a 17-year-old student with limited gear and weekend studio time, I set out to produce a progressive house track inspired by Martin Garrix. With only FL Studio, my electric guitar, and a lot of late nights, I brought my vision to life—proving that big sound doesn’t need a big budget.")









with st.container():
    st.write("---")
    st.header("Example Work:")

    # First Example: Spotify release
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("images/spotify logo.png", use_container_width=True)
    with col2:
        st.subheader("🎵 Stream")
        st.markdown('[**"AGAIN" by zhaelly**](https://open.spotify.com/track/6bxmPoPqjkPLzxalB2l8QG?si=238440af124c43b8)')

    st.write("##")

    # Second Example: Christmas Song
    col3, col4 = st.columns([1, 3])
    with col3:
        st.image("images/song logo.png", use_container_width=True)
    with col4:
        st.subheader("[Christmas Song](https://web.facebook.com/100068574985087/videos/pcb.901173735511784/1089267532979390)")

    st.write("##")

    # Third Example: G10 Farewell Song
    col5, col6 = st.columns([1, 3])
    with col5:
        st.image("images/song logo.png", use_container_width=True)
    with col6:
        st.subheader("[G10 Farewell Song](https://youtu.be/fSJmLsSLIF0?si=7LQ2jPjxHnqbw5Y3)")

