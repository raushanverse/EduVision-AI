import os

file_path = os.path.abspath("extended_roadmaps.json")

if os.path.exists(file_path):
    print("✅ File mil gaya:", file_path)
else:
    print("❌ File nahi mila:", file_path)
