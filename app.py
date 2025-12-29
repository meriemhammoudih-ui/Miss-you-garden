import streamlit as st

st.set_page_config(page_title="Miss you garden", page_icon="🌸")

#knowing what screen is on display
if "page" not in st.session_state:
    st.session_state.page = "garden"
if "flower" not in st.session_state:
    st.session_state.flower = None

if st.session_state.page == "garden":
    #SCREEN 1: garden
    st.title("Our garden")
    st.write("🌿 A space that grows when we miss each other.")

    if st.button("Thinking of you.."):
        st.session_state.page = "choose_flower"
        st.rerun()

elif st.session_state.page == "choose_flower":
    #SCREEN 2: choose flower
    st.title("Choose a flower")
    st.write("what flower do I remind you of?")

    flowers = ["🌹 Rose", "🌻 Sunflower", "🌷 Tulip", "🌼 Daisy", "🪻 Lavender", "🌸 cherry blossom"]
    selected_flower = st.selectbox("Select a flower:", flowers)

    if st.button("Plant flower"):
        st.session_state.flower = selected_flower
        st.write(f"I remind you of {selected_flower}! <3")
        st.session_state.page = "new_memory"
        st.rerun()

    if st.button("Back to garden"):
        st.session_state.page = "garden"
        st.rerun()

elif st.session_state.page == "new_memory":
    #SCREEN 3: new memory
    st.title("New Memory")
    st.write(f"You planted a {st.session_state.flower}!")