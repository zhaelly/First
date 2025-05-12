import streamlit as st

with st.container():
    col1, col2, col3 = st.columns([1,8,1])

    with col2:
        st.header("Commissioned Works")
        st.write("##")

    # --- Christmas Song ---
    col1, col2, col3 = st.columns([1, 2, 5])  # Narrow margin, image, then text
    with col2:
        st.image("images/song logo.png", use_container_width=True)
    with col3:
        st.subheader("🎄 [Christmas Song](https://web.facebook.com/100068574985087/videos/pcb.901173735511784/1089267532979390)")

    st.write("##")

    # --- G10 Farewell Song ---
    col1, col2, col3 = st.columns([1, 2, 5])
    with col2:
        st.image("images/song logo.png", use_container_width=True)
    with col3:
        st.subheader("🎓 [G10 Farewell Song](https://youtu.be/fSJmLsSLIF0?si=7LQ2jPjxHnqbw5Y3)")
