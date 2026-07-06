from utils.roadmap_generator import get_course_roadmap

course = "B.Tech in Computer Science"  # replace with your real course name
roadmap = get_course_roadmap(course)
print("FOUND ✅" if roadmap else "NOT FOUND ❌")
