"""
UI service for handling UI-related operations and state management.
"""

from typing import Dict, List, Optional, Tuple
import streamlit as st


class UIService:
    """Service class for handling UI-related operations."""
    
    def __init__(self):
        """Initialize UIService."""
        pass
    
    def initialize_session_state(self, default_values: Dict) -> None:
        """
        Initialize session state variables with default values.
        
        Args:
            default_values: Dictionary of key-value pairs for session state
        """
        try:
            for key, default_value in default_values.items():
                if key not in st.session_state:
                    st.session_state[key] = default_value
        except Exception as e:
            st.error(f"Error initializing session state: {str(e)}")
    
    def get_session_value(self, key: str, default_value=None):
        """
        Get a value from session state.
        
        Args:
            key: Session state key
            default_value: Default value if key doesn't exist
            
        Returns:
            Value from session state or default value
        """
        try:
            return st.session_state.get(key, default_value)
        except Exception as e:
            st.error(f"Error getting session value: {str(e)}")
            return default_value
    
    def set_session_value(self, key: str, value) -> bool:
        """
        Set a value in session state.
        
        Args:
            key: Session state key
            value: Value to set
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            st.session_state[key] = value
            return True
        except Exception as e:
            st.error(f"Error setting session value: {str(e)}")
            return False
    
    def clear_session_state(self, keys: List[str]) -> bool:
        """
        Clear specific keys from session state.
        
        Args:
            keys: List of keys to clear
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            for key in keys:
                if key in st.session_state:
                    del st.session_state[key]
            return True
        except Exception as e:
            st.error(f"Error clearing session state: {str(e)}")
            return False
    
    def rerun_application(self) -> None:
        """Trigger application rerun to refresh the UI."""
        try:
            st.session_state["__rerun__"] = st.session_state.get("__rerun__", 0) + 1
        except Exception as e:
            st.error(f"Error triggering rerun: {str(e)}")
    
    def format_kpi_data(
        self, 
        courses: List[str], 
        selected_course: Optional[str], 
        roadmap_steps: List[str]
    ) -> Dict:
        """
        Format data for KPI dashboard display.
        
        Args:
            courses: List of recommended courses
            selected_course: Currently selected course
            roadmap_steps: List of roadmap steps
            
        Returns:
            Dict: Formatted KPI data
        """
        try:
            return {
                "courses_count": len(courses) if courses else 0,
                "course_status": "Selected" if selected_course else "Not Selected",
                "roadmap_steps": len(roadmap_steps) if roadmap_steps else 0,
                "status_icon": "✅" if selected_course else "⏳"
            }
        except Exception as e:
            st.error(f"Error formatting KPI data: {str(e)}")
            return {
                "courses_count": 0,
                "course_status": "Error",
                "roadmap_steps": 0,
                "status_icon": "❌"
            }
    
    def validate_form_inputs(
        self, 
        interest: str, 
        goal: str, 
        marks: str
    ) -> Tuple[bool, str]:
        """
        Validate form inputs from user.
        
        Args:
            interest: User's area of interest
            goal: User's career goal
            marks: User's 12th marks percentage
            
        Returns:
            Tuple[bool, str]: (is_valid, error_message)
        """
        try:
            if not interest.strip():
                return False, "Interest field is required."
            
            if not goal.strip():
                return False, "Career goal field is required."
            
            if not marks.strip():
                return False, "Marks field is required."
            
            # Validate marks is a valid percentage
            try:
                marks_float = float(marks)
                if marks_float < 0 or marks_float > 100:
                    return False, "Marks must be between 0 and 100."
            except ValueError:
                return False, "Marks must be a valid number."
            
            return True, ""
            
        except Exception as e:
            return False, f"Validation error: {str(e)}"
    
    def create_user_inputs_dict(
        self, 
        interest: str, 
        goal: str, 
        marks: str
    ) -> Dict[str, str]:
        """
        Create a dictionary of user inputs.
        
        Args:
            interest: User's area of interest
            goal: User's career goal
            marks: User's 12th marks percentage
            
        Returns:
            Dict[str, str]: Dictionary of user inputs
        """
        try:
            return {
                "interest": interest.strip(),
                "goal": goal.strip(),
                "marks": marks.strip()
            }
        except Exception as e:
            st.error(f"Error creating user inputs: {str(e)}")
            return {}
    
    def should_show_kpi_dashboard(
        self, 
        courses: List[str], 
        selected_course: Optional[str]
    ) -> bool:
        """
        Determine if KPI dashboard should be shown.
        
        Args:
            courses: List of recommended courses
            selected_course: Currently selected course
            
        Returns:
            bool: True if KPI dashboard should be shown
        """
        try:
            return bool(courses or selected_course)
        except Exception as e:
            st.error(f"Error determining KPI display: {str(e)}")
            return False
    
    def should_show_main_content(
        self, 
        courses: List[str], 
        selected_course: Optional[str]
    ) -> bool:
        """
        Determine if main content tabs should be shown.
        
        Args:
            courses: List of recommended courses
            selected_course: Currently selected course
            
        Returns:
            bool: True if main content should be shown
        """
        try:
            return bool(courses or selected_course)
        except Exception as e:
            st.error(f"Error determining content display: {str(e)}")
            return False
