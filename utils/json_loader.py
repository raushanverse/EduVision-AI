import json

JSON_PATH = "eduvision_ai/extended_roadmaps_with_roadmap.json"


def load_courses():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("courses", {})

def save_courses(courses):
    with open(JSON_PATH, "r+", encoding="utf-8") as f:
        data = json.load(f)
        data["courses"] = courses
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
