"""
Admin service for handling authentication and admin panel operations.
"""

import json
from typing import Dict, List, Tuple, Optional
import streamlit as st


class AdminService:
    """Service class for handling admin authentication and operations."""
    
    def __init__(self, username: str, password: str):
        """
        Initialize AdminService with admin credentials.
        
        Args:
            username: Admin username for authentication
            password: Admin password for authentication
        """
        self.username = username
        self.password = password
        self._is_authenticated = False
    
    def authenticate(self, input_username: str, input_password: str) -> bool:
        """
        Authenticate admin user with provided credentials.
        
        Args:
            input_username: Username input from user
            input_password: Password input from user
            
        Returns:
            bool: True if authentication successful, False otherwise
        """
        try:
            if input_username == self.username and input_password == input_password:
                self._is_authenticated = True
                return True
            return False
        except Exception as e:
            st.error(f"Authentication error: {str(e)}")
            return False
    
    def is_authenticated(self) -> bool:
        """
        Check if admin is currently authenticated.
        
        Returns:
            bool: True if authenticated, False otherwise
        """
        return self._is_authenticated
    
    def logout(self) -> None:
        """Logout admin user and clear authentication state."""
        self._is_authenticated = False
    
    def update_recommended_websites(self, websites_json: str) -> Tuple[bool, str]:
        """
        Update recommended websites from JSON input.
        
        Args:
            websites_json: JSON string containing website data
            
        Returns:
            Tuple[bool, str]: (success_status, message)
        """
        try:
            websites_obj = json.loads(websites_json)
            return True, "Websites updated successfully"
        except json.JSONDecodeError as e:
            return False, f"Invalid JSON format: {str(e)}"
        except Exception as e:
            return False, f"Error updating websites: {str(e)}"
    
    def update_recommended_courses(self, courses_str: str) -> Tuple[bool, str, List[str]]:
        """
        Update recommended courses from comma-separated string.
        
        Args:
            courses_str: Comma-separated string of course names
            
        Returns:
            Tuple[bool, str, List[str]]: (success_status, message, courses_list)
        """
        try:
            courses_list = [c.strip() for c in courses_str.split(",") if c.strip()]
            return True, "Courses updated successfully", courses_list
        except Exception as e:
            return False, f"Error updating courses: {str(e)}", []
    
    def save_admin_changes(
        self, 
        websites_json: str, 
        courses_str: str
    ) -> Tuple[bool, str, Optional[Dict], Optional[List[str]]]:
        """
        Save both websites and courses changes.
        
        Args:
            websites_json: JSON string containing website data
            courses_str: Comma-separated string of course names
            
        Returns:
            Tuple[bool, str, Optional[Dict], Optional[List[str]]]: 
            (success_status, message, websites_obj, courses_list)
        """
        try:
            # Update websites
            websites_success, websites_msg = self.update_recommended_websites(websites_json)
            if not websites_success:
                return False, websites_msg, None, None
            
            # Update courses
            courses_success, courses_msg, courses_list = self.update_recommended_courses(courses_str)
            if not courses_success:
                return False, courses_msg, None, None
            
            # Parse websites object for return
            websites_obj = json.loads(websites_json)
            
            return True, "Admin data updated successfully", websites_obj, courses_list
            
        except Exception as e:
            return False, f"Error saving admin changes: {str(e)}", None, None
