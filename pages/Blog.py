import streamlit as st

with st.container():
    col1,col2,col3, = st.columns([1,8,1])

    with col2:
        st.header("🎧 Chasing Dreams & Clicking Keys: My Journey So Far")
        st.write("**Hey there, and welcome to my little corner of the internet.**")
        st.write("I’m zhaelly — an artist, coder, dreamer, and someone who’s constantly juggling between music projects, code snippets, and late-night thoughts about the future.")
        st.write("---")

with st.container():
    col1,col2,col3 = st.columns([1,8,1])
    with col2:
        st.header("🌟 What This Blog Is About")
        st.write("This space is for documenting the wild ride I'm on — from producing music in my bedroom and releasing tracks on Spotify, to learning how to code and chasing a future I once thought was too far away. Whether I’m experimenting with FL Studio or debugging my latest website, you’ll find my journey here.")
        st.write("---")

with st.container():
    col1,col2,col3 = st.columns([1,8,1])
    with col2:
        st.header("🎵 My Passion for Music")
        st.write("Music has always been my escape. I write songs, produce beats, and post snippets online. Some tracks are raw, some are polished, but all of them are pieces of me. I want to share the ups and downs — the messy drafts, the late-night breakthroughs, and the rush of uploading a finished track.")
        st.write("---")

with st.container():
    col1,col2,col3, = st.columns([1,8,1])
    with col2:
        st.header("💻 Learning to Code")
        st.write("Alongside music, I’m diving into the world of Computer Science. At first, it was intimidating — lines of code I didn’t understand. But with time (and a bit of help from AI), I’m starting to get the hang of it. It’s empowering to build something from scratch, even if it’s just a form or a portfolio site for now.")
        st.write("---")

with st.container():
    col1,col2,col3 = st.columns([1,8,1])
    with col2:
        st.header("💭 Big Dreams, Real Talk")
        st.write("I dream of living in Manhattan, working in a studio, and giving my family the life they deserve. It sounds huge — and it is — but that doesn’t mean it’s impossible. Here, I’ll share real thoughts: my doubts, my progress, and maybe even a few setbacks. No filters, just honesty.")
        st.write("---")

with st.container():
    col1, col2, col3 = st.columns([1,8,1])
    
    with col2:
        st.write("""
If you’re on your own journey — in music, tech, or life — I hope this blog gives you something real to relate to.
Thanks for being here. Let’s keep creating, learning, and chasing what sets our souls on fire.

— *zhaelly*""")
    