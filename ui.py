import streamlit as st
from youtube_analyzer import build_youtube_agent


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Synora AI | YouTube Video Analyzer",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

/* ============================================================
   SYNORA AI BRAND COLORS
   ============================================================ */

:root {
    --synora-red: #ff0033;
    --synora-coral: #ff4d67;
    --synora-violet: #7c3aed;
    --synora-pink: #f43f5e;
    --synora-purple: #6d28d9;
}


/* ============================================================
   GLOBAL BACKGROUND
   ============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at 12% 8%,
            rgba(255, 0, 51, 0.08) 0%,
            rgba(255, 0, 51, 0) 30%
        ),
        radial-gradient(
            circle at 88% 12%,
            rgba(124, 58, 237, 0.09) 0%,
            rgba(124, 58, 237, 0) 32%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(255, 77, 103, 0.05) 0%,
            rgba(255, 77, 103, 0) 30%
        ),
        linear-gradient(
            135deg,
            #fffafb 0%,
            #f8f7ff 50%,
            #faf9ff 100%
        ) !important;

    color: #172033 !important;
}

.main {
    background: transparent !important;
}

.block-container {
    max-width: 1180px !important;
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
}


/* ============================================================
   STREAMLIT HEADER
   ============================================================ */

header[data-testid="stHeader"] {
    background: transparent !important;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background:
        radial-gradient(
            circle at 10% 5%,
            rgba(255, 0, 51, 0.11) 0%,
            rgba(255, 0, 51, 0) 35%
        ),
        radial-gradient(
            circle at 90% 95%,
            rgba(124, 58, 237, 0.11) 0%,
            rgba(124, 58, 237, 0) 35%
        ),
        linear-gradient(
            180deg,
            #fffafb 0%,
            #f8f7ff 100%
        ) !important;

    border-right: 1px solid rgba(124, 58, 237, 0.12) !important;
}

section[data-testid="stSidebar"] > div {
    padding-top: 2rem !important;
}


/* ============================================================
   SIDEBAR BRAND
   ============================================================ */

.sidebar-brand {
    font-size: 24px !important;
    font-weight: 900 !important;
    letter-spacing: -0.5px !important;

    background: linear-gradient(
        90deg,
        #ff0033 0%,
        #ff4d67 45%,
        #7c3aed 100%
    ) !important;

    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;

    margin-bottom: 2px !important;
}

.sidebar-tagline {
    color: #6b7280 !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    letter-spacing: 0.2px !important;
    margin-bottom: 8px !important;
}

.sidebar-description {
    color: #6b7280 !important;
    font-size: 13px !important;
    line-height: 1.6 !important;
}

section[data-testid="stSidebar"] hr {
    border: none !important;

    height: 1px !important;

    background: linear-gradient(
        90deg,
        rgba(255, 0, 51, 0.15),
        rgba(124, 58, 237, 0.15)
    ) !important;

    margin: 1.4rem 0 !important;
}

section[data-testid="stSidebar"] h3 {
    color: #374151 !important;
    font-size: 15px !important;
    font-weight: 700 !important;
}

section[data-testid="stSidebar"] .stMarkdown p {
    color: #374151 !important;
}

section[data-testid="stSidebar"] .stMarkdown li {
    color: #4b5563 !important;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {
    position: relative !important;

    width: 100% !important;

    text-align: center !important;

    padding: 55px 20px 45px 20px !important;
}


/* Hero ambient glow */

.hero::before {
    content: "" !important;

    position: absolute !important;

    width: 520px !important;
    height: 260px !important;

    left: 50% !important;
    top: 25px !important;

    transform: translateX(-50%) !important;

    background: linear-gradient(
        90deg,
        rgba(255, 0, 51, 0.11),
        rgba(255, 77, 103, 0.07),
        rgba(124, 58, 237, 0.11)
    ) !important;

    filter: blur(65px) !important;

    border-radius: 50% !important;

    pointer-events: none !important;

    z-index: 0 !important;
}

