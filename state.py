import streamlit as st

def init_state():
    """
    Initialize all session_state variables once 
    """

    if "page" not in st.session_state:
        st.session_state.page = "garden"
    if "flower" not in st.session_state:
        st.session_state.flower = None
    
    # Screen 3 memory data
    if "memory_tag" not in st.session_state:
        st.session_state.memory_tag = ""
    if "memory_image" not in st.session_state:
        st.session_state.memory_image = None
    if "memory_image_caption" not in st.session_state:
        st.session_state.memory_image_caption = ""
    if "memory_audio" not in st.session_state:
        st.session_state.memory_audio = None
