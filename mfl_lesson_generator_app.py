
import streamlit as st

st.set_page_config(page_title="MFL Lesson Generator", page_icon="📚")

st.title("MFL Lesson Generator")
st.markdown("This tool helps you create custom prompts to generate full lesson resources using ChatGPT.")

language = st.selectbox("Language", ["Spanish", "French", "German"])
year = st.selectbox("Year Group", ["Year 7", "Year 8", "Year 9", "Year 10", "Year 11"])
exam_board = st.selectbox("Exam Board", ["AQA", "Edexcel", "OCR"])
topic = st.text_input("Topic (e.g., Mi familia)", placeholder="Enter your lesson topic")
focus = st.multiselect("Thematic Focus", ["Vocabulary", "Grammar", "Listening", "Speaking", "Reading", "Writing"])
output_type = st.selectbox("Output Type", [
    "Full lesson pack", "PowerPoint only", "Worksheet only", 
    "Starter/Plenary activity", "Game"
])

if st.button("Generate Prompt"):
    if topic.strip() == "":
        st.warning("Please enter a topic to generate your prompt.")
    else:
        prompt = (
            f"Create a [{output_type}] for [{language}], aimed at {year} students "
            f"following the [{exam_board}] curriculum.\n"
            f"Topic: [\"{topic}\"]\n"
            f"Thematic Focus: [{' / '.join(focus)}]\n"
            f"Please include scaffolded tasks for mixed-ability learners, challenge options, "
            f"visual elements (illustrations, colour), and interactive features "
            f"(e.g., click-to-reveal vocabulary in slides)."
        )
        st.text_area("Copy and paste this into ChatGPT:", value=prompt, height=300)
