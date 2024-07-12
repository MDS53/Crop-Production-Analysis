import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
from logger import logging


class show_relationships:
    def __init__(self):
        try:
            self.df=pd.read_csv('Crop Production data (1).csv')
            self.relationships_(self.df)
            logging.info(f"relationship.py's constructor ran successfully")
        except Exception as e:
            print(e)
            logging.exception(f"error {e} occured in relationship.py's constructor")
    
    def relationships_(self,df):
        try:
            self.df=df
            self.df.dropna(inplace=True)
            self.df['Crop_Year'] = self.df['Crop_Year'].astype(str)
            
            
            #1st plot
            self.d=self.df[['Crop','Area','Production']]
            st.title(" ")
            st.markdown('### Relationship Between Crop Area and Production Over selected crop  ')
            self.col1, self.col2,self.col3,self.col4,self.col5 = st.columns([5,4,3,2, 1])
            with self.col1:
                self.selected_crop = st.selectbox('Pick Crop', list(self.df['Crop'].unique()),key="1.1")
            self.chart = alt.Chart(self.d[self.d.Crop==self.selected_crop]).mark_circle().encode(
                    x='Area:Q',
                    y='Production:Q',
                    color=alt.Color('Crop:N', scale=alt.Scale(scheme='category10')),
                    tooltip=['Crop:N','Area:Q', 'Production:Q']
                ).properties(
                    width=800,
                    height=400,
                    title='Scatter Plot: Area vs Production corresponding to selected crop'
                )
            st.altair_chart(self.chart, use_container_width=True)
            self.col1, self.col2 = st.columns([3,9])
            with self.col1:
                st.write("This table corresponds to the visualization above.")
                st.dataframe(self.d[self.d.Crop==self.selected_crop][['Crop','Area','Production']])
            
            with self.col2:
                st.title("")
                st.write("### Insights ###")
                st.write("""
                    
                    You'll be able to...
                    - Understand how different crops require different amounts of space and resources to produce well.
                    - Recognize the impact of climate adaptability on the relationship between crop area and production.
                    - Appreciate the importance of resource utilization and agronomic practices in maximizing crop yields.
                    - See the significant role of soil fertility in determining how much area is needed for optimal production.
                    - Acknowledge the economic factors that influence how much land is dedicated to various crops.
                    - Realize the potential of technology to improve crop production efficiency, affecting the relationship between area and output.
                    
                    And 
                    
                    - You can cross-check or download the table to obtain exact values for detailed analysis.
                    - The table data will dynamically update based on your selected options.
                """)
                
                
            #2nd plot  
            self.d=self.df[['Crop','Crop_Year','Area','Production']]  
            st.title(" ")
            st.markdown('### Relationship Between Crop Area and Production Over selected Year  ')
            self.col1, self.col2,self.col3,self.col4,self.col5 = st.columns([5,4,3,2, 1])
            with self.col1:
                self.selected_crop_year = st.selectbox('Pick Year', list(self.df['Crop_Year'].unique()),key="2.1")
            self.chart = alt.Chart(self.d[self.d.Crop_Year==self.selected_crop_year]).mark_circle(color='Blue').encode(
                    x='Area:Q',
                    y='Production:Q',
                    color=alt.Color('Crop_Year:N', scale=alt.Scale(scheme='category10')),
                    tooltip=['Crop:N','Crop_Year:N','Area:Q', 'Production:Q']
                ).properties(
                    width=800,
                    height=400,
                    title='Scatter Plot: Area vs Production corresponding to selected Crop_Year'
                )
            st.altair_chart(self.chart, use_container_width=True)
            self.col1, self.col2 = st.columns([3,9])
            with self.col1:
                st.write("This table corresponds to the visualization above.")
                st.dataframe(self.d[self.d.Crop_Year==self.selected_crop_year][['Crop_Year','Area','Production']])
            
            with self.col2:
                st.write("### Insights ###")
                st.write("""
                    
                    you'll be able to...
                    - See how crop production varies across Area over years. 
                    - Identify in visualization that  how changes in crop area influence production outcomes. 
                    - take insights that which crop has less area but large production vice-versa , when you hover at the data points in scatter plot
                    - Identify optimal crop years for maximum yield based on cultivated area.
        
                    And
                    
                    - You can see The exact production values by hovering over the data points in the scatter plot above.
                    -By hovering over the data points in the scatter plot, you'll be able to see insights on which crops have small areas but high production, and vice versa.
                    
                    - You can cross-check or download the table to obtain exact values for detailed analysis.
                    - The table data will dynamically update based on your selected options.
                """)    
            
            
            
            
            #3rd plot 
            
            self.d=self.df[['Crop','Season','Area','Production']]
            st.title(" ")
            st.markdown('### Relationship between Area and Production with respect to Season  ')
            self.col1, self.col2,self.col3,self.col4,self.col5 = st.columns([5,4,3,2, 1])
            with self.col1:
                self.selected_season = st.selectbox('Pick Season', list(self.df['Season'].unique()),key="3.1")
            self.chart = alt.Chart(self.d[self.d.Season==self.selected_season]).mark_circle(color='Blue').encode(
                    x='Area:Q',
                    y='Production:Q',
                    color=alt.Color('Season:N', scale=alt.Scale(scheme='category10')),
                    tooltip=['Crop:N','Season:N','Area:Q', 'Production:Q']
                ).properties(
                    width=800,
                    height=400,
                    title='Scatter Plot: Area vs Production corresponding to selected Crop_Year'
                )
            st.altair_chart(self.chart, use_container_width=True)
            
            self.col1, self.col2 = st.columns([3,9])
            with self.col1:
                st.write("This table corresponds to the visualization above.")
                st.dataframe(self.d[self.d.Season==self.selected_season][['Crop','Area','Production']])
            
            with self.col2:
                
                st.write("### Insights ###")
                st.write("""
                    You'll be able to...
                    
                    - Notice that certain crops show a strong relationship between area and production depending on the season.
                    - Find that in some seasons, a smaller cultivation area can result in high production due to favorable growing conditions.
                    - Observe that during specific seasons, larger areas are necessary to achieve high production because of less favorable weather.
                    - See that seasonal variations can significantly impact the efficiency of crop production relative to the area cultivated.
                    - Recognize that crop yield efficiency in terms of area can fluctuate seasonally, highlighting the importance of selecting the right season for planting.
                    
                    And
                    
                    - You can see The exact production values by hovering over the data points in the scatter plot above.
                    -By hovering over the data points in the scatter plot, you'll be able to see insights on which crops have small areas but high production, and vice versa.
                    - You can cross-check or download the table to obtain exact values for detailed analysis.
                    - The table data will dynamically update based on your selected options.
                """)  
                
            
            #4th plot
            self.d=self.df[['Crop','District_Name','Area','Production']]
            st.title(" ")
            st.markdown('### Relationship between Area and Production in selected District    ')
            self.col1, self.col2,self.col3,self.col4,self.col5 = st.columns([5,4,3,2, 1])
            with self.col1:
                self.selected_district = st.selectbox('Select District ', list(self.df['District_Name'].unique()),key="4.1")
            self.chart = alt.Chart(self.d[self.d.District_Name==self.selected_district]).mark_circle(color='white').encode(
                    x='Area:Q',
                    y='Production:Q',
                    color=alt.Color('District_Name:N', scale=alt.Scale(scheme='category10')),
                    tooltip=['Crop:N','District_Name:N','Area:Q', 'Production:Q']
                ).properties(
                    width=800,
                    height=400,
                    title='Scatter Plot: Area vs Production corresponding to selected District'
                )
            st.altair_chart(self.chart, use_container_width=True)
            
            self.col1, self.col2 = st.columns([3,9])
            with self.col1:
                st.write("This table corresponds to the visualization above.")
                st.dataframe(self.d[self.d.District_Name==self.selected_district][['Crop','Area','Production']])
            
            with self.col2:
                
                st.write("### Insights ###")
                st.write("""
                    You'll be able to...
                    - Notice that certain districts exhibit a strong correlation between the cultivated area and production output.
                    - Observe that in some districts, even a small cultivated area can result in high production due to optimal local growing conditions.
                    - See that certain districts require larger areas to achieve high production, which could be due to soil quality or other regional factors.
                    - Find that the efficiency of crop production in terms of area can vary significantly across different districts.
                    - Recognize that specific districts may have unique agricultural practices that impact the relationship between area and production.
                    
                    And
                    
                    - You can see The exact production values by hovering over the data points in the scatter plot above.
                    - By hovering over the data points in the scatter plot, you'll be able to see Crop name as well 
                    - You can cross-check or download the table to obtain exact values for detailed analysis.
                    - The table data will dynamically update based on your selected options.
                """)  
                
                
                
            #5th plot
            self.d=self.df[['Crop','State_Name','Area','Production']]
            st.title(" ")
            st.markdown('### Relationship between Area and Production in selected State    ')
            self.col1, self.col2,self.col3,self.col4,self.col5 = st.columns([5,4,3,2, 1])
            with self.col1:
                self.selected_state = st.selectbox('Select State ', list(self.df['State_Name'].unique()),key="5.1")
            self.chart = alt.Chart(self.d[self.d.State_Name==self.selected_state]).mark_circle(color='white').encode(
                    x='Area:Q',
                    y='Production:Q',
                    color=alt.Color('State_Name:N', scale=alt.Scale(scheme='category10')),
                    tooltip=['Crop:N','State_Name:N','Area:Q', 'Production:Q']
                ).properties(
                    width=800,
                    height=400,
                    title='Scatter Plot: Area vs Production corresponding to selected District'
                )
            st.altair_chart(self.chart, use_container_width=True)
            
            self.col1, self.col2 = st.columns([3,9])
            with self.col1:
                st.write("This table corresponds to the visualization above.")
                st.dataframe(self.d[self.d.State_Name==self.selected_state][['Crop','Area','Production']])
            
            with self.col2:
                
                st.write("### Insights ###")
                st.write("""
                    You'll be able to...
                    - Notice that certain State exhibit a strong correlation between the cultivated area and production output.
                    - Observe that in some State, even a small cultivated area can result in high production due to optimal local growing conditions.
                    - See that certain State require larger areas to achieve high production, which could be due to soil quality or other regional factors.
                    - Find that the efficiency of crop production in terms of area can vary significantly across different State.
                    - Recognize that specific State may have unique agricultural practices that impact the relationship between area and production.
                    
                    And
                    
                    - You can see The exact production values by hovering over the data points in the scatter plot above.
                    - By hovering over the data points in the scatter plot, you'll be able to see Crop name as well 
                    - You can cross-check or download the table to obtain exact values for detailed analysis.
                    - The table data will dynamically update based on your selected options.
                """)
            logging.info("show_relationship() ran successfully")
        except Exception as e:
            logging.exception("Error {e} occured at relationship.py package in show_relationship()")  
            
            
        