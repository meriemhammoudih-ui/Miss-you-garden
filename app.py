import streamlit as st

st.set_page_config(page_title="Miss you garden", page_icon="🌸")

st.title("This month's garden")
st.write("🌿 A little space that grows whenever we miss each other.")

if st.button("Plant a memory"):
    st.write("➡️ Next: memory screen (coming soon!)")
