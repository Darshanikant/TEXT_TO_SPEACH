
import streamlit as st
from gtts import gTTS
import os
st.markdown('''<style>
    .reportview-container {
        background-image: url('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dreamstime.com%2Fphotos-images%2Fbackground-wallpaper-hd.html&psig=AOvVaw2ADxaFr199z16Wq2OyjF1u&ust=1728104461084000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMDA-vf484gDFQAAAAAdAAAAABAE');  /* Replace with your image URL */
        background-size: cover;  /* Cover the entire background */
        background-position: center;  /* Center the background image */
        background-repeat: no-repeat;  /* Do not repeat the image */
    }
    .sidebar .sidebar-content {
        background-color: rgba(255, 255, 255, 0.7);  /* Optional: semi-transparent sidebar */
    }
    </style>'''
    ,
    unsafe_allow_html=True
)


# Streamlit app layout
st.title("Text to Speech Converter")
st.write("Enter the text you want to convert to speech:")

# Input text
input_text = st.text_area("Enter text here","")



# Button to trigger text-to-speech conversion
if st.button("Convert to Speech"):
    if input_text:
        # Convert text to speech
        tts = gTTS(text=input_text, slow=False)
        
        # Save the audio file
        tts.save("output.mp3")
        
        # Play the audio file in the Streamlit app
        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()

        # Streamlit audio player
        st.audio(audio_bytes, format="audio/mp3")
        st.success("Conversion successful!")
    else:
        st.error("Please enter some text.")
        
st.write("This is the app for converting text to speech")