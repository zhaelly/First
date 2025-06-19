import streamlit as st



with st.container():
    st.header("Released Music")

    # First Example: Spotify release
    col1, col2, col3 = st.columns([1, 2, 5])
    with col2:
        st.image("images/zhaelly-wish.jpg", use_container_width=True)
    with col3:
        st.subheader("🎵 Stream")
        st.markdown('[**"wish" by zhaelly**](https://push.fm/fl/yyk8rzj2)')
        
    col1, col2, col3 = st.columns([1, 2, 5])
    with col2:
        st.image("images/zhaelly-AGAIN.jpg", use_container_width=True)
    with col3:
        st.subheader("🎵 Stream")
        st.markdown('[**"AGAIN" by zhaelly**](https://push.fm/fl/Z2572Hrc)')
   
    
