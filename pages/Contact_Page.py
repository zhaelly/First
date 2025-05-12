import streamlit as st


with st.container():
    col1,col2,col3, = st.columns([1,8,1])

    with col2:
        st.title("📬 Get in Touch")
        st.write(" Got a question, a collab idea, or want to commission a custom song? I’d love to hear from you!")
        st.write("Whether you're a fellow artist, someone looking for original music, or just curious about what I do — feel free to drop a message.")
        st.write("---")

with st.container():
        col1,col2,col3, = st.columns([1,8,1])

with col2:
        st.subheader("💡 What You Can Reach Out About:")  
        st.write("""
            - 🎶 Custom Songwriting (lyrics, melodies, full demos)

            - 🛍 Digital Products & Orders

            - 🤝 Collaborations & Partnerships

            - 🧠 Questions, feedback, or just saying hi!""")
        st.write("---")

with st.container():
        col1,col2,col3, = st.columns([1,8,1])

with col2:
    st.header("📩 How to Reach Me:")
    st.subheader("Just fill out the form below with your name, email, and message. I usually reply within 1–2 days!")
    st.write("*(If you’re contacting about a commission, please include details like your project idea, deadline, and any references you have.)*")
    st.write("---")

import streamlit as st

with st.container():
    col1, col2, col3 = st.columns([1, 8, 1])

    with col2:
        contact_form = """
        <form action="https://formsubmit.co/el/vewaya" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your message here"></textarea>
            <button type="submit">Send</button>
        </form>
        """

        st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Assuming you have a local CSS file in 'style/style.css'
local_css("style/style.css")
