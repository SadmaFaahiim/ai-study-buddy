import streamlit as st
from src.core.persona import AIPersona

def render_header():
    """Renders the main header and logo of the application."""
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 30px;">
            <span style="font-size: 3rem;">🎓</span>
            <h1 class="gradient-text" style="font-size: 2.8rem; margin: 10px 0 5px 0;">AI Learning Buddy</h1>
            <p style="color: #8D8B8B; font-size: 1.1rem; max-width: 600px; margin: 0 auto;">
                Your dedicated AI Tutor powered by Google Gemini. Explore concepts, test your understanding, and get real-world examples!
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_footer():
    """Renders the footer layout."""
    st.markdown(
        """
        <div class="footer-text">
            <p>Made with ❤️ using Streamlit & Google Gemini API | AI Learning Buddy © 2026</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_sidebar_info(model_name: str):
    """
    Renders detailed information about the active AI Tutor persona in the sidebar.
    
    Args:
        model_name: Name of the Gemini model loaded.
    """
    st.sidebar.markdown("### 🎓 About Your Tutor")
    st.sidebar.markdown(
        f"""
        <div class="sidebar-panel">
            <strong>Name:</strong> {AIPersona.NAME}<br>
            <strong>Role:</strong> Gentle, structured tutor for students.<br>
            <strong>Engine:</strong> <code>{model_name}</code>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.sidebar.markdown("### 🌟 Prompt Strategies")
    st.sidebar.markdown(
        """
        <div class="sidebar-panel" style="font-size: 0.85rem;">
            This buddy uses structured <strong>Role Prompting</strong> and 
            <strong>Few-Shot Formatting</strong> templates to:
            <ul style="padding-left: 18px; margin: 6px 0;">
                <li>Simplify complex terms with analogies.</li>
                <li>Provide clean real-world examples.</li>
                <li>Deliver interactive quizzes.</li>
                <li>Constructively grade student work.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_card(title: str, content: str, badge_text: str = None, badge_type: str = "purple"):
    """
    Renders content in a styled container with optional badges.
    
    Args:
        title: Card header text.
        content: Main body text (rendered as markdown).
        badge_text: Optional text for a top-corner badge.
        badge_type: 'purple' or 'green' styling.
    """
    badge_html = ""
    if badge_text:
        badge_class = f"badge-{badge_type}"
        badge_html = f'<div style="text-align: right;"><span class="badge {badge_class}">{badge_text}</span></div>'
        
    st.markdown(
        f"""
        <div class="glass-card">
            {badge_html}
            <div class="section-header">{title}</div>
            <div style="line-height: 1.6; color: #504E4E;">
        """,
        unsafe_allow_html=True
    )
    st.markdown(content)
    st.markdown("</div></div>", unsafe_allow_html=True)

def render_info_box(message: str):
    """Renders a custom info notification card."""
    st.markdown(
        f"""
        <div class="info-card">
            💡 <strong>Tutor Tip:</strong> {message}
        </div>
        """,
        unsafe_allow_html=True
    )
