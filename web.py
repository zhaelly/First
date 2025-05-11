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
    
    left_column, right_column = st.columns(2)
    with right_column:
        st.header("Services I Offer:")

        st.subheader("🎵 Music & Audio Services")
        st.write(
            """
            - Songwriting (custom & ghost)

            - Beat production (EDM, pop)

            - Vocal demos & jingles

            - FL Studio templates & sound packs

            """
        )

    with left_column:
         st.lottie(gif, height=350, key="music")

with st.container():
    st.write("---")
    st.header("My Projects")

    img, text = st.columns ((1,2))

with img:
        st.write("###")
        st.image('images/project christmas.jpg')
    
with text:
        st.header("[HOW I PRODUCED A CHRISTMAS TRACK IN 2024](https://www.youtube.com/watch?v=KbLGTxJFpaY)")
        st.subheader("Made a Christmas Track with Just Passion and Limited Resources")
        st.write("In 2024, I produced a full Christmas track despite being a student with a tight budget, limited gear, and barely any time. With nothing but my determination, creativity, and a love for music, I made it happen—one beat at a time.")
        

st.write("###")

with st.container():
    with img:
        st.write("###")
        st.write("###")
        st.write("###")
        st.write("###")
        st.write("###")
        st.image('images/project prog.png')

    with text:
        st.write("###")
        st.write("###")
        st.header("[How I Made A Progressive House Track Like Martin Garrix](https://www.youtube.com/watch?v=-0MqhnY5VgA&t=29s)")
        st.subheader("Made a Progressive House Track Like Martin Garrix with Just My Laptop and Passion")
        st.write("As a 17-year-old student with limited gear and weekend studio time, I set out to produce a progressive house track inspired by Martin Garrix. With only FL Studio, my electric guitar, and a lot of late nights, I brought my vision to life—proving that big sound doesn’t need a big budget.")













# Create a container for layout
with st.container():
    # Add a separator and a header
    st.write("---")
    st.header("Example Work:")

    # Define 4 columns for layout
    col1, col2, col3, col4 = st.columns([1, 4, 4, 1])  # Adjust column width ratio as needed
    
    # First section: Spotify logo and Stream title on the same row
    with col2:
        st.image('images/spotify logo.png', width=150)
    
    with col3:
        st.subheader("🎵 Stream")
        st.subheader('["AGAIN"](https://open.spotify.com/track/6bxmPoPqjkPLzxalB2l8QG?si=238440af124c43b8) by zhaelly')

    # Adding some spacing between sections
    st.write("##")
    st.write("##")

    # Second section: Song logo and link (Christmas song) in the same row
    with col2:
        st.write("##")
        st.image('images/song logo.png', width=150)
    
    with col3:
        st.write("##")
        st.write("##")
        st.subheader("[Christmas Song](https://web.facebook.com/100068574985087/videos/pcb.901173735511784/1089267532979390)")

    # Adding some spacing between sections
    st.write("##")
    st.write("##")

    # Third section: Another song logo and link (G10 Farewell Song) in the same row
    with col2:
        st.write("##")
        st.image('images/song logo.png', width=150)
    
    with col3:
        st.write("##")
        st.write("##")
        st.subheader("[G10 Farewell Song](https://youtu.be/fSJmLsSLIF0?si=7LQ2jPjxHnqbw5Y3)")


