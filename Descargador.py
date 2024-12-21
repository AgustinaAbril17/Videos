import yt_dlp as youtube_d1
def descargar_video(url):
    yd1_opts = {
        'format': 'bestaudio',     
        'outtmpl': '%(title)s.%(ext)s',
    }  #bestvideo = video con mejor calidad, bestaudio = audio con mejor calidad, best = video y audio con mejor calidad disponible
    with youtube_d1.YoutubeDL(yd1_opts) as yd1:
        yd1.download([url])

url = "https://www.youtube.com/watch?v=o6wtDPVkKqI"
descargar_video(url)