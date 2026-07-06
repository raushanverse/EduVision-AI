# from utils.youtube_fetcher import fetch_youtube_links


# def fetch_resources_for_topic(topic):
#     # Fetch YouTube videos
#     youtube_videos = fetch_youtube_links(topic)

#     # Dummy website links (replace with real URLs if needed)
#     websites = [
#         f"https://www.geeksforgeeks.org/{topic.replace(' ', '-').lower()}/",
#         f"https://www.javatpoint.com/{topic.replace(' ', '-').lower()}"
#     ]

#     return {
#         "youtube": youtube_videos,
#         "websites": websites
#     }


import json
import os

COURSE_FILE = "extended_roadmaps_with_roadmap.json"

def load_courses():
    if os.path.exists(COURSE_FILE):
        with open(COURSE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def get_resources(course_name, all_courses=None):
    """
    Returns free and paid resources for a given course from the JSON data.
    """
    if all_courses is None:
        all_courses = load_courses()

    course_data = all_courses.get(course_name)
    if course_data:
        free_res = course_data.get("free_resources", [])
        paid_res = course_data.get("paid_resources", [])
        return free_res, paid_res
    return [], []

