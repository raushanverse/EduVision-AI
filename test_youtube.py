from utils.youtube_fetcher import fetch_youtube_videos

videos = fetch_youtube_videos("Introduction to Machine Learning")

for title, url in videos:
    print("🎬", title)
    print("🔗", url)
    print()
