import streamlit as st

# Set the page configuration
#st.set_page_config(page_title="Crop Analysis", page_icon="🌾")

# Custom CSS for styling and animation
custom_css = """
<style>
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.animated-heading {
    font-size: 3em;
    font-weight: bold;
    color: white;
    text-align: center;
    margin-top: 5%;
    animation: fadeIn 2s ease-in-out;
}

.animated-subheading {
    font-size: 1.5em;
    text-align: center;
    margin-top: 1%;
    animation: fadeIn 3s ease-in-out;
    background-color: #000; /* Black background */
    color: #0074D9; /* Blue text */
    padding: 10px;
    border-radius: 5px;
}

.animated-quote {
    font-size: 1.2em;
    color: #FFB6C1;
    text-align: center;
    margin-top: 2%;
    font-style: italic;
    animation: fadeIn 4s ease-in-out;
    background-color: #0074D9; /* Blue background */
    color: white; /* White text */
    padding: 5px 10px; /* Adjust padding as needed */
    border-radius: 5px;
}

body {
    background-image: url("{background_image}");
    background-size: cover;
    
    background-repeat: no-repeat;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    
    font-family: Arial, sans-serif;
}
</style>
"""


# Apply the custom CSS
#st.markdown(custom_css, unsafe_allow_html=True)

# HTML content for the heading, subheading, and quote
heading_text = """
<div class="animated-heading">
    Analysis on Crop Productions
</div>
"""

subheading_text = """
<div class="animated-subheading">
    Gain valuable insights about crop production
</div>
"""

quote_text = """
<div class="animated-quote">
    "Understanding crop insights is  essential!, because even plants need good vibes!"
</div>
"""

