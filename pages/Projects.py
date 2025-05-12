import streamlit as st




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










