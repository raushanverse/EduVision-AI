def get_course_category(course_name: str) -> str:
    course_name = course_name.lower()
    if any(word in course_name for word in ["data", "ai", "software", "programming", "machine learning", "computer"]):
        return "Technical"
    elif any(word in course_name for word in ["medicine", "nursing", "pharmacy", "health", "medical", "biology"]):
        return "Medical"
    elif any(word in course_name for word in ["mba", "business", "management", "finance", "marketing"]):
        return "Management"
    else:
        return "Arts & Humanities"
