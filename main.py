from gtts import gTTS
from moviepy.editor import AudioFileClip, VideoFileClip, CompositeVideoClip,concatenate_audioclips

# 定义你想要转换为语音的文本
# text = "这是我想要加到视频中的语音。"

# # 使用gTTS生成语音
# tts = gTTS(text=text, lang='zh-cn')
# tts.save("temp_audio.mp3")

# tts = gTTS(text="ここに日本語のテキストを入力してください。ここはテスト用の音を生成する。", lang='ja')
# tts.save("temp_audio_ja.mp3")

# tts = gTTS(text="Enter your English text here.", lang='en')
# tts.save("temp_audio_en.mp3")
# 加载原视频，这里假设视频文件名为"test.mp4"
video_clip = VideoFileClip("test.mp4").without_audio()  # 使用without_audio()去除原视频音轨

# 加载新的背景音乐，这里假设音乐文件名为"temp_audio_ja.mp3"
background_music = AudioFileClip("temp_audio_ja.mp3")

# 将新的背景音乐设置为视频的音轨
final_video = video_clip.set_audio(background_music)

# 导出处理后的视频到一个新文件，这里假设输出文件名为"output_video.mp4"
final_video.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac")
