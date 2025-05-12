import streamlit as st



with st.container():
    st.header("Released Music")

    # First Example: Spotify release
    col1, col2, col3 = st.columns([1, 2, 5])
    with col2:
        st.image("images/spotify logo.png", use_container_width=True)
    with col3:
        st.subheader("🎵 Stream")
        st.markdown('[**"AGAIN" by zhaelly**](https://open.spotify.com/track/6bxmPoPqjkPLzxalB2l8QG?si=238440af124c43b8)')