.hero > * {
    position: relative !important;
    z-index: 1 !important;
}


/* ============================================================
   HERO BADGE
   ============================================================ */

.hero-badge {
    display: inline-block !important;

    padding: 8px 18px !important;

    border-radius: 999px !important;

    background: linear-gradient(
        135deg,
        rgba(255, 0, 51, 0.08),
        rgba(124, 58, 237, 0.08)
    ) !important;

    border: 1px solid rgba(255, 0, 51, 0.18) !important;

    color: #e11d48 !important;

    font-size: 12px !important;

    font-weight: 800 !important;

    letter-spacing: 0.5px !important;

    box-shadow:
        0 5px 18px rgba(225, 29, 72, 0.08) !important;
}


/* ============================================================
   HERO BRAND NAME
   ============================================================ */

.hero-brand {
    font-size: 54px !important;

    font-weight: 900 !important;

    line-height: 1.05 !important;

    margin: 20px 0 6px 0 !important;

    padding: 0 !important;

    letter-spacing: -2px !important;

    background: linear-gradient(
        90deg,
        #ff0033 0%,
        #ff4d67 45%,
        #7c3aed 100%
    ) !important;

    -webkit-background-clip: text !important;

    -webkit-text-fill-color: transparent !important;

    background-clip: text !important;
}


/* ============================================================
   HERO TAGLINE
   ============================================================ */

.hero-tagline {
    color: #374151 !important;

    font-size: 18px !important;

    font-weight: 600 !important;

    letter-spacing: 0.1px !important;

    margin: 0 0 12px 0 !important;
}


/* ============================================================
   HERO DESCRIPTION
   ============================================================ */

.hero-description {
    max-width: 720px !important;

    margin: 0 auto !important;

    color: #6b7280 !important;

    font-size: 16px !important;

    line-height: 1.7 !important;

    text-align: center !important;
}


/* ============================================================
   FEATURE CARDS
   ============================================================ */

.feature-card {
    position: relative !important;

    overflow: hidden !important;

    background: rgba(255, 255, 255, 0.94) !important;

    border: 1px solid rgba(229, 231, 235, 0.90) !important;

    border-radius: 16px !important;

    padding: 24px !important;

    min-height: 185px !important;

    height: 100% !important;

    box-sizing: border-box !important;

    box-shadow:
        0 8px 25px rgba(15, 23, 42, 0.05) !important;

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease,
        border-color 0.2s ease !important;
}

.feature-card:hover {
    transform: translateY(-4px) !important;

    border-color: rgba(244, 63, 94, 0.25) !important;

    box-shadow:
        0 15px 35px rgba(124, 58, 237, 0.10) !important;
}


/* Gradient card accent */

.feature-card::before {
    content: "" !important;

    position: absolute !important;

    top: 0 !important;

    left: 20px !important;

    right: 20px !important;

    height: 2px !important;

    background: linear-gradient(
        90deg,
        #ff0033,
        #ff4d67,
        #7c3aed
    ) !important;

    border-radius: 0 0 10px 10px !important;

    opacity: 0.75 !important;
}


/* ============================================================
   FEATURE ICON
   ============================================================ */

.feature-icon {
    width: 47px !important;

    height: 47px !important;

    display: flex !important;

    align-items: center !important;

    justify-content: center !important;

    background: linear-gradient(
        135deg,
        rgba(255, 0, 51, 0.09),
        rgba(124, 58, 237, 0.10)
    ) !important;

    border: 1px solid rgba(244, 63, 94, 0.12) !important;

    border-radius: 12px !important;

    font-size: 23px !important;

    margin-bottom: 14px !important;

    box-shadow:
        0 5px 15px rgba(124, 58, 237, 0.07) !important;
}

.feature-title {
    font-size: 18px !important;

    font-weight: 700 !important;

    color: #111827 !important;

    margin-bottom: 8px !important;
}

