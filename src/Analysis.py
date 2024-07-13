import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
from logger import logging


# Define the Analysis page contents
class show_analysis__:
    def __init__(self):
        try:
            
            self.df=pd.read_csv("Crop Production data (1).csv")
            #print(self.df.head())
            self.df.dropna(inplace=True)
            self.df['Crop_Year'] = self.df['Crop_Year'].astype(str)
            self.show_analysis_Bars(self.df)
            self.show_analysis_Scatters(self.df)
            logging.info("Constructor from show_analysis__ class ran successfully")
        except Exception as e:
            logging.error(f"Error {e} occured in show_analysis__ class from Analysis.py")


    def show_analysis_Bars(self,df):
        
        try:
            #1st plot
            self.df=df
            st.title(" ")
            st.markdown('### Crop Availability and Production in the Chosen District  ')
    #("Hello from the Analysis page!")
            self.col1, self.col2,self.col3,self.col4,self.col5 = st.columns([5,4,3,2, 1])
            with self.col1:
                self.selected_district = st.selectbox('Pick District', sorted(list(self.df['District_Name'].unique())))
            #st.write(self.selected_district)
            self.d=self.df.groupby(['District_Name','Crop'])['Production'].mean().sort_values(ascending=False).reset_index()
            self.bar_chart = alt.Chart(self.d[self.d['District_Name']==self.selected_district]).mark_bar(color='yellow').encode(x=alt.X('Crop', axis=alt.Axis(title='Crop Name')),y=alt.Y('Production', axis=alt.Axis(title='Production')),tooltip=[alt.Tooltip('Crop', title='Crop'),alt.Tooltip('District_Name', title='District'), alt.Tooltip('Production', title='Production')]).properties(width=2000,height=500,title="Production by District").configure_mark(tooltip=alt.TooltipContent('encoding')).interactive()
            
            # Display the chart in Streamlit
            st.altair_chart(self.bar_chart, use_container_width=True)
                # Sample dataframe
            
            
            
            self.col1, self.col2= st.columns([3,8])  # Adjust the ratio as needed
            
            with self.col1:
                st.write("This table corresponds to the visualization above.")
                st.dataframe(self.d[self.d['District_Name']==self.selected_district])
            
            with self.col2:
                st.title("")
                st.write("### Insights ###")
                st.write("""
                    
                    - You'll discover which crops dominate production in each district based on the selected data.
                    - You can see the exact production values by hovering over the bars in the chart above.
                    - And you can cross-check or download the table to obtain exact values for detailed analysis.
                    - The table data will dynamically update based on your selected options.
                """)
                #st.title("Analysis Page")
                

                
            #2nd plot
            st.title(" ")
            st.markdown('### Crop Production Analysis: Yearly Trends for Selected Crop  ')
            self.col1, self.col2,self.col3,self.col4,self.col5 = st.columns([5,4,3,2, 1])
            
            with self.col1:
                self.selected_crop = st.selectbox('Pick Crop', list(self.df['Crop'].unique()))
            #st.write(self.selected_crop)
            #self.selected_year = st.selectbox('Pick Year', list(self.df['Crop_Year'].unique()))
            #st.write(self.selected_year)
            #st.radio('Pick Year', list(self.df['Crop_Year'].unique()))
            self.d=self.df.groupby(['Crop','Crop_Year'])['Production'].mean().sort_values(ascending=False).reset_index()
            self.bar_chart = alt.Chart(self.d[self.d['Crop']==self.selected_crop].head(200)).mark_bar(color='purple').encode(x=alt.Y('Crop_Year', axis=alt.Axis(title='Crop_Year')),y=alt.X('Production', axis=alt.Axis(title='Production')),tooltip=[alt.Tooltip('Crop', title='Crop'),alt.Tooltip('Production', title='Production'), alt.Tooltip('Crop_Year', title='Crop_Year')]).properties(width=200,height=800,title=" Yearly Crop Production Insights").configure_mark(tooltip=alt.TooltipContent('encoding')).interactive()
            
            # Display the chart in Streamlit
            st.altair_chart(self.bar_chart, use_container_width=True)
                # Sample dataframe
            self.col1, self.col2= st.columns([2,8])  # Adjust the ratio as needed
            
            with self.col1:
                st.write("This table corresponds to the visualization above.")
                st.dataframe(self.d)
            
            with self.col2:
                st.title("")
                st.write("### Insights ###")
                st.write("""
                    
                    - You'll be able to see the yearly trends in crop production for the selected crop.
                    - Easily compare production trends year-on-year for informed decision-making.
                    - You can see the exact production values by hovering over the bars in the chart above.
                    - And you can cross-check or download the table to obtain exact values for detailed analysis.
                    - The table data will dynamically update based on your selected options.
                """)
        
        
            # 3rd plot
            st.title(" ")
            st.markdown('### Crop Production Trends Based on Selected Crop and State ### ')
            self.col1, self.col2,self.col3,self.col4,self.col5 = st.columns([5,4,3,2, 1])
            with self.col1:
                self.selected_State = st.selectbox('Pick State', list(self.df['State_Name'].unique()),key="3.1")
        # st.write(self.selected_State)
            with self.col2:
                self.selected_crop = st.selectbox('Pick Crop', list(self.df['Crop'].unique()),key=3.2)
            #st.write(self.selected_crop)
            #self.selected_year = st.selectbox('Pick Year', list(self.df['Crop_Year'].unique()))
            #st.write(self.selected_year)
            #st.radio('Pick Year', list(self.df['Crop_Year'].unique()))
            self.d=df.groupby(['State_Name','Crop','Crop_Year']).agg({'Production':'mean'}).sort_values(by=['Production'],ascending=False).reset_index()
            self.bar_chart = alt.Chart(self.d[(self.d['Crop']==self.selected_crop) & (self.d['State_Name']==self.selected_State)].head(200)).mark_bar().encode(x=alt.Y('Crop_Year', axis=alt.Axis(title='Crop_Year')),y=alt.X('Production', axis=alt.Axis(title='Production')),tooltip=[alt.Tooltip('Crop', title='Crop'),alt.Tooltip('Production', title='Production'), alt.Tooltip('Crop_Year', title='Crop_Year')]).properties(width=200,height=800,title=" Production by Crop").configure_mark(tooltip=alt.TooltipContent('encoding')).interactive()
            
            # Display the chart in Streamlit
            st.altair_chart(self.bar_chart, use_container_width=True)
                # Sample dataframe
            self.col1, self.col2 = st.columns([3,8])  # Adjust the ratio as needed
            
            with self.col1:
                st.write("This table corresponds to the visualization above.")
                st.dataframe(self.d)
            
            with self.col2:
                st.title("")
                st.write("### Insights ###")
                st.write("""
                    - You'll be able to see trends and patterns for the selected crop and state over the years. 
                    - You'll discover which years had the highest and lowest production. 
                    - You'll be able to compare production values across different states for the same crop. 
                    - You'll gain a deeper understanding of how production has evolved over time and identify key factors influencing these changes.
                    - You can see the exact production values by hovering over the bars in the chart above.
                    - And you can cross-check or download the table to obtain exact values for detailed analysis.
                    - The table data will dynamically update based on your selected options.
                """)


        # 4th plot
            st.title(" ")
            st.markdown('### State-wise Crop Production: Detailed Analysis ### ')
            self.col1, self.col2,self.col3,self.col4,self.col5 = st.columns([5,4,3,2, 1])
            with self.col1:
                self.selected_State = st.selectbox('Pick State', list(self.df['State_Name'].unique()),key="4.1")
            st.write(self.selected_State)
            st.write(self.selected_crop)
            #self.selected_year = st.selectbox('Pick Year', list(self.df['Crop_Year'].unique()))
            #st.write(self.selected_year)
            #st.radio('Pick Year', list(self.df['Crop_Year'].unique()))
            self.d=df.groupby(['State_Name','Crop','Crop_Year']).agg({'Production':'mean'}).sort_values(by=['Production'],ascending=False).reset_index()
            self.bar_chart = alt.Chart(self.d[(self.d['State_Name']==self.selected_State)].head(200)).mark_bar().encode(x=alt.Y('Crop', axis=alt.Axis(title='Crop')),y=alt.X('Production', axis=alt.Axis(title='Production')),tooltip=[alt.Tooltip('Crop', title='Crop'),alt.Tooltip('Production', title='Production'), alt.Tooltip('Crop_Year', title='Crop_Year')]).properties(width=200,height=800,title=" Production by Crop").configure_mark(tooltip=alt.TooltipContent('encoding')).interactive()
            
            # Display the chart in Streamlit
            st.altair_chart(self.bar_chart, use_container_width=True)
                # Sample dataframe
            self.col1, self.col2,self.col3,self.col4,self.col5 = st.columns([5,4,3,2, 1])  # Adjust the ratio as needed
            
            with self.col1:
                st.write("This table corresponds to the visualization above.")
                st.dataframe(self.d)
            
            with self.col2:
                st.title("")
                st.write("### Insights ###")
                st.write("""
                    - You can able to Explore Crop  Production Trends State-wise.                    
                    - You can identify which crops are  most productive in each state.
                    - You can see the exact production values by hovering over the bars in the chart above.
                    - And you can cross-check or download the table to obtain exact values for detailed analysis.
                    - The table data will dynamically update based on your selected options.
                    
                """)
                
                
                
            #5th column 
            st.title(" ")
            st.markdown('### Crop Production Analysis by Season ### ')
            self.col1, self.col2,self.col3 = st.columns([5,3,5])
            self.d=self.df.groupby(['Season','Crop'])['Production'].mean().sort_values(ascending=False).reset_index()
        
            with self.col1:
                self.selected_Crop = st.selectbox('Pick Crop', list(self.df['Crop'].unique()),key="5.1")
                self.d=self.d[self.d.Crop==self.selected_Crop]    
                self.season_production = self.d.groupby('Season')['Production'].sum().reset_index()
                # Create a pie chart-like visualization using Arcs in Altair
                chart = alt.Chart(self.season_production).mark_arc().encode(
                    color=alt.Color('Season:N', scale=alt.Scale(scheme='viridis')),  # Gradient color scale (Viridis)
                    tooltip=['Season:N', 'Production:Q'],
                    angle='Production:Q'
                ).properties(
                    width=400,
                    height=400,
                    title=f'Production by Season for {self.selected_Crop}'
                ).configure_mark(
                    tooltip=alt.TooltipContent('encoding')
                )

                # Display the chart in Streamlit
                st.altair_chart(chart, use_container_width=True)
            with self.col2:
                st.write("This table corresponds to the visualization above.")
                st.dataframe(self.d)
            
            with self.col3:
                st.title("")
                st.write("### Insights ###")
                st.write("""
                    - You'll be able to see which crops are most productive in different seasons. 
                    - You'll be able to compare crop production across different seasons to identify trends and patterns. 
                    - Interactive charts and graphs to visualize the relationship between crop production and seasons.
                    - You can see the exact production values by hovering over the slices in the Pie chart above.
                    - And you can cross-check or download the table to obtain exact values for detailed analysis.
                    - The table data will dynamically update based on your selected options.
                """)
            logging.info("show_analysis_Bars() from Analysis package ran successfully ")
            
        except Exception as e:
            logging.error(f"Error {e} occured in show_analysis_Bars() from show_analysis__ class from Analysis.py")
            
            
    def show_analysis_Scatters(self,df):
        
        
        try:
            
            self.df=df
            self.d=df.groupby(['Crop_Year','State_Name'])[['Area','Production']].mean().sort_values(by=['Production'],ascending=False).reset_index()
            
            #1st plot
            st.title(" ")
            st.markdown('### Crop Analysis by Area and Production on Selected State ### ')
            self.col1, self.col2,self.col3= st.columns([7,3,6])
            
            
            with self.col1:
                self.selected_State = st.selectbox('Select State_Name', list(self.df['State_Name'].unique()),key="1.1.1")
                self.chart = alt.Chart(self.d[self.d.State_Name==self.selected_State]).mark_circle().encode(
                    x='Area:Q',
                    y='Production:Q',
                    color=alt.Color('Crop_Year:N', scale=alt.Scale(scheme='category10')),
                    tooltip=['Crop_Year:N','Area:Q', 'Production:Q']
                ).properties(
                    width=800,
                    height=400,
                    title='Scatter Plot: Area vs Production'
                )
                st.altair_chart(self.chart, use_container_width=True)
            with self.col2:
                st.write("This table corresponds to the visualization above.")
                st.dataframe(self.d[self.d.State_Name==self.selected_State][['Crop_Year','Area','Production']])
            
            with self.col3:
                st.title("")
                st.write("### Insights ###")
                st.write("""
                    - You can Analyze the production trends of the selected crop across different years.
                    - You can Examine how the area dedicated to the selected crop has changed over the years. 
                    - You can Understand the relationship between crop area and production yield. 
                    - You can able to see  how crop production varies annually and its relation to cultivated area.Identify the years with the highest and lowest production rates.
                    - Compare the production and area data across multiple years to identify patterns and anomalies.Use the insights gained to make informed decisions about crop planning and resource allocation.
                    - You can see the exact production values by hovering over the data points in the chart above.
                    - And you can cross-check or download the table to obtain exact values for detailed analysis.
                    - The table data will dynamically update based on your selected options.
                """)
            
            
            
            #2nd plot.
            st.title(" ")
            st.markdown('### Understanding Crop Production Patterns over Crop Year and its Area ### ')
            
            self.col1, self.col2,self.col3= st.columns([7,3,6])
            self.d=self.df.groupby(['Crop','Crop_Year'])[['Area','Production']].mean().sort_values(by=['Production'],ascending=False).reset_index()
            
            with self.col1:
                self.selected_Crop = st.selectbox('Pick Crop', list(self.df['Crop'].unique()),key="2.1.1")
                self.chart = alt.Chart(self.d[self.d.Crop==self.selected_Crop]).mark_circle().encode(
                    x='Area:Q',
                    y='Production:Q',
                    color=alt.Color('Crop_Year:N', scale=alt.Scale(scheme='category10')),
                    tooltip=['Crop_Year:N','Area:Q', 'Production:Q']
                ).properties(
                    width=800,
                    height=400,
                    title='Scatter Plot: Area vs Production'
                )
                st.altair_chart(self.chart, use_container_width=True)
            with self.col2:
                st.write("This table corresponds to the visualization above.")
                st.dataframe(self.d[self.d.Crop==self.selected_Crop][['Crop_Year','Area','Production']])
            
            with self.col3:
                st.title("")
                st.write("### Insights ###")
                st.write("""
                    - You can see how crop production varies across Area over years. 
                    - You can identify in visualization that  how changes in crop area influence production outcomes. 
                    - You'll be able to Identify optimal crop years for maximum yield based on cultivated area.
                    - You can see the exact production values by hovering over the data points in the scatter plot above.
                    - And you can cross-check or download the table to obtain exact values for detailed analysis.
                    - The table data will dynamically update based on your selected options.
                """)

            
            #3rd plot
            
            st.title(" ")
            st.markdown('### Exploring Crop Diversity, Area, and Yield in Selected District s ### ')
            self.d=self.df.groupby(['Crop','District_Name'])[['Area','Production']].mean().sort_values(by=['Production'],ascending=False).reset_index()
            
            
            self.selected_district = st.selectbox('Select District', list(self.df['District_Name'].unique()),key="3.1.1")
            self.chart = alt.Chart(self.d[self.d.District_Name==self.selected_district]).mark_circle().encode(
                x='Area:Q',
                y='Production:Q',
                color=alt.Color('Crop:N', scale=alt.Scale(scheme='category10')),
                tooltip=['Crop:N','Area:Q', 'Production:Q']
            ).properties(
                width=900,
                height=600,
                title='Scatter Plot: Area vs Production'
            )
            st.altair_chart(self.chart, use_container_width=True)
            self.col3,self.col4= st.columns([3,9])
            with self.col3:
                st.write("This table corresponds to the visualization above.")
                st.dataframe(self.d[self.d.District_Name==self.selected_district][['Crop','Area','Production']])
            with self.col4:
                st.write("### Insights ###")
                st.write("""
                    - You can Explore the variety of crops grown within each district and their respective areas under cultivation.Analyze the production levels of various crops within specific districts, providing insights into yield variations.
                    - And you can assess how crop production and cultivated areas vary spatially across districts, highlighting regional agricultural patterns.
                    - Compare crop production efficiencies and patterns between different districts, identifying areas for improvement.
                    - You can see the exact production values by hovering over the data points in the scatter plot above.
                    - And you can cross-check or download the table to obtain exact values for detailed analysis.
                    
                """)
            
            
            #4th plot
            
            st.title(" ")
            st.markdown('### Understanding Crop Production Patterns over Crop Year and its Area ### ')
            self.f={}
            self.f=dict(self.f)
            for self.i in self.df.State_Name.unique():
                self.l=self.df[self.df.State_Name==self.i]['District_Name']
                self.l=list(self.l)
                self.l=set(self.l)
                self.f[self.i]=self.l
            self.d=self.df.groupby(['State_Name','District_Name','Crop_Year','Crop'])[['Area','Production']].mean().sort_values(by=['Production'],ascending=False).reset_index()
            self.col1, self.col2,self.col3,self.col4= st.columns([4,3,2, 1])
            with self.col1:
                self.selected_State = st.selectbox('Select State_Name', list(self.df['State_Name'].unique()),key="4.1.1")
                
            with self.col2:  
                self.crop_options = [None] + list(self.f[self.selected_State])
                self.selected_district = st.selectbox('Select District',self.crop_options,key="4.2.1")
            
            with self.col3:
                self.crop_options = [None] + sorted(list(self.df['Crop_Year'].unique()))
                self.selected_year = st.selectbox('Select Year', self.crop_options,key="4.3.1")
            st.write(self.selected_district)
            self.d=self.df.groupby(['State_Name','District_Name','Crop_Year','Crop'])[['Area','Production']].mean().sort_values(by=['Production'],ascending=False).reset_index()    

            
            if self.selected_district is None:
                if self.selected_year is None:    
                    self.chart = alt.Chart(self.d[(self.d.State_Name==self.selected_State)]).mark_circle().encode(
                        x='Area:Q',
                        y='Production:Q',
                        color=alt.Color('Crop:N', scale=alt.Scale(scheme='category10')),
                        tooltip=['Crop:N','Area:Q', 'Production:Q']
                    ).properties(
                        width=800,
                        height=700,
                        title='Scatter Plot: Area vs Production'
                    )
                    st.altair_chart(self.chart, use_container_width=True)
                else:
                    self.chart = alt.Chart(self.d[(self.d.State_Name==self.selected_State) & (self.d.Crop_Year==self.selected_year)]).mark_circle().encode(
                        x='Area:Q',
                        y='Production:Q',
                        color=alt.Color('Crop:N', scale=alt.Scale(scheme='category10')),
                        tooltip=['Crop:N','Area:Q', 'Production:Q']
                    ).properties(
                        width=800,
                        height=700,
                        title='Scatter Plot: Area vs Production'
                    )
                    st.altair_chart(self.chart, use_container_width=True)
            else:
                if self.selected_year is None:  
                    self.chart = alt.Chart(self.d[(self.d.State_Name==self.selected_State) & (self.d.District_Name==self.selected_district)]).mark_circle().encode(
                        x='Area:Q',
                        y='Production:Q',
                        color=alt.Color('Crop:N', scale=alt.Scale(scheme='category10')),
                        tooltip=['Crop:N','Area:Q', 'Production:Q']
                    ).properties(
                        width=800,
                        height=700,
                        title='Scatter Plot: Area vs Production'
                    )
                    st.altair_chart(self.chart, use_container_width=True)
                else:
                    self.chart = alt.Chart(self.d[(self.d.State_Name==self.selected_State) & (self.d.District_Name==self.selected_district)& (self.d.Crop_Year==self.selected_year)]).mark_circle().encode(
                        x='Area:Q',
                        y='Production:Q',
                        color=alt.Color('Crop:N', scale=alt.Scale(scheme='category10')),
                        tooltip=['Crop:N','Area:Q', 'Production:Q']
                    ).properties(
                        width=800,
                        height=700,
                        title='Scatter Plot: Area vs Production'
                    )
                    st.altair_chart(self.chart, use_container_width=True)
            self.col1, self.col2= st.columns([3,9])                    
            with self.col1:
                st.write("This table corresponds to the visualization above.")
                st.dataframe(self.d[self.d.State_Name==self.selected_State][['Crop','Area','Production']])
            
            with self.col2:
                st.title("")
                st.write("### Insights ###")
                st.write("""
                    - You can Explore crop data specific to your chosen State and District, focusing on the selected Crop Year.View crop details only for districts that fall within your selected State, ensuring relevant insights.
                    - You'll be Analyzing how Crop Name, Area, and Production vary across different Crop Years in the selected State and District.Gain insights into key metrics such as Crop Name, Area under cultivation, and Production levels.
                    - When selecting a state without specifying a district, the analysis will encompass all districts within the chosen state. Only districts that belong to the selected state will be available for selection
                    - You can see the exact production values by hovering over the data points in the scatter plot above.
                    - And you can cross-check or download the table to obtain exact values for detailed analysis.
                    - The table data will dynamically update based on your selected options.
                """)
            st.write(" ## Note : Here you can see 'None' option in selecting options, it  means selecting all options  ##")
            logging.info("show_analysis_Scatters() from Analysis package ran successfully ")
            
        except Exception as e:
            logging.error(f"Error {e} occured in show_analysis_Scatters() from show_analysis__ class from Analysis.py")
        
        
        
        
        
        
            


