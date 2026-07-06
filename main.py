"""
EduVision AI - Smart Career Guidance Application
"""

from email.mime import message

import streamlit as st
from typing import Dict, List
import json

# Import services
from services.admin_service import AdminService
from services.course_service import CourseService
from services.roadmap_service import RoadmapService
from services.ui_service import UIService

# Import utilities
from utils.constants import RECOMMENDED_WEBSITES

# Load custom CSS
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Page configuration
st.set_page_config(
    page_title="EduVision AI - Smart Career Guidance",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize services
admin_service = AdminService("Raushan", "admin123ve")
course_service = CourseService()
roadmap_service = RoadmapService()
ui_service = UIService()


def initialize_application() -> None:
    """Initialize the application with default session state values."""
    try:
        default_values = {
            "recommended_courses": [],
            "selected_course": None,
            "roadmap": [],
            "user_inputs": {},
            "admin_logged_in": False,
            "recommended_websites_json": RECOMMENDED_WEBSITES,
            "__rerun__": 0,
        }
        ui_service.initialize_session_state(default_values)
    except Exception as e:
        st.error(f"Error initializing application: {str(e)}")


def render_particle_background() -> None:
    """Render the animated particle background effect."""
    try:
        st.markdown("""
        <div class="particle-bg">
            <div class="particle" style="left: 10%; animation-delay: 0s;"></div>
            <div class="particle" style="left: 20%; animation-delay: 2s;"></div>
            <div class="particle" style="left: 30%; animation-delay: 4s;"></div>
            <div class="particle" style="left: 40%; animation-delay: 6s;"></div>
            <div class="particle" style="left: 50%; animation-delay: 8s;"></div>
            <div class="particle" style="left: 60%; animation-delay: 10s;"></div>
            <div class="particle" style="left: 70%; animation-delay: 12s;"></div>
            <div class="particle" style="left: 80%; animation-delay: 14s;"></div>
            <div class="particle" style="left: 90%; animation-delay: 16s;"></div>
        </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error rendering particle background: {str(e)}")


def render_header() -> None:
    """Render the main application header with animated elements."""
    try:
        st.markdown("""
        <div style="text-align: center; padding: 3rem 0; position: relative;">
            <div style="position: relative; z-index: 2;">
                <h1 style="
                    color: white; 
                    font-size: 4rem; 
                    margin-bottom: 1rem; 
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                    font-weight: 800;
                    letter-spacing: 2px;
                    animation: float 3s ease-in-out infinite;
                ">🎯 EduVision AI</h1>
                <p style="
                    color: rgba(255,255,255,0.9); 
                    font-size: 1.4rem; 
                    margin: 0;
                    text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
                    font-weight: 500;
                ">Smart Career Guidance & Learning Roadmaps</p>
                <div style="
                    margin-top: 2rem;
                    display: flex;
                    justify-content: center;
                    gap: 1rem;
                    flex-wrap: wrap;
                ">
                    <span style="
                        background: rgba(255,255,255,0.2);
                        backdrop-filter: blur(10px);
                        padding: 0.5rem 1rem;
                        border-radius: 20px;
                        color: white;
                        font-size: 0.9rem;
                        border: 1px solid rgba(255,255,255,0.3);
                    ">✨ AI-Powered</span>
                    <span style="
                        background: rgba(255,255,255,0.2);
                        backdrop-filter: blur(10px);
                        padding: 0.5rem 1rem;
                        border-radius: 20px;
                        color: white;
                        font-size: 0.9rem;
                        border: 1px solid rgba(255,255,255,0.3);
                    ">🚀 Personalized</span>
                    <span style="
                        background: rgba(255,255,255,0.2);
                        backdrop-filter: blur(10px);
                        padding: 0.5rem 1rem;
                        border-radius: 20px;
                        color: white;
                        font-size: 0.9rem;
                        border: 1px solid rgba(255,255,255,0.3);
                    ">🎓 Expert Guidance</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error rendering header: {str(e)}")


def render_kpi_dashboard() -> None:
    """Render the KPI dashboard with course metrics."""
    try:
        courses = ui_service.get_session_value("recommended_courses", [])
        selected_course = ui_service.get_session_value("selected_course")
        roadmap_steps = ui_service.get_session_value("roadmap", [])
        
        if not ui_service.should_show_kpi_dashboard(courses, selected_course):
            return
        
        kpi_data = ui_service.format_kpi_data(courses, selected_course, roadmap_steps)
        
        st.markdown('<div style="margin: 2rem 0;">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="kpi-card glow-effect">
                <div style="font-size: 2rem; margin-bottom: 1rem;">📚</div>
                <div class="kpi-value">{kpi_data['courses_count']}</div>
                <div class="kpi-label">Courses Found</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="kpi-card glow-effect">
                <div style="font-size: 2rem; margin-bottom: 1rem;">{kpi_data['status_icon']}</div>
                <div class="kpi-value">{kpi_data['course_status']}</div>
                <div class="kpi-label">Course Status</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="kpi-card glow-effect">
                <div style="font-size: 2rem; margin-bottom: 1rem;">🗺️</div>
                <div class="kpi-value">{kpi_data['roadmap_steps']}</div>
                <div class="kpi-label">Roadmap Steps</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error rendering KPI dashboard: {str(e)}")


def render_course_recommendations_tab() -> None:
    """Render the course recommendations tab."""
    try:
        courses = ui_service.get_session_value("recommended_courses", [])
        selected_course = ui_service.get_session_value("selected_course")
        
        if not courses or selected_course:
            st.info("Please enter your details in the sidebar to get course recommendations.")
            return
        
        st.markdown('<div class="custom-card glow-effect">', unsafe_allow_html=True)
        st.subheader("✅ Recommended Courses for You")
        st.markdown("Choose a course to see its detailed roadmap:")
        
        for i, course in enumerate(courses):
            if st.button(f"🎓 {course}", key=f"course_btn_{i}"):
                handle_course_selection(course)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error rendering course recommendations: {str(e)}")


def render_learning_roadmap_tab() -> None:
    """Render the learning roadmap tab."""
    try:
        selected_course = ui_service.get_session_value("selected_course")
        roadmap_steps = ui_service.get_session_value("roadmap", [])
        
        if not selected_course:
            st.info("Select a course to view its learning roadmap.")
            return
        
        st.markdown('<div class="custom-card glow-effect">', unsafe_allow_html=True)
        st.subheader(f"📍 Learning Roadmap for {selected_course}")
        
        formatted_steps = roadmap_service.format_roadmap_steps(roadmap_steps)
        
        for i, step in enumerate(formatted_steps, 1):
            st.markdown(f"""
            <div class="roadmap-step glow-effect">
                <span class="roadmap-step-number">{i}</span>
                {step}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error rendering learning roadmap: {str(e)}")


def render_learning_resources_tab() -> None:
    """Render the learning resources tab."""
    try:
        selected_course = ui_service.get_session_value("selected_course")
        websites_data = ui_service.get_session_value("recommended_websites_json", {})
        roadmap_steps = ui_service.get_session_value("roadmap", [])
        
        if not selected_course:
            st.info("Select a course to view recommended learning resources.")
            return
        
        # Get recommended websites
        websites = course_service.get_recommended_websites(selected_course, websites_data)
        
        st.markdown('<div class="custom-card glow-effect">', unsafe_allow_html=True)
        category = course_service.get_course_category(selected_course)
        st.subheader(f"🌐 Recommended Learning Resources for {category.capitalize()}")
        
        if websites:
            st.markdown("**Top websites to enhance your learning:**")
            for site in websites:
                st.markdown(f'<a href="{site}" target="_blank" class="website-link glow-effect">{site}</a>', unsafe_allow_html=True)
        else:
            st.write("No recommended websites configured for this category.")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # PDF Download Section
        render_pdf_download_section(selected_course, roadmap_steps, websites)
        
    except Exception as e:
        st.error(f"Error rendering learning resources: {str(e)}")


def render_pdf_download_section(course_name: str, roadmap_steps: List[str], websites: List[str]) -> None:
    """Render the PDF download section."""
    try:
        st.markdown('<div class="custom-card glow-effect">', unsafe_allow_html=True)
        st.subheader("📄 Download Your Roadmap")
        st.markdown("Get a printable PDF version of your learning roadmap:")
        
        if st.button("📥 Download Roadmap as PDF", key="pdf_download_btn"):
            handle_pdf_generation(course_name, roadmap_steps, websites)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error rendering PDF download section: {str(e)}")


def render_main_content_tabs() -> None:
    """Render the main content tabs."""
    try:
        courses = ui_service.get_session_value("recommended_courses", [])
        selected_course = ui_service.get_session_value("selected_course")
        
        if not ui_service.should_show_main_content(courses, selected_course):
            return
        
        st.markdown('<div style="margin: 2rem 0;">', unsafe_allow_html=True)
        tab1, tab2, tab3 = st.tabs(["📚 Course Recommendations", "🗺️ Learning Roadmap", "🌐 Learning Resources"])
        
        with tab1:
            render_course_recommendations_tab()
        
        with tab2:
            render_learning_roadmap_tab()
        
        with tab3:
            render_learning_resources_tab()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error rendering main content tabs: {str(e)}")


def render_welcome_section() -> None:
    """Render the welcome section when no courses are selected."""
    try:
        st.markdown("""
        <div class="welcome-section glow-effect">
            <div style="position: relative; z-index: 2;">
                <h2 style="
                    color: #1e293b; 
                    margin-bottom: 2rem; 
                    font-size: 2.5rem;
                    font-weight: 800;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    background-clip: text;
                ">🚀 Ready to Start Your Learning Journey?</h2>
                <p style="
                    color: #64748b; 
                    font-size: 1.3rem; 
                    margin-bottom: 3rem;
                    line-height: 1.6;
                    max-width: 600px;
                    margin-left: auto;
                    margin-right: auto;
                ">
                    Fill in your details in the sidebar to get personalized course recommendations and learning roadmaps tailored just for you.
                </p>
                <div style="
                    display: flex; 
                    justify-content: center; 
                    gap: 3rem; 
                    flex-wrap: wrap;
                    margin-top: 3rem;
                ">
                    <div style="
                        text-align: center;
                        padding: 2rem;
                        background: rgba(255,255,255,0.1);
                        backdrop-filter: blur(10px);
                        border-radius: 20px;
                        border: 1px solid rgba(255,255,255,0.2);
                        transition: all 0.3s ease;
                        min-width: 200px;
                    " onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
                        <h3 style="
                            color: #667eea; 
                            font-size: 3rem;
                            margin-bottom: 1rem;
                            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
                        ">🎯</h3>
                        <p style="
                            color: #1e293b; 
                            font-size: 1.1rem;
                            font-weight: 600;
                            margin: 0;
                        ">Personalized Recommendations</p>
                        <p style="
                            color: #64748b; 
                            font-size: 0.9rem;
                            margin: 0.5rem 0 0 0;
                        ">AI-powered course suggestions</p>
                    </div>
                    <div style="
                        text-align: center;
                        padding: 2rem;
                        background: rgba(255,255,255,0.1);
                        backdrop-filter: blur(10px);
                        border-radius: 20px;
                        border: 1px solid rgba(255,255,255,0.2);
                        transition: all 0.3s ease;
                        min-width: 200px;
                    " onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
                        <h3 style="
                            color: #06b6d4; 
                            font-size: 3rem;
                            margin-bottom: 1rem;
                            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
                        ">🗺️</h3>
                        <p style="
                            color: #1e293b; 
                            font-size: 1.1rem;
                            font-weight: 600;
                            margin: 0;
                        ">Step-by-step Roadmaps</p>
                        <p style="
                            color: #64748b; 
                            font-size: 0.9rem;
                            margin: 0.5rem 0 0 0;
                        ">Clear learning pathways</p>
                    </div>
                    <div style="
                        text-align: center;
                        padding: 2rem;
                        background: rgba(255,255,255,0.1);
                        backdrop-filter: blur(10px);
                        border-radius: 20px;
                        border: 1px solid rgba(255,255,255,0.2);
                        transition: all 0.3s ease;
                        min-width: 200px;
                    " onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
                        <h3 style="
                            color: #10b981; 
                            font-size: 3rem;
                            margin-bottom: 1rem;
                            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
                        ">🌐</h3>
                        <p style="
                            color: #1e293b; 
                            font-size: 1.1rem;
                            font-weight: 600;
                            margin: 0;
                        ">Learning Resources</p>
                        <p style="
                            color: #64748b; 
                            font-size: 0.9rem;
                            margin: 0.5rem 0 0 0;
                        ">Curated study materials</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error rendering welcome section: {str(e)}")


def render_admin_login() -> None:
    """Render the admin login form in the sidebar."""
    try:
        st.sidebar.markdown('<div class="custom-card glow-effect">', unsafe_allow_html=True)
        st.sidebar.subheader("🔐 Admin Login")
        
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        
        if st.sidebar.button("Login", key="admin_login_btn"):
            handle_admin_login(username, password)
        
        st.sidebar.markdown('</div>', unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error rendering admin login: {str(e)}")


def render_admin_panel() -> None:
    """Render the admin panel in the sidebar."""
    try:
        st.sidebar.markdown('<div class="custom-card glow-effect">', unsafe_allow_html=True)
        st.sidebar.subheader("⚙️ Admin Panel")
        
        # Get current data
        websites_data = ui_service.get_session_value("recommended_websites_json", {})
        courses = ui_service.get_session_value("recommended_courses", [])
        
        # Editable recommended websites JSON area
        current_websites_json = json.dumps(websites_data, indent=2)
        websites_json = st.sidebar.text_area(
            "Edit Recommended Websites JSON (category-wise):", 
            value=current_websites_json, 
            height=250
        )
        
        # Editable recommended courses (comma separated)
        current_courses = ", ".join(courses) if courses else ""
        courses_str = st.sidebar.text_area(
            "Edit Default Recommended Courses (comma separated):", 
            value=current_courses
        )
        
        if st.sidebar.button("Save Admin Changes", key="save_admin_btn"):
            handle_admin_save_changes(websites_json, courses_str)
        
        st.sidebar.markdown('</div>', unsafe_allow_html=True)
        
        # Logout button
        st.sidebar.markdown("---")
        if st.sidebar.button("Logout", key="logout_btn"):
            handle_admin_logout()
        
    except Exception as e:
        st.error(f"Error rendering admin panel: {str(e)}")


def render_user_input_form() -> None:
    """Render the user input form in the sidebar."""
    try:
        st.sidebar.markdown('<div class="custom-card glow-effect">', unsafe_allow_html=True)
        st.sidebar.subheader("📝 Your Information")
        
        interest = st.sidebar.text_input(
            "Your Interest", 
            key="interest_input", 
            placeholder="e.g., Technology, Medicine, Business"
        )
        goal = st.sidebar.text_input(
            "Your Career Goal", 
            key="goal_input", 
            placeholder="e.g., Software Engineer, Doctor, Manager"
        )
        marks = st.sidebar.text_input(
            "Your 12th Marks (%)", 
            value="0", 
            key="marks_input", 
            placeholder="Enter your percentage"
        )
        
        if st.sidebar.button("🚀 Get Recommended Courses", key="get_courses_btn"):
            handle_get_courses(interest, goal, marks)
        
        st.sidebar.markdown('</div>', unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error rendering user input form: {str(e)}")


def render_sidebar() -> None:
    """Render the sidebar with appropriate content based on admin state."""
    try:
        st.sidebar.title("🎯 EduVision AI")
        
        admin_logged_in = ui_service.get_session_value("admin_logged_in", False)
        
        if not admin_logged_in:
            render_admin_login()
        else:
            render_admin_panel()
        
        # Show user input fields only if admin is not logged in
        if not admin_logged_in:
            render_user_input_form()
        
    except Exception as e:
        st.error(f"Error rendering sidebar: {str(e)}")


def handle_admin_login(username: str, password: str) -> None:
    """Handle admin login authentication."""
    try:
        if admin_service.authenticate(username, password):
            ui_service.set_session_value("admin_logged_in", True)
            st.sidebar.success("Logged in as Admin!")
            ui_service.rerun_application()
        else:
            st.sidebar.error("Invalid credentials")
    except Exception as e:
        st.error(f"Error during admin login: {str(e)}")


def handle_admin_logout() -> None:
    """Handle admin logout."""
    try:
        admin_service.logout()
        ui_service.set_session_value("admin_logged_in", False)
        ui_service.rerun_application()
    except Exception as e:
        st.error(f"Error during admin logout: {str(e)}")


def handle_admin_save_changes(websites_json: str, courses_str: str) -> None:
    """Handle saving admin changes."""
    try:
        success, message, websites_obj, courses_list = admin_service.save_admin_changes(
            websites_json, courses_str
        )
        
        if success:
            ui_service.set_session_value("recommended_websites_json", websites_obj)
            ui_service.set_session_value("recommended_courses", courses_list)
            st.sidebar.success(message)
            ui_service.rerun_application()
        else:
            st.sidebar.error(message)
            
    except Exception as e:
        st.error(f"Error saving admin changes: {str(e)}")


def handle_get_courses(interest: str, goal: str, marks: str) -> None:
    """Handle getting course recommendations."""
    try:
        # Validate inputs
        is_valid, error_message = ui_service.validate_form_inputs(interest, goal, marks)
        if not is_valid:
            st.warning(error_message)
            return
        
        # Create user inputs dictionary
        user_inputs = ui_service.create_user_inputs_dict(interest, goal, marks)
        ui_service.set_session_value("user_inputs", user_inputs)
        
        # Get course recommendations
        success, message, courses = course_service.get_course_recommendations(
            interest, goal, marks
        )
        
        if success:
            ui_service.set_session_value("recommended_courses", courses)
            ui_service.set_session_value("selected_course", None)
            ui_service.set_session_value("roadmap", [])
            st.success(message)
        else:
            ui_service.set_session_value("recommended_courses", [])
            st.error(message)
        
        ui_service.rerun_application()
        
    except Exception as e:
        st.error(f"Error getting course recommendations: {str(e)}")


def handle_course_selection(course_name: str) -> None:
    """Handle course selection and roadmap generation."""
    try:
        # Generate roadmap for selected course
        success, message, roadmap_steps = roadmap_service.generate_roadmap(course_name)
        
        if success:
            ui_service.set_session_value("roadmap", roadmap_steps)
            ui_service.set_session_value("selected_course", course_name)
            st.success(f"Course selected: {course_name}")
        else:
            ui_service.set_session_value("roadmap", [message])
            ui_service.set_session_value("selected_course", course_name)
            st.error(message)
        
        ui_service.rerun_application()
        
    except Exception as e:
        st.error(f"Error selecting course: {str(e)}")


def handle_pdf_generation(course_name: str, roadmap_steps: List[str], websites: List[str]) -> None:
    """Handle PDF roadmap generation."""
    try:
        success, message, pdf_buffer = roadmap_service.generate_pdf_roadmap(
    course_name, roadmap_steps, websites
)

        if success and pdf_buffer:
            st.download_button(
                label="💾 Download PDF",
                data=pdf_buffer,
                file_name=f"{course_name}_roadmap.pdf",
                mime="application/pdf",
                key="download_pdf_btn"
    )
        else:
            st.error(message)
            
    except Exception as e:
        st.error(f"Error generating PDF: {str(e)}")


def main() -> None:
    """Main application function."""
    try:
        # Initialize application
        initialize_application()
        
        # Render particle background
        render_particle_background()
        
        # Render header
        render_header()
        
        # Render KPI dashboard
        render_kpi_dashboard()
        
        # Render main content
        render_main_content_tabs()
        
        # Render welcome section if no content
        courses = ui_service.get_session_value("recommended_courses", [])
        selected_course = ui_service.get_session_value("selected_course")
        if not courses and not selected_course:
            render_welcome_section()
        
        # Render sidebar
        render_sidebar()
        
    except Exception as e:
        st.error(f"Application error: {str(e)}")


if __name__ == "__main__":
    main()