.feature-description {
    font-size: 14px !important;

    line-height: 1.6 !important;

    color: #6b7280 !important;
}


/* ============================================================
   ANALYZER SECTION
   ============================================================ */

.analyzer-title {
    font-size: 26px !important;

    font-weight: 800 !important;

    color: #111827 !important;

    margin-top: 45px !important;

    margin-bottom: 7px !important;
}

.analyzer-description {
    color: #6b7280 !important;

    font-size: 15px !important;

    margin-bottom: 18px !important;
}


/* ============================================================
   INPUT
   ============================================================ */

div[data-testid="stTextInput"] {
    width: 100% !important;
}

div[data-testid="stTextInput"] input {
    background: rgba(255, 255, 255, 0.95) !important;

    color: #111827 !important;

    border: 1px solid #d1d5db !important;

    border-radius: 11px !important;

    min-height: 48px !important;

    padding: 10px 15px !important;

    font-size: 15px !important;

    box-shadow:
        0 4px 12px rgba(15, 23, 42, 0.03) !important;
}

div[data-testid="stTextInput"] input::placeholder {
    color: #9ca3af !important;
}

div[data-testid="stTextInput"] input:focus {
    border-color: #ff3655 !important;

    box-shadow:
        0 0 0 1px #ff3655,
        0 5px 20px rgba(255, 0, 51, 0.08) !important;
}


/* ============================================================
   ANALYZE BUTTON
   ============================================================ */

div.stButton {
    width: 100% !important;
}

div.stButton > button {
    width: 100% !important;

    min-height: 49px !important;

    background: linear-gradient(
        135deg,
        #ff0033 0%,
        #ff4d67 45%,
        #7c3aed 100%
    ) !important;

    color: #ffffff !important;

    border: none !important;

    border-radius: 11px !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    padding: 12px 20px !important;

    box-shadow:
        0 7px 20px rgba(225, 29, 72, 0.20) !important;

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease !important;
}

div.stButton > button:hover {
    background: linear-gradient(
        135deg,
        #e6002f 0%,
        #f43f5e 45%,
        #6d28d9 100%
    ) !important;

    color: #ffffff !important;

    border: none !important;

    transform: translateY(-2px) !important;

    box-shadow:
        0 12px 30px rgba(225, 29, 72, 0.25) !important;
}

div.stButton > button:focus {
    background: linear-gradient(
        135deg,
        #ff0033 0%,
        #ff4d67 45%,
        #7c3aed 100%
    ) !important;

    color: #ffffff !important;

    border: none !important;

    outline: none !important;
}


/* ============================================================
   RESULT
   ============================================================ */

.result-header {
    position: relative !important;

    overflow: hidden !important;

    background: linear-gradient(
        135deg,
        rgba(255, 0, 51, 0.07),
        rgba(255, 77, 103, 0.06),
        rgba(124, 58, 237, 0.08)
    ) !important;

    border: 1px solid rgba(244, 63, 94, 0.18) !important;

    border-radius: 14px !important;

    padding: 20px 22px !important;

    margin-top: 35px !important;

    box-shadow:
        0 8px 25px rgba(124, 58, 237, 0.06) !important;
}

.result-header::before {
    content: "" !important;

    position: absolute !important;

    top: 0 !important;

    left: 0 !important;

    width: 100% !important;

    height: 3px !important;

    background: linear-gradient(
        90deg,
        #ff0033,
        #ff4d67,
        #7c3aed
    ) !important;
}

.result-title {
    background: linear-gradient(
        90deg,
        #e11d48 0%,
        #7c3aed 100%
    ) !important;

    -webkit-background-clip: text !important;

    -webkit-text-fill-color: transparent !important;

    background-clip: text !important;

    font-size: 21px !important;

    font-weight: 800 !important;
}

