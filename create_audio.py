from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

text = f"""
在阳丘县的一个平凡午后，李慕，在厨房前沉思。自从三天前来到这个世界，依靠借来的钱维生，他开始融入这个既熟悉又陌生的地方，一个深受古代华夏文化影响的世界。这里有道家、佛门，尽管与他所知稍有不同，但思想和教义却无异。接受了新身份的他，开始思考未来，不愿平庸一生，却也面临着现实的困境和挑战。一次偶遇，让他认识了李清，一位高冷的女修行者，她的简单帮助让李慕感受到了温暖。但随后，一位自称能预见未来的老道士的预言，暗示了李慕潜在的危机，这让他不禁反思自己的处境与未来。
"""
tts = gTTS(text=text, lang='zh-cn')
tts.save("output.mp3")

# 加载MP3文件
audio = AudioSegment.from_mp3("output.mp3")

# 改变语速，这里将速度提高为原来的1.3倍
# 注意：100代表原速，小于100减速，大于100加速
audio_fast = audio.speedup(playback_speed=1.3)

# 保存加速后的音频文件
audio_fast.export("output_fast.mp3", format="mp3")

# 如果你想直接播放看看效果
play(audio_fast)
