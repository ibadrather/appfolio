import streamlit as st
from projects import app as projects_app
from portfolio import app as portfolio_app

# Define the navigation menu
PAGES = {
    "Portfolio": portfolio_app,
    "My Projects": projects_app,  # Add the My Projects page to the navigation menu
}

# Render the app
def main():
    # Set page title, icon, and layout width
    st.set_page_config(
        page_title="Ibad Rather",
        page_icon=":robot_face:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", list(PAGES.keys()))
    PAGES[page]()


if __name__ == "__main__":
    main()
