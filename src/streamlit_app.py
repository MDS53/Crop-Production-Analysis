import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
from Analysis import show_analysis__
from relationship import show_relationships
from welcome import custom_css,heading_text,subheading_text,quote_text
from logger import logging

df = pd.read_csv("Crop Production data (1).csv")
try:
    st.set_page_config(page_title="Crop Analysis", page_icon="🌾",layout="wide")
    st.markdown(custom_css, unsafe_allow_html=True)
    # Display the heading, subheading, and quote
    st.markdown(heading_text, unsafe_allow_html=True)
    st.markdown(subheading_text, unsafe_allow_html=True)
    st.markdown(quote_text, unsafe_allow_html=True)
    # Get the current query parameters
    st.title("   ")
    query_params = st.experimental_get_query_params()
    page = query_params.get('page', ['home'])[0]

    #st.set_page_config(page_title="Crop Analysis", page_icon="🌾")
    logging.info("Home page ran successfully ") 
    # Define the Analysis page content
except Exception as e:
    logging.exception(f"Error {e} at app.py file ")
    
    
def show_analysis():
    try:
        k=show_analysis__()
        
        logging.info(f"show_analysis() ran successfully ")
        #st.button('Go to Home', on_click=go_to_home)
    except Exception as e:
        logging.exception(f"Error {e} at app.py file in show_analysis() ")


# Define the Relationship page content
def show_relationship():
    
    try:
        a=show_relationships()
        logging.info(f"show_analysis() ran successfully ")
       # st.button('Go to Home', on_click=go_to_home)
    except Exception as e:
        logging.exception(f"Error {e} at app.py file in show_relationship() ")
        
        
def show_dataframe():
    st.title("Crop Production DataFrame")
    st.dataframe(df)
    

# Define the Home page content
def show_home():
    st.title("Discover insights in Crop Production Analysis with these below buttons.")
    if st.button('Go to Analysis'):
        st.experimental_set_query_params(page='analysis')
        #st.experimental_rerun() # this will reruns the application from start
    if st.button('Go to Relationship'):
        st.experimental_set_query_params(page='relationship')
        #st.experimental_rerun()
    if st.button('Go to DataFrame'):
        st.experimental_set_query_params(page='dataframe')
def go_to_home():
    st.experimental_set_query_params(page='home')

# Display the appropriate page content based on the query parameter
if page == 'analysis':
    show_analysis()
elif page == 'relationship':
    show_relationship()
elif page == 'dataframe':
    show_dataframe()
else:
    show_home()

