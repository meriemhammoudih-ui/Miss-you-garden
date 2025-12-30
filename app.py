import streamlit as st

st.set_page_config(page_title="Miss you garden", page_icon="🌸")

from state import init_state
init_state()

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
    memory_tag = st.text_area("What made me think of you was...", placeholder="e.g. 'An ugly teddy bear'")
    memory_image = st.file_uploader("What made me think of you looks like...", type=["png", "jpg", "jpeg", "HEIC"], help="Upload an image from that moment.")
    memory_image_caption = st.text_input("Image caption:", placeholder="e.g. 'The ugly teddy bear we got on our first date.'")
    memory_audio = st.file_uploader("What made me think of you sounds like...", type=["mp3", "wav", "m4a"],help="Upload an audio from that moment.")
    
    if st.button("Attatch memory tag!"):
        st.session_state.memory_tag = memory_tag
        st.session_state.memory_image = memory_image
        st.session_state.memory_image_caption = memory_image_caption
        st.session_state.memory_audio = memory_audio
        st.session_state.page = "flower_overview"
        st.rerun()

    if st.button("Back to shop"):
        st.session_state.page = "choose_flower"
        st.rerun()

    if st.button("Back to garden"):
        st.session_state.page = "garden"
        st.rerun()

elif st.session_state.page == "flower_overview":
    #SCREEN 4: flower overview
    st.title("Your flower is ready to reach the garden!")
    st.write(f"Here's your {st.session_state.flower}:")
    st.write(f"**Memory tag:** {st.session_state.memory_tag}")
    if st.session_state.memory_image is not None:
        st.image(st.session_state.memory_image, caption=st.session_state.memory_image_caption)
    
    if st.session_state.memory_audio is not None:
        st.audio(st.session_state.memory_audio)
    
    st.write("Are you ready to send it to the garden?")
    if st.button ("Yes, I'm ready!"):
        st.session_state.page = "garden"
        st.rerun()
    
    if st.button ("No, I need to remember more."):
        st.session_state.page = "new_memory"
        st.rerun()
