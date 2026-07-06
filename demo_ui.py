"""
Enhanced Demo script to showcase beautiful UI improvements for EduVision AI
This script demonstrates the new enhanced UI components and styling
"""

import streamlit as st

# Load custom CSS
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.set_page_config(
    page_title="EduVision AI - Beautiful UI Demo",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Particle background effect
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

# Enhanced Demo Header
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
        ">Beautiful UI Demo - Enhanced Phase 1</p>
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
            ">✨ Glassmorphism</span>
            <span style="
                background: rgba(255,255,255,0.2);
                backdrop-filter: blur(10px);
                padding: 0.5rem 1rem;
                border-radius: 20px;
                color: white;
                font-size: 0.9rem;
                border: 1px solid rgba(255,255,255,0.3);
            ">🚀 Animations</span>
            <span style="
                background: rgba(255,255,255,0.2);
                backdrop-filter: blur(10px);
                padding: 0.5rem 1rem;
                border-radius: 20px;
                color: white;
                font-size: 0.9rem;
                border: 1px solid rgba(255,255,255,0.3);
            ">🎨 Modern Design</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Enhanced KPI Section Demo
st.subheader("📊 Enhanced KPI Cards Demo")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="kpi-card glow-effect">
        <div style="font-size: 2rem; margin-bottom: 1rem;">📚</div>
        <div class="kpi-value">5</div>
        <div class="kpi-label">Courses Found</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="kpi-card glow-effect">
        <div style="font-size: 2rem; margin-bottom: 1rem;">✅</div>
        <div class="kpi-value">Selected</div>
        <div class="kpi-label">Course Status</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="kpi-card glow-effect">
        <div style="font-size: 2rem; margin-bottom: 1rem;">🗺️</div>
        <div class="kpi-value">8</div>
        <div class="kpi-label">Roadmap Steps</div>
    </div>
    """, unsafe_allow_html=True)

# Enhanced Tabs Demo
st.subheader("📑 Enhanced Tabs Demo")
tab1, tab2, tab3 = st.tabs(["📚 Course Recommendations", "🗺️ Learning Roadmap", "🌐 Learning Resources"])

with tab1:
    st.markdown('<div class="custom-card glow-effect">', unsafe_allow_html=True)
    st.subheader("✅ Recommended Courses")
    st.markdown("Choose a course to see its detailed roadmap:")
    
    # Demo course buttons
    if st.button("🎓 Bachelor of Technology in Computer Science", key="demo_course_1"):
        st.success("Course selected!")
    
    if st.button("🎓 Bachelor of Medicine and Bachelor of Surgery", key="demo_course_2"):
        st.success("Course selected!")
    
    if st.button("🎓 Bachelor of Business Administration", key="demo_course_3"):
        st.success("Course selected!")
    
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="custom-card glow-effect">', unsafe_allow_html=True)
    st.subheader("📍 Learning Roadmap")
    
    # Demo roadmap steps
    demo_steps = [
        "Learn Python & Programming Basics",
        "Understand Data Structures & Algorithms", 
        "Dive into Machine Learning Basics",
        "Build AI Projects & Deploy",
        "Prepare for AI/ML Job Interviews"
    ]
    
    for i, step in enumerate(demo_steps, 1):
        st.markdown(f"""
        <div class="roadmap-step glow-effect">
            <span class="roadmap-step-number">{i}</span>
            {step}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="custom-card glow-effect">', unsafe_allow_html=True)
    st.subheader("🌐 Learning Resources")
    st.markdown("**Top websites to enhance your learning:**")
    
    # Demo website links
    demo_websites = [
        "https://www.coursera.org",
        "https://www.udemy.com", 
        "https://www.edx.org"
    ]
    
    for site in demo_websites:
        st.markdown(f'<a href="{site}" target="_blank" class="website-link glow-effect">{site}</a>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Enhanced PDF Download Demo
    st.markdown('<div class="custom-card glow-effect">', unsafe_allow_html=True)
    st.subheader("📄 Download Your Roadmap")
    st.markdown("Get a printable PDF version of your learning roadmap:")
    
    if st.button("📥 Download Roadmap as PDF", key="demo_pdf_btn"):
        st.success("PDF generation started!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Enhanced Sidebar Demo
with st.sidebar:
    st.title("🎯 EduVision AI")
    
    st.markdown('<div class="custom-card glow-effect">', unsafe_allow_html=True)
    st.subheader("📝 Your Information")
    
    interest = st.text_input("Your Interest", placeholder="e.g., Technology, Medicine, Business")
    goal = st.text_input("Your Career Goal", placeholder="e.g., Software Engineer, Doctor, Manager")
    marks = st.text_input("Your 12th Marks (%)", placeholder="Enter your percentage")
    
    if st.button("🚀 Get Recommended Courses", key="demo_get_courses_btn"):
        if interest and goal and marks:
            st.success("Form submitted successfully!")
        else:
            st.warning("Please fill all fields.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Enhanced Welcome Section Demo
st.markdown("---")
st.subheader("🚀 Enhanced Welcome Section Demo")

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
            Experience the most beautiful and modern UI design for career guidance and learning roadmaps.
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
                ">✨</h3>
                <p style="
                    color: #1e293b; 
                    font-size: 1.1rem;
                    font-weight: 600;
                    margin: 0;
                ">Glassmorphism</p>
                <p style="
                    color: #64748b; 
                    font-size: 0.9rem;
                    margin: 0.5rem 0 0 0;
                ">Modern glass effects</p>
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
                ">🎨</h3>
                <p style="
                    color: #1e293b; 
                    font-size: 1.1rem;
                    font-weight: 600;
                    margin: 0;
                ">Beautiful Design</p>
                <p style="
                    color: #64748b; 
                    font-size: 0.9rem;
                    margin: 0.5rem 0 0 0;
                ">Stunning visuals</p>
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
                ">🚀</h3>
                <p style="
                    color: #1e293b; 
                    font-size: 1.1rem;
                    font-weight: 600;
                    margin: 0;
                ">Smooth Animations</p>
                <p style="
                    color: #64748b; 
                    font-size: 0.9rem;
                    margin: 0.5rem 0 0 0;
                ">Fluid interactions</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Feature Showcase
st.markdown("---")
st.subheader("🎨 Feature Showcase")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="custom-card glow-effect">', unsafe_allow_html=True)
    st.subheader("✨ Glassmorphism Effects")
    st.markdown("""
    - **Backdrop blur** for modern glass look
    - **Transparent backgrounds** with subtle borders
    - **Layered depth** for visual hierarchy
    - **Smooth transitions** between states
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="custom-card glow-effect">', unsafe_allow_html=True)
    st.subheader("🎭 Advanced Animations")
    st.markdown("""
    - **Floating particles** in background
    - **Hover effects** with transforms
    - **Smooth transitions** using cubic-bezier
    - **Staggered animations** for cards
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Final Summary
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 3rem 0; color: #64748b;">
    <h2 style="color: #1e293b; margin-bottom: 1rem;">🎉 Enhanced UI Complete!</h2>
    <p style="font-size: 1.2rem; margin-bottom: 2rem;">
        Experience the most beautiful and modern UI design for EduVision AI
    </p>
    <div style="
        display: flex;
        justify-content: center;
        gap: 2rem;
        flex-wrap: wrap;
        margin-top: 2rem;
    ">
        <span style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem 2rem;
            border-radius: 25px;
            font-weight: 600;
            box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
        ">✨ Glassmorphism</span>
        <span style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 1rem 2rem;
            border-radius: 25px;
            font-weight: 600;
            box-shadow: 0 8px 32px rgba(240, 147, 251, 0.3);
        ">🎨 Modern Design</span>
        <span style="
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            padding: 1rem 2rem;
            border-radius: 25px;
            font-weight: 600;
            box-shadow: 0 8px 32px rgba(79, 172, 254, 0.3);
        ">🚀 Smooth Animations</span>
    </div>
</div>
""", unsafe_allow_html=True)