.result-subtitle {
    color: #6b7280 !important;

    font-size: 13px !important;

    margin-top: 4px !important;
}


/* ============================================================
   ALERTS
   ============================================================ */

div[data-testid="stAlert"] {
    border-radius: 11px !important;
}


/* ============================================================
   EXPANDER
   ============================================================ */

div[data-testid="stExpander"] {
    background: rgba(255, 255, 255, 0.95) !important;

    border: 1px solid #e5e7eb !important;

    border-radius: 11px !important;
}


/* ============================================================
   CAPTION
   ============================================================ */

div[data-testid="stCaptionContainer"] {
    color: #6b7280 !important;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    position: relative !important;

    text-align: center !important;

    color: #9ca3af !important;

    font-size: 13px !important;

    padding: 25px 0 10px 0 !important;

    margin-top: 35px !important;
}

.footer::before {
    content: "" !important;

    display: block !important;

    width: 100% !important;

    height: 1px !important;

    margin-bottom: 18px !important;

    background: linear-gradient(
        90deg,
        transparent 0%,
        rgba(255, 0, 51, 0.20) 25%,
        rgba(255, 77, 103, 0.35) 50%,
        rgba(124, 58, 237, 0.20) 75%,
        transparent 100%
    ) !important;
}

.footer-brand {
    margin-bottom: 10px !important;
    font-size: 13px !important;
    color: #6b7280 !important;
}

.footer-brand strong {
    background: linear-gradient(
        90deg,
        #e11d48,
        #7c3aed
    ) !important;

    -webkit-background-clip: text !important;

    -webkit-text-fill-color: transparent !important;

    background-clip: text !important;
}

.footer-credit {
    margin-bottom: 8px !important;
    color: #6b7280 !important;
}

.footer-credit a {
    text-decoration: none !important;
}

.footer-credit strong {
    background: linear-gradient(
        90deg,
        #e11d48,
        #7c3aed
    ) !important;

    -webkit-background-clip: text !important;

    -webkit-text-fill-color: transparent !important;

    background-clip: text !important;

    font-weight: 700 !important;
}

.footer-social {
    margin-bottom: 10px !important;
}

.footer-social a {
    color: #2563eb !important;
    text-decoration: none !important;
    font-weight: 500 !important;
}

.footer-social a:hover {
    text-decoration: underline !important;
}

.footer-tagline {
    color: #9ca3af !important;
    font-size: 13px !important;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 768px) {

    .hero {
        padding: 35px 10px !important;
    }

    .hero-brand {
        font-size: 40px !important;
    }

    .hero-tagline {
        font-size: 16px !important;
    }

    .hero-description {
        font-size: 14px !important;
    }

    .feature-card {
        margin-bottom: 15px !important;
    }

}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# LOAD AI AGENT
# ============================================================

@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent = get_agent()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-brand">SYNORA AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-tagline">'
        'Intelligence Behind Every Video.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-description">'
        'AI-powered YouTube video analysis for '
        'structured insights and understanding.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### ✨ Analysis Features")

    st.markdown(
        """
- 🎬 Video overview
- ⏱️ Smart timestamps
- 🧠 Main themes
- 📚 Key learning points
- 🔍 Practical insights
"""
    )

    st.divider()

    st.markdown("### ⚙️ Technology Stack")

    st.markdown(
        """
**LLM:** GPT-OSS 120B  
**Framework:** Agno  
**Tool:** YouTubeTools  
**Interface:** Streamlit  
**Language:** Python
"""
    )

    st.divider()

    st.caption(
        "SYNORA AI · YouTube Intelligence"
    )


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
<div class="hero">

<div class="hero-badge">
✦ AI-POWERED YOUTUBE VIDEO ANALYZER
</div>

<div class="hero-brand">
SYNORA AI
</div>

<div class="hero-tagline">
Intelligence Behind Every Video.
</div>

