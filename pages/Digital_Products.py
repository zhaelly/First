import streamlit as st
from streamlit_lottie import st_lottie

gif = "https://lottie.host/a11fff5d-541f-4c72-82e4-85391ae4b66a/67Bu1rWcS9.json"





col1, col2, col3, col4 = st.columns([1, 4, 4, 1])
with col3:
        st.header("Services I Offer:")

        st.subheader("🎵 Things I Do")
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