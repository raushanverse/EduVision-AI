import json

with open("extended_roadmaps.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("🧪 Checking which courses have roadmaps:\n")
for course in data["courses"]:
    name = course.get("course_name", "Unnamed")
    if "roadmap" in course:
        print(f"✅ {name}")
    else:
        print(f"❌ {name} → No roadmap found")


# ye code check karta hy kitne course may roadmap hy ya nhi (json ke data may)