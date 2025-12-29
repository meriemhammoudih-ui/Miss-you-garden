import streamlit as st

st.set_page_config(page_title="Miss you garden", page_icon="🌸")

#knowing what screen is on display
if "page" not in st.session_state:
    st.session_state.page = "garden"
if "flower" not in st.session_state:
    st.session_state.flower = None
if "confirm_flower" not in st.session_state:
    st.session_state.confirm_flower = False

if st.session_state.page == "garden":
    #SCREEN 1: garden
    st.title("Our garden")
    st.write("🌿 A space that grows when we miss each other.")

    if st.button("Thinking of you.."):
        st.session_state.page = "choose_flower"
        st.rerun()

elif st.session_state.page == "choose_flower":
    #SCREEN 2: choose flower
    st.title("Welcome to the flower shop!")
    st.write("Before you are several seeds. What flower are you reminded of?")

    flowers = ["🌹 rose", "🌻 sunflower", "🌷 tulip", "🌼 daisy", "🪻 lavender", "🌸 cherry blossom"]
    selected_flower = st.selectbox("I see you reflected in a...", flowers)

    if st.button("Pick up seed"):
        st.session_state.flower = selected_flower
        st.session_state.page = "confirm_flower"
        st.rerun()

    if st.button("Back to garden"):
        st.session_state.page = "garden"
        st.rerun()

elif st.session_state.page == "confirm_flower":
    #SCREEN 2.5: confirm flower
    st.title("Checkout.")
    st.write(f"In your hands is a {st.session_state.flower} seed... will you take it?")

    if st.button("Yes, plant it!"):
        st.session_state.page = "new_memory"
        st.rerun()

    if st.button("No, let me think again..."):
        st.session_state.page = "choose_flower"
        st.rerun()


elif st.session_state.page == "new_memory":
    #SCREEN 3: new memory
    st.title("A new memory has been planted!")
    st.write(f"You planted a {st.session_state.flower}!")

    st.subheader("Memory tag:")
    memory_tag = st.text_input("I found you when...", "")
    memory_tag = st.text_area("Describe the memory:", "")