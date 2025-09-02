from pydub import AudioSegment
import moviepy.editor as mp

def make_vixapixa_layered(songs, output="vixapixa_mix.mp3"):
    if not songs:
        return

    # Load first track as base
    base = AudioSegment.from_file(songs[0])
    
    # Mix all others on top
    for s in songs[1:]:
        track = AudioSegment.from_file(s)
        base = base.overlay(track)

    # Export final mix
    base.export(output, format="mp3")
    return output

def make_vixapixa_video(audio_file, video_file="vixapixa_video.mp4"):
    # Create waveform-style video with just audio + color bg
    audio = mp.AudioFileClip(audio_file)
    duration = audio.duration

    # Simple blank background
    clip = mp.ColorClip(size=(720, 480), color=(30,30,30), duration=duration)
    clip = clip.set_audio(audio)

    clip.write_videofile(video_file, fps=24)
    return video_file
