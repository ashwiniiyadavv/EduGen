from moviepy.editor import ImageSequenceClip, AudioFileClip

def merge_frames_and_audio(frame_dir, audio_path, output_path="final.mp4", fps=30):
    clip = ImageSequenceClip(frame_dir, fps=fps)
    audio = AudioFileClip(audio_path)
    clip = clip.set_audio(audio)
    clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
    return output_path
