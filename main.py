from pytube import YouTube
import ffmpeg

print("YTB Video Link: ",end="")
uservideochoice = input()
yt = YouTube(uservideochoice)
videos = yt.streams.filter(only_audio=True, mime_type="audio/webm").order_by('abr').desc().first()
title = yt.title
print(f"Downlaod Started For Video Titled: {title}")
print("---Downloading Audio File---")
videos.download(r"C:\Users\Jainam\Desktop\Audio")
videos = yt.streams.order_by('resolution').desc().first()
print("---Downloading Video File---")
videos.download(r"C:\Users\Jainam\Desktop\Video")
print("Audio Video Download Complete")
print("Merging Downloaded Audio and Video Files")
input_video = ffmpeg.input(fr"C:\Users\Jainam\Desktop\Video\{title}.webm")
added_audio = ffmpeg.input(fr"C:\Users\Jainam\Desktop\Audio\{title}.webm").audio.filter('adelay', "1500|1500")

merged_audio = ffmpeg.filter([input_video.audio, added_audio], 'amix')

(
    ffmpeg
    .concat(input_video, merged_audio, v=1, a=1)
    .output(r"C:\Users\Jainam\Desktop\mix_delayed_audio.mp4")
    .run(overwrite_output=True)
)