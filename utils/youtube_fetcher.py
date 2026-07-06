# import requests
# from youtubesearchpython import VideosSearch

# def fetch_piped_videos(topic, max_results=5):
#     """
#     Piped API se videos fetch kare.
#     Agar fail ho to empty list return kare.
#     """
#     search_url = f"https://pipedapi.kavin.rocks/search?q={topic}+tutorial"
#     try:
#         response = requests.get(search_url)
#         if response.status_code != 200:
#             print(f"Piped API error: Status code {response.status_code}")
#             return []
#         results = response.json()
#         videos = results.get("items", [])[:max_results]
#         video_links = [
#             {
#                 "title": video.get("title", "No title"),
#                 "url": f"https://piped.video/watch?v={video['url'].split('=')[-1]}"
#             }
#             for video in videos if video.get("url")
#         ]
#         if not video_links:
#             print("Piped API returned zero videos.")
#         return video_links
#     except Exception as e:
#         print(f"⚠️ Error fetching videos from Piped API: {e}")
#         return []

# def fetch_videos_ysp(course_name, max_results=5):
#     """
#     fallback: YouTubeSearchPython se videos fetch kare
#     """
#     try:
#         videos_search = VideosSearch(f"{course_name} tutorial", limit=max_results)
#         results = videos_search.result()
#         video_links = []
#         for video in results.get('result', []):
#             video_links.append({
#                 "title": video.get("title"),
#                 "url": video.get("link")
#             })
#         if not video_links:
#             print("YouTubeSearchPython returned zero videos.")
#         return video_links
#     except Exception as e:
#         print(f"⚠️ Error fetching videos from YouTubeSearchPython: {e}")
#         return []

# def get_course_videos(course_name, max_results=5):
#     """
#     Pehle piped se try karo, agar fail ho to YouTubeSearchPython fallback.
#     """
#     videos = fetch_piped_videos(course_name, max_results)
#     if not videos:
#         videos = fetch_videos_ysp(course_name, max_results)
#     return videos


import requests

def fetch_piped_videos(topic, max_results=5):
    """
    Piped API se videos fetch karta hai.
    Args:
        topic (str): Search query/topic.
        max_results (int): Maximum videos to fetch.
    Returns:
        List of dicts: [{"title": ..., "url": ...}, ...]
    """
    search_url = f"https://pipedapi.kavin.rocks/search?q={topic}+tutorial"
    try:
        response = requests.get(search_url)
        if response.status_code != 200:
            print(f"Piped API returned status code: {response.status_code}")
            return []
        results = response.json()
        videos = results.get("items", [])[:max_results]
        video_links = []
        for video in videos:
            video_url = video.get("url", "")
            if video_url:
                # Extract video id from URL
                video_id = video_url.split("v=")[-1]
                video_links.append({
                    "title": video.get("title", "No title"),
                    "url": f"https://piped.video/watch?v={video_id}"
                })
        if not video_links:
            print("No videos found from Piped API.")
        return video_links
    except Exception as e:
        print(f"Error fetching videos from Piped API: {e}")
        return []

def get_course_videos(course_name, max_results=5):
    # "tutorial" add karke relevant videos laate hain
    return fetch_piped_videos(course_name, max_results)
