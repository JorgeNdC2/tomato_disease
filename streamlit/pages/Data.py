# Imports
import streamlit as st

# Streamlit code
st.set_page_config(
    page_title="Data",
    page_icon="🍅",
)

st.write("# Dataset Tomato Leaf Disease Project! 🍅")
st.sidebar.title("Pages")
st.sidebar.success("Select a page above.")

st.markdown(
    """
    Hey there! 👋 

    This is a dashboard for our Tomato Leaf Disease Project.

    You can navigate through the pages using the sidebar on the left, where you can find the following options:

    - **Home**: This page.

    - **Models**: A summary with the results we have obtained from the models we have trained. You can find a line chart with the accuracy and validation accuracy of the models in the `Models` tab.

    - **Data**: A summary of the data we have used to train our models. You can get a glimpse of the data in the `Data` tab.
    """
)
