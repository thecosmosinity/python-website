from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="About Me!", page_icon=":tada:", layout="wide")

## Load Assets

def load(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

## Assets 
pookie = load("https://lottie.host/09b51c0e-7a6d-4533-9741-39a65bd39252/9RbLAiC8sM.json")
img_veteran = Image.open("images/roblox-badge-veteran.png")
cat_pookie = Image.open("images/cat-pfp-black.jpg")

# Use Local CSS code
def css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
css("style/style.css")


## Header Section

with st.container():
    st.subheader("Hi! I am cosmosinity! :wave:")
    st.title("Your average programmer, I like to mess around with tech.")
    st.write("I love the colour white, I also like to code and use python to make some cool stuff!")
    st.write("[Redirects >](https://bento.me/cosmosinity)")

    st.image(img_veteran)
    st.write("learning python for a year :3")

## wadoido

with st.container():
    st.write("---")
    left, right = st.columns(2)
    with left:
        st.header("What I do")
        st.write("##")
        st.write('''

        Yo! I'm cosmosinity, I make content on YouTube and I love to play video games.

        I-

        - Mess around with tech every once in a while.
        - Emulate older tech.
        - Try out older unreleased software.
        - Play with code!
        - I also like to troll people :)        

        ''')
        st.write("[Another cool website!](https://oguser.xyz/redirect)")
    with right:
        st_lottie(pookie, height=500, key = "pookie :3")


## My Projects

# Base
with st.container():
    st.write("---")
    st.header("My Projects!")
    st.write("##")
    image, text = st.columns((1, 2))

    with image:
        st.image(cat_pookie)
    with text:
        st.subheader("The Ultimate Gaming PC!")
        st.write('''
        19-04-2024, Friday
                 
        This was by far, my hardest project. After all, i only had scrap parts ;-;.
        This project was made ENTIRELY by scrap laptops.
                 
        One day, I was bored, and I thought, 'why don't i make a gaming laptop, it can't be that hard, right?'
        I took out 3 old laptops, and selected an HP ProBook 6460b as my base.
        I also had an ancient Toshiba Portege and a newer ProBook.
                 
        The reason I took the older model was because the new ProBook opens from the keyboard,
        and, the 6460b had a faster CPU and more RAM. I decided to put an SSD in and slotted in 8 gigs of ram.
        I installed Windows 10 and currently have the bare minimum drivers... I have more but there were hardly 3 installed...
        
        Soon, when I feel like it, I'll run benchmarks and install games, but till then,
        we won't have any updates.
                 
        Expect an update by late April, peace!

        ''')

## Contact

with st.container():
    st.write("---")
    st.header("Get in Touch! :tada:")
    st.write("##")

    ## Docs at https://formsubmit.co/ !!! CHANGE EMAIL !!!

    contactform = """
    <form action="https://formsubmit.co/cosmosinity@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder='your name'required>
        <input type="email" name="email" placeholder='your email' required>
        <textarea name="message" placeholder="your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
"""

    left1, right1 = st.columns(2)
    with left1:
        st.markdown(contactform, unsafe_allow_html=True)
    with right1:
        st.empty()
    