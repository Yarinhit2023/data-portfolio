import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime
import numpy as np
from plotly.subplots import make_subplots

# Page config
st.set_page_config(
    page_title="Yarin Noy | Data Expert",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Sample Projects Data
PROJECTS = [
    {
        'title': 'AI-Powered Market Analysis',
        'description': 'Deep learning model for real-time market trend prediction with 94% accuracy',
        'tech_stack': ['Python', 'TensorFlow', 'AWS', 'Docker'],
        'metrics': {'Accuracy': '94%', 'Processing Time': '0.3s', 'Data Points': '1M+'},
        'github_link': 'https://github.com/YarinNoy/market-analysis',
        'live_demo': 'https://demo.market-analysis.com',
    },
    {
        'title': 'Data Pipeline Automation',
        'description': 'Automated ETL pipeline processing 100GB+ daily data with real-time monitoring',
        'tech_stack': ['Apache Airflow', 'Python', 'PostgreSQL', 'Kibana'],
        'metrics': {'Efficiency': '85%', 'Data Volume': '100GB/day', 'Uptime': '99.9%'},
        'github_link': 'https://github.com/YarinNoy/data-pipeline',
        'live_demo': 'https://demo.data-pipeline.com',
    },
    {
        'title': 'Predictive Analytics Dashboard',
        'description': 'Interactive dashboard for business metrics prediction and anomaly detection',
        'tech_stack': ['React', 'Python', 'scikit-learn', 'D3.js'],
        'metrics': {'Prediction Accuracy': '91%', 'Users': '1000+', 'Active Sessions': '200+'},
        'github_link': 'https://github.com/YarinNoy/analytics-dashboard',
        'live_demo': 'https://demo.analytics-dashboard.com',
    }
]

# Social Links Data
SOCIAL_LINKS = {
    'email': 'mailto:yarinnoy@gmail.com',
    'github': 'https://github.com/YarinNoy',
    'linkedin': 'https://linkedin.com/in/yarin-noy',
    'x': 'https://twitter.com/YarinNoy'
}

# Visualization Functions
def create_tech_bubble_chart():
    tech_data = {
        'Technology': ['Python', 'TensorFlow', 'AWS', 'Docker', 'React', 'PostgreSQL', 'Airflow'],
        'Projects': [15, 8, 10, 7, 5, 6, 4],
        'Experience': [5, 3, 4, 3, 2, 4, 2],
        'Category': ['Language', 'ML', 'Cloud', 'DevOps', 'Frontend', 'Database', 'DevOps']
    }
    df = pd.DataFrame(tech_data)
    
    fig = px.scatter(df, x='Projects', y='Experience', size='Projects',
                    color='Category', text='Technology',
                    title='Technology Expertise Map',
                    template='plotly_dark')
    
    fig.update_traces(textposition='top center')
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    return fig

def create_skills_radar():
    categories = ['Data Science', 'Machine Learning', 'Data Engineering',
                 'Cloud Computing', 'DevOps', 'Visualization']
    values = [9, 8, 9, 7, 8, 9]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        line_color='#64FFDA'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        showlegend=False,
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        title='Skills Overview'
    )
    return fig

def create_project_timeline():
    df = pd.DataFrame([
        dict(Task="Market Analysis", Start='2023-01-01', End='2023-06-30', Status='Completed'),
        dict(Task="Data Pipeline", Start='2023-04-01', End='2023-09-30', Status='Completed'),
        dict(Task="Analytics Dashboard", Start='2023-07-01', End='2023-12-31', Status='In Progress'),
    ])
    
    fig = px.timeline(df, x_start="Start", x_end="End", y="Task", color="Status",
                     title="Project Timeline")
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    return fig

def create_impact_metrics():
    fig = go.Figure()
    
    categories = ['Data Processing', 'Model Accuracy', 'User Engagement', 'System Uptime']
    values = [85, 94, 78, 99]
    
    fig.add_trace(go.Bar(
        x=categories,
        y=values,
        marker_color='#64FFDA',
        text=values,
        textposition='auto',
    ))
    
    fig.update_layout(
        title='Key Performance Metrics',
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=False
    )
    
    return fig
# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(45deg, #4A154B, #8B1F60, #BC2666);
    }
    
    .main {
        background: transparent;
    }
    
    .content-wrapper {
        position: relative;
        z-index: 1;
        text-align: center;
        padding-top: 15vh;
    }
    
    .main-title {
        color: white;
        font-size: 5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 0 0 10px rgba(0,0,0,0.3);
    }
    
    .subtitle {
        color: rgba(255,255,255,0.9);
        font-size: 2.5rem;
        font-weight: 500;
        margin-bottom: 3rem;
    }
    
    .social-links {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .social-icon {
        width: 50px;
        height: 50px;
        background: rgba(255,255,255,0.1);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .social-icon:hover {
        transform: translateY(-5px);
        background: rgba(255,255,255,0.2);
    }
    
    .nav-links {
        display: flex;
        justify-content: center;
        gap: 3rem;
        margin-top: 3rem;
    }
    
    .nav-link {
        color: white;
        text-decoration: none;
        font-size: 1.2rem;
        font-weight: 500;
        opacity: 0.8;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .nav-link:after {
        content: '';
        position: absolute;
        width: 0;
        height: 2px;
        bottom: -5px;
        left: 0;
        background-color: white;
        transition: width 0.3s ease;
    }
    
    .nav-link:hover {
        opacity: 1;
    }
    
    .nav-link:hover:after {
        width: 100%;
    }
    
    .section {
        margin-top: 5rem;
        padding: 2rem;
        background: rgba(0,0,0,0.2);
        border-radius: 1rem;
        backdrop-filter: blur(10px);
    }
    
    .project-card {
        background: rgba(255,255,255,0.05);
        border-radius: 1rem;
        padding: 2rem;
        margin-bottom: 2rem;
        transition: transform 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
    }
    
    .tech-stack {
        margin: 1rem 0;
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    
    .tech-tag {
        background: rgba(100, 255, 218, 0.1);
        color: #64FFDA;
        padding: 0.3rem 0.8rem;
        border-radius: 1rem;
        font-size: 0.9rem;
    }
    
    .project-metrics {
        display: flex;
        justify-content: space-around;
        margin: 1.5rem 0;
    }
    
    .metric {
        text-align: center;
    }
    
    .metric-value {
        display: block;
        font-size: 1.5rem;
        color: #64FFDA;
        font-weight: bold;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: rgba(255,255,255,0.7);
    }
    
    .project-links {
        display: flex;
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .project-link {
        color: #64FFDA;
        text-decoration: none;
        padding: 0.5rem 1rem;
        border: 1px solid #64FFDA;
        border-radius: 4px;
        transition: all 0.3s ease;
    }
    
    .project-link:hover {
        background: rgba(100, 255, 218, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Header Section
    st.markdown("""
        <div class="content-wrapper">
            <h1 class="main-title">Yarin Noy</h1>
            <h2 class="subtitle">Data Expert</h2>
            
            <div class="social-links">
                <a href="{}" target="_blank" class="social-icon">📧</a>
                <a href="{}" target="_blank" class="social-icon">GitHub</a>
                <a href="{}" target="_blank" class="social-icon">LinkedIn</a>
                <a href="{}" target="_blank" class="social-icon">𝕏</a>
            </div>
            
            <div class="nav-links">
                <a href="#about" class="nav-link">About</a>
                <a href="#projects" class="nav-link">Projects</a>
                <a href="#contact" class="nav-link">Contact</a>
            </div>
        </div>
    """.format(
        SOCIAL_LINKS['email'],
        SOCIAL_LINKS['github'],
        SOCIAL_LINKS['linkedin'],
        SOCIAL_LINKS['x']
    ), unsafe_allow_html=True)
    
    # About Section with Visualizations
    st.markdown('<div id="about" class="section">', unsafe_allow_html=True)
    st.markdown('### About Me')
    st.write('Data Expert with strong background in Computer Science and Applied Mathematics.')
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_tech_bubble_chart(), use_container_width=True)
    with col2:
        st.plotly_chart(create_skills_radar(), use_container_width=True)
    
    # Projects Section
    st.markdown('<div id="projects" class="section">', unsafe_allow_html=True)
    st.markdown('### Featured Projects')
    
    # Project Timeline
    st.plotly_chart(create_project_timeline(), use_container_width=True)
    
    # Impact Metrics
    st.plotly_chart(create_impact_metrics(), use_container_width=True)
    
    # Project Cards
    for project in PROJECTS:
        st.markdown(f"""
            <div class="project-card">
                <h3>{project['title']}</h3>
                <p>{project['description']}</p>
                <div class="tech-stack">
                    {''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['tech_stack']])}
                </div>
                <div class="project-metrics">
                    {''.join([f'<div class="metric"><span class="metric-value">{value}</span><span class="metric-label">{key}</span></div>' 
                             for key, value in project['metrics'].items()])}
                </div>
                <div class="project-links">
                    <a href="{project['github_link']}" target="_blank" class="project-link">GitHub</a>
                    <a href="{project['live_demo']}" target="_blank" class="project-link">Live Demo</a>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Contact Section
    st.markdown('<div id="contact" class="section">', unsafe_allow_html=True)
    st.markdown('### Get in Touch')
    st.write('Feel free to reach out for collaborations or just a friendly chat.')

    # Hide Streamlit elements
    hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

if __name__ == "__main__":
    main()