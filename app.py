import streamlit as st
from vixapixa_mixer import make_vixapixa_layered, make_vixapixa_video
import os

st.set_page_config(page_title="VixaPixa Mixer", layout="wide")
st.title("🎶 VixaPixa - Layered Chorus Mixer")

st.markdown("""
Upload your songs (MP3) and VixaPixa will:
1. Extract choruses  
2. Layer vocals & instrumentals  
3. Match tempo & key  
4. Export audio + video mashup ready for YouTube/TikTok  
""")

uploaded_files = st.file_uploader(
    "Upload MP3 files",
    type=["mp3"],
    accept_multiple_files=True
)

if uploaded_files:
    os.makedirs("temp_songs", exist_ok=True)
    songs = []
    for file in uploaded_files:
        path = os.path.join("temp_songs", file.name)
        with open(path, "wb") as f:
            f.write(file.getbuffer())
        songs.append(path)

    st.success(f"✅ {len(songs)} songs uploaded successfully!")

    if st.button("🎛️ Make VixaPixa Mix"):
        with st.spinner("Processing mashup..."):
            audio_output = "vixapixa_mix.mp3"
            make_vixapixa_layered(songs, output=audio_output)

            video_output = "vixapixa_video.mp4"
            make_vixapixa_video(audio_output, video_file=video_output)

        st.success("🎉 VixaPixa mashup complete!")

        st.audio(audio_output, format="audio/mp3")
        st.video(video_output)
