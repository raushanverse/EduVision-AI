import os

for root, dirs, files in os.walk(".", topdown=True):
    for name in files:
        if "roadmap" in name.lower():
            print(os.path.join(root, name))
