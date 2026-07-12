import streamlit as st

def inject_custom_css():
    """
    Injects professional CSS styles into the Streamlit application page
    to match the 'UX School' UI Style Guide inspiration (light/pastel theme, Poppins/Nunito fonts).
    """
    st.markdown(
        """
        <style>
        /* Import Poppins and Nunito from Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600;700&family=Poppins:wght@400;500;600;700&display=swap');
        
        /* Apply fonts and global text color */
        html, body, [class*="css"], .stApp {
            font-family: 'Nunito', sans-serif;
            color: #504E4E;
            background-color: #FDFBFF !important;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Poppins', sans-serif !important;
            color: #AA80CD !important;
            font-weight: 600 !important;
        }

        /* Styled Cards based on the UI Guide */
        .glass-card {
            background-color: #FFFFFF;
            border-radius: 16px;
            padding: 24px;
            border: 1px solid #EFDAFF;
            margin-bottom: 20px;
            box-shadow: 0 8px 24px rgba(170, 128, 205, 0.08);
            transition: all 0.3s ease;
        }
        .glass-card:hover {
            border-color: #AA80CD;
            box-shadow: 0 12px 30px rgba(170, 128, 205, 0.15);
            transform: translateY(-2px);
        }

        /* Section headers with decorative bottom borders */
        .section-header {
            font-family: 'Poppins', sans-serif;
            font-size: 1.4rem;
            font-weight: 600;
            color: #AA80CD;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 2px solid #EFDAFF;
        }

        /* Interactive Quiz Card */
        .quiz-card {
            background-color: #F9F6FC;
            border-radius: 12px;
            padding: 16px;
            border-left: 5px solid #AA80CD;
            margin-bottom: 16px;
            font-weight: 600;
            color: #504E4E;
        }

        /* Info card */
        .info-card {
            background-color: #EFDAFF;
            border: 1px solid rgba(170, 128, 205, 0.3);
            color: #504E4E;
            padding: 14px 18px;
            border-radius: 12px;
            margin-bottom: 18px;
            font-size: 0.95rem;
            line-height: 1.5;
        }

        /* Footer styling */
        .footer-text {
            text-align: center;
            font-size: 0.85rem;
            color: #8D8B8B;
            margin-top: 60px;
            padding-top: 20px;
            border-top: 1px solid #EFDAFF;
        }

        /* Badges based on Style Guide */
        .badge {
            display: inline-block;
            padding: 5px 12px;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .badge-purple {
            background-color: #EFDAFF;
            color: #AA80CD;
            border: 1px solid rgba(170, 128, 205, 0.4);
        }
        .badge-green {
            background-color: #9CDDB8;
            color: #27C47A;
            border: 1px solid rgba(39, 196, 122, 0.4);
        }

        /* Sidebar Panels */
        .sidebar-panel {
            background-color: #FDFBFF;
            border-radius: 12px;
            padding: 14px;
            border: 1px solid #EFDAFF;
            font-size: 0.9rem;
            margin-bottom: 12px;
            box-shadow: 0 4px 12px rgba(170, 128, 205, 0.04);
            color: #504E4E;
        }

        /* Rounded pill-style primary buttons matching UX element guide */
        div.stButton > button {
            background: linear-gradient(135deg, #AA80CD 0%, #B893D6 100%) !important;
            color: white !important;
            border: none !important;
            padding: 10px 24px !important;
            border-radius: 24px !important;
            font-family: 'Poppins', sans-serif !important;
            font-weight: 500 !important;
            font-size: 0.95rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 12px rgba(170, 128, 205, 0.3) !important;
            width: auto !important;
        }
        div.stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 18px rgba(170, 128, 205, 0.45) !important;
            background: linear-gradient(135deg, #B893D6 0%, #AA80CD 100%) !important;
        }
        div.stButton > button:active {
            transform: translateY(0px) !important;
        }

        /* Custom secondary buttons (styled form submit, action items, etc.) */
        div[data-testid="stForm"] div.stButton > button {
            background: #27C47A !important;
            box-shadow: 0 4px 12px rgba(39, 196, 122, 0.3) !important;
        }
        div[data-testid="stForm"] div.stButton > button:hover {
            background: #3CD08C !important;
            box-shadow: 0 6px 18px rgba(39, 196, 122, 0.45) !important;
        }

        /* Search inputs & selectors style */
        div.stTextInput > div > div > input, div.stSelectbox > div > div > div {
            border: 1px solid #EFDAFF !important;
            background-color: #FFFFFF !important;
            border-radius: 20px !important;
            padding-left: 15px !important;
            color: #504E4E !important;
            box-shadow: 0 2px 8px rgba(170, 128, 205, 0.02) !important;
        }
        div.stTextInput > div > div > input:focus {
            border-color: #AA80CD !important;
            box-shadow: 0 0 0 2px rgba(170, 128, 205, 0.2) !important;
        }
        
        /* Custom sidebar styling matching UX School background */
        section[data-testid="stSidebar"] {
            background-color: #F8F4FC !important;
            border-right: 1px solid #EFDAFF;
        }
        
        /* Radio button labels spacing and style */
        div[data-testid="stMarkdownContainer"] p {
            margin-bottom: 0px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
