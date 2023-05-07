import streamlit as st
from content.portfolio import app

# Render the app
def main():
    # Set page title, icon, and layout width
    st.set_page_config(
        page_title="Ibad Rather",
        page_icon=":robot_face:",
        layout="wide",
        initial_sidebar_state="auto",
    )

    # display content in the main section
    app()


if __name__ == "__main__":
    main()
