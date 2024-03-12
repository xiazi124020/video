from moviepy.editor import *
import os

# Folder containing images and path to audio file
image_folder = 'images'
audio_file = 'weixiaobao.mp3'
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
images.sort()  # Sort the images by name

# Settings
slide_duration = 5  # seconds per image
fps = 24  # frames per second

# Create a clip for each image
clips = []
for image in images:
    img_path = os.path.join(image_folder, image)
    img_clip = ImageClip(img_path).set_duration(slide_duration).crossfadein(1).crossfadeout(1)
    clips.append(img_clip)

# Concatenate all clips
video = concatenate_videoclips(clips, method="compose")

# Add a title, intro, and outro
txt_clip_title = TextClip("Video Title", fontsize=70, color='white').set_position('center').set_duration(3)
txt_clip_intro = TextClip("Video Introduction", fontsize=50, color='white').set_position('center').set_duration(3)
txt_clip_outro = TextClip("Video Conclusion", fontsize=50, color='white').set_position('center').set_duration(3)

# Putting everything together
final_video = concatenate_videoclips([txt_clip_title, txt_clip_intro, video, txt_clip_outro], method="compose")

# Add audio
audio_background = AudioFileClip(audio_file).subclip(0, final_video.duration)
final_video = final_video.set_audio(audio_background)

# Export the video
final_video.write_videofile("output.mp4", fps=fps)

