import streamlit as st
st.set_page_config(page_title="Home - zhaelly", page_icon="headphone", layout="wide")


with st.container():
    col1,col2,col3 = st.columns([1,8,1])


    with col2:
        st.header("✨ Welcome to zhaelly’s Creative Hub")
        st.write("Hey there! I’m Zhaelly — a music producer, digital creator, and student with a passion for turning feelings into sound and ideas into digital art.")
        st.write("🎶 Whether you’re here to listen to my music, commission a custom song, or check out my digital products, you’re in the right place.")
        st.write("---")

        st.header("🔥 What You’ll Find Here")
        st.write("""
            -  🎧 My Music – Originals, demos, and projects I’ve produced

            - ✍️ Songwriting Commissions – Let me write your next love song or jingle

            - 📓 Blog & Journey – Thoughts, tips, and behind-the-scenes stories

            - 📬 Contact Me – Reach out for collaborations or questions""")
        st.write("---")

with st.container():
    col1, col2, col3 = st.columns([1,8,1])

    with col2:
        st.header("🌟 Featured")
        st.subheader("""*“I make music for fun, feelings, and future dreams.”*""")
        st.write("Check out my latest release on [Spotify](https://open.spotify.com/artist/22eQEvDIUVR7hD6de7wP09) or follow me on [TikTok](https://www.tiktok.com/@zhaelly.zhae) for mini music moments and creative chaos!")