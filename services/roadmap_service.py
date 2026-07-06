"""
Roadmap service for handling learning roadmap generation and operations.
"""

from io import BytesIO
from typing import List, Tuple, Optional
import streamlit as st
from utils.roadmap_generator import openrouter_roadmap
from utils.pdf_generator import generate_pdf


class RoadmapService:
    """Service class for handling roadmap-related operations."""
    
    def __init__(self):
        """Initialize RoadmapService."""
        pass
    
    @st.cache_data(ttl=1800)  # Cache for 30 minutes
    def generate_roadmap(_self, course_name: str) -> Tuple[bool, str, List[str]]:
        """
        Generate a learning roadmap for a given course.
        
        Args:
            course_name: Name of the course for roadmap generation
            
        Returns:
            Tuple[bool, str, List[str]]: (success_status, message, roadmap_steps)
        """
        try:
            # Validate course name
            if not _self._validate_course_name(course_name):
                return False, "Invalid course name provided.", []
            
            # Generate roadmap from API
            roadmap_text = openrouter_roadmap(course_name)
            
            # Check for API errors
            if roadmap_text.startswith("Error fetching roadmap"):
                return False, roadmap_text, []
            
            # Parse roadmap steps
            roadmap_steps = [
                line.strip("-•. ") for line in roadmap_text.split("\n") if line.strip()
            ]
            
            if not roadmap_steps:
                return False, "No roadmap steps found for this course.", []
            
            return True, "Roadmap generated successfully", roadmap_steps
            
        except Exception as e:
            error_msg = f"Error generating roadmap: {str(e)}"
            st.error(error_msg)
            return False, error_msg, []
    
    def generate_pdf_roadmap(
        self, 
        course_name: str, 
        roadmap_steps: List[str], 
        websites: List[str]
    ) -> Tuple[bool, str, Optional[BytesIO]]:
        """
        Generate a PDF roadmap for download.
        
        Args:
            course_name: Name of the course
            roadmap_steps: List of roadmap steps
            websites: List of recommended websites
            
        Returns:
            Tuple[bool, str, Optional[BytesIO]]: (success_status, message, pdf_buffer)
        """
        try:
            # Validate inputs
            if not self._validate_pdf_inputs(course_name, roadmap_steps):
                return False, "Invalid inputs for PDF generation.", None
            
            # Generate PDF
            pdf_buffer = generate_pdf(course_name, roadmap_steps, websites)

            if not pdf_buffer:
                return False, "Failed to generate PDF.", None

            return True, "PDF generated successfully", pdf_buffer
            
        except Exception as e:
            error_msg = f"Error generating PDF: {str(e)}"
            st.error(error_msg)
            return False, error_msg, None
    
    def format_roadmap_steps(self, roadmap_steps: List[str]) -> List[str]:
        """
        Format roadmap steps for display.
        
        Args:
            roadmap_steps: List of roadmap steps
            
        Returns:
            List[str]: Formatted roadmap steps
        """
        try:
            if not roadmap_steps:
                return []
            
            # Clean and format each step
            formatted_steps = []
            for step in roadmap_steps:
                # Remove any extra whitespace and special characters
                cleaned_step = step.strip()
                if cleaned_step:
                    formatted_steps.append(cleaned_step)
            
            return formatted_steps
            
        except Exception as e:
            st.error(f"Error formatting roadmap steps: {str(e)}")
            return roadmap_steps
    
    def get_roadmap_summary(self, roadmap_steps: List[str]) -> str:
        """
        Get a summary of the roadmap.
        
        Args:
            roadmap_steps: List of roadmap steps
            
        Returns:
            str: Summary of the roadmap
        """
        try:
            if not roadmap_steps:
                return "No roadmap available."
            
            step_count = len(roadmap_steps)
            return f"Roadmap contains {step_count} learning steps."
            
        except Exception as e:
            st.error(f"Error generating roadmap summary: {str(e)}")
            return "Roadmap summary unavailable."
    
    def _validate_course_name(self, course_name: str) -> bool:
        """
        Validate course name input.
        
        Args:
            course_name: Name of the course to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        try:
            if not course_name or not isinstance(course_name, str):
                return False
            
            if len(course_name.strip()) < 3:
                return False
            
            return True
            
        except Exception as e:
            st.error(f"Course name validation error: {str(e)}")
            return False
    
    def _validate_pdf_inputs(
        self, 
        course_name: str, 
        roadmap_steps: List[str]
    ) -> bool:
        """
        Validate inputs for PDF generation.
        
        Args:
            course_name: Name of the course
            roadmap_steps: List of roadmap steps
            
        Returns:
            bool: True if valid, False otherwise
        """
        try:
            if not course_name or not roadmap_steps:
                return False
            
            if not isinstance(roadmap_steps, list) or len(roadmap_steps) == 0:
                return False
            
            return True
            
        except Exception as e:
            st.error(f"PDF input validation error: {str(e)}")
            return False
