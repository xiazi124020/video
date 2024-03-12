from gtts import gTTS
from moviepy.editor import AudioFileClip, VideoFileClip, CompositeVideoClip,concatenate_audioclips

# 加载原视频，
video_clip = VideoFileClip("weixiaobao.mp4")

# 加载新的背景音乐，这里假设音乐文件名为"temp_audio_ja.mp3"
audio = video_clip.audio

audio.write_audiofile("weixiaobao.mp3")  
