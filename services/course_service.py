"""
Course service for handling course recommendations and related operations.
"""

from typing import Dict, List, Tuple
import streamlit as st
from utils.course_recommender import openrouter_course_recommendation
from utils.helpers import get_course_category


class CourseService:
    """Service class for handling course-related operations."""
    
    def __init__(self):
        """Initialize CourseService."""
        pass
    
    @st.cache_data(ttl=3600)  # Cache for 1 hour
    def get_course_recommendations(
        _self, 
        interest: str, 
        goal: str, 
        marks: str
    ) -> Tuple[bool, str, List[str]]:
        """
        Get course recommendations based on user inputs.
        
        Args:
            interest: User's area of interest
            goal: User's career goal
            marks: User's 12th marks percentage
            
        Returns:
            Tuple[bool, str, List[str]]: (success_status, message, courses_list)
        """
        try:
            # Validate inputs
            if not _self._validate_user_inputs(interest, goal, marks):
                return False, "Please fill all fields with valid data.", []
            
            # Get course recommendations from API
            courses_text = openrouter_course_recommendation(interest, goal, marks)
            
            # Parse courses from response
            courses_list = [
                c.strip() for c in courses_text.split("\n") if c.strip()
            ]
            
            if not courses_list:
                return False, "No courses found. Please try again.", []
            
            return True, "Courses retrieved successfully", courses_list
            
        except Exception as e:
            error_msg = f"Error fetching course recommendations: {str(e)}"
            st.error(error_msg)
            return False, error_msg, []
    
    def get_course_category(self, course_name: str) -> str:
        """
        Get the category for a given course name.
        
        Args:
            course_name: Name of the course
            
        Returns:
            str: Category of the course
        """
        try:
            return get_course_category(course_name)
        except Exception as e:
            st.error(f"Error determining course category: {str(e)}")
            return "General"
    
    def get_recommended_websites(
        self, 
        course_name: str, 
        websites_data: Dict
    ) -> List[str]:
        """
        Get recommended websites for a course category.
        
        Args:
            course_name: Name of the course
            websites_data: Dictionary containing website data by category
            
        Returns:
            List[str]: List of recommended websites
        """
        try:
            category = self.get_course_category(course_name)
            websites = websites_data.get(category, [])
            return websites
        except Exception as e:
            st.error(f"Error getting recommended websites: {str(e)}")
            return []
    
    def _validate_user_inputs(self, interest: str, goal: str, marks: str) -> bool:
        """
        Validate user input fields.
        
        Args:
            interest: User's area of interest
            goal: User's career goal
            marks: User's 12th marks percentage
            
        Returns:
            bool: True if all inputs are valid, False otherwise
        """
        try:
            # Check if all fields are filled
            if not interest.strip() or not goal.strip() or not marks.strip():
                return False
            
            # Validate marks is a number
            try:
                marks_float = float(marks)
                if marks_float < 0 or marks_float > 100:
                    return False
            except ValueError:
                return False
            
            return True
            
        except Exception as e:
            st.error(f"Input validation error: {str(e)}")
            return False
    
    def format_course_display(self, courses: List[str]) -> List[str]:
        """
        Format course names for display.
        
        Args:
            courses: List of course names
            
        Returns:
            List[str]: Formatted course names
        """
        try:
            return [f"🎓 {course}" for course in courses]
        except Exception as e:
            st.error(f"Error formatting courses: {str(e)}")
            return courses