<p class="hero-description">
Transform long-form YouTube videos into structured summaries,
smart timestamps, key topics, learning points, and actionable insights.
</p>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# FEATURE CARDS
# ============================================================

col1, col2, col3 = st.columns(
    3,
    gap="medium"
)


with col1:

    st.markdown(
        """
<div class="feature-card">

<div class="feature-icon">
🎬
</div>

<div class="feature-title">
Video Overview
</div>

<div class="feature-description">
Understand the purpose, content type, and overall
context of the YouTube video.
</div>

</div>
""",
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
<div class="feature-card">

<div class="feature-icon">
⏱️
</div>

<div class="feature-title">
Smart Timestamps
</div>

<div class="feature-description">
Identify important sections and organize the
major topics covered throughout the video.
</div>

</div>
""",
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
<div class="feature-card">

<div class="feature-icon">
🧠
</div>

<div class="feature-title">
Key Insights
</div>

<div class="feature-description">
Extract important themes, learning points,
and practical takeaways from the content.
</div>

</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# ANALYZER SECTION
# ============================================================

st.markdown(
    '<div class="analyzer-title">'
    '🔗 Analyze a YouTube Video'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="analyzer-description">'
    'Paste a public YouTube video URL below and let '
    'SYNORA AI generate a structured analysis.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# YOUTUBE URL
# ============================================================

video_url = st.text_input(
    "YouTube URL",
    placeholder="https://www.youtube.com/watch?v=...",
    label_visibility="collapsed"
)

st.caption(
    "💡 Use a public YouTube video with an accessible transcript."
)


# ============================================================
# ANALYZE BUTTON
# ============================================================

analyze = st.button(
    "🚀 Analyze Video"
)


# ============================================================
# ANALYSIS
# ============================================================

if analyze:

    # --------------------------------------------------------
    # EMPTY URL
    # --------------------------------------------------------

    if not video_url.strip():

        st.warning(
            "⚠️ Please enter a YouTube video URL."
        )


    # --------------------------------------------------------
    # INVALID URL
    # --------------------------------------------------------

    elif (
        "youtube.com" not in video_url.lower()
        and "youtu.be" not in video_url.lower()
    ):

        st.error(
            "❌ Please enter a valid YouTube URL."
        )


    # --------------------------------------------------------
    # VALID URL
    # --------------------------------------------------------

    else:

        with st.spinner(
            "🤖 SYNORA AI is analyzing the video..."
        ):

            try:

                response = agent.run(
                    f"Analyze this video: {video_url}"
                )


                # ------------------------------------------------
                # RESULT HEADER
                # ------------------------------------------------

                st.markdown(
                    """
<div class="result-header">

<div class="result-title">
📊 SYNORA AI Analysis
</div>

<div class="result-subtitle">
AI-generated YouTube video intelligence
</div>

</div>
""",
                    unsafe_allow_html=True
                )


                # ------------------------------------------------
                # RESULT CONTENT
                # ------------------------------------------------

                if response and response.content:

                    st.markdown(
                        response.content
                    )

                else:

                    st.warning(
                        "SYNORA AI did not return any analysis."
                    )


            except Exception as e:

                st.error(
                    "⚠️ Something went wrong while analyzing the video."
                )

                with st.expander(
                    "Technical details"
                ):

                    st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer">
<div class="footer-brand"><strong>SYNORA AI</strong> · AI-Powered YouTube Video Analyzer</div>
<div class="footer-credit">Built by <a href="mailto:rathivaishnavi949@gmail.com"><strong>Vaishnavi Rathi</strong></a></div>
<div class="footer-social">
<a href="https://www.linkedin.com/in/vaishnavi-rathi-/" target="_blank">LinkedIn</a>
&nbsp;·&nbsp;
<a href="https://github.com/VaishnaviRathiii" target="_blank">GitHub</a>
</div>
<div class="footer-tagline">Intelligence Behind Every Video.</div>
</div>
""",
    unsafe_allow_html=True
)
