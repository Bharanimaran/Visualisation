# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:30:43 2023

@author: Bharanidharan Thirumaran
"""

#import modules
import matplotlib.pyplot as plt
import pandas as pd

#Read data
wc_matches = pd.read_csv("./data.csv")
wc_matches 

# Line Plot Graph
#Create funtion for line plot
def create_line_plot(wc_matches):
    
    """
    Create a line graph that displays Teams 1 and 2's probability scores.

    Variables:
    World Cup match data is contained in the DataFrame wc_matches (DataFrame).
    
    """ 
    
    # Select the first five countries in the "team1" and "Proj_score" column
    first_team= wc_matches['team1'].head(5)
    probability_score_1 = wc_matches['prob1'].head(5)  
    second_team= wc_matches['team2'].head(5)
    probability_score_2 = wc_matches['prob2'].head(5)
    # Create a line plot
    plt.figure(figsize=(15, 8))  
    plt.plot(first_team, probability_score_1)
    plt.plot(second_team,probability_score_2)
    plt.title('Probability Score for Team 1 and Team2')
    plt.xlabel('Teams')
    plt.ylabel('Probability')
    plt.legend(['probability_score_team1','probability_score_team2'])
    plt.grid()
    plt.show()
# Call the function to create Line plot    
create_line_plot(wc_matches)

 # Scatter Plot 
#Create function for scatter plot
def create_scatter_plot(wc_matches):
    
    """
    Generate a scatter plot showing the projection scores for Team 1 and Team 2.

    Parameters:
    World Cup match data is contained in the DataFrame wc_matches (DataFrame).
    
    """
    
    # Select the first Eight countries in the "team1","team2" and "Proj_score1","Proj_score2" column
    First_team = wc_matches['team1'].head(8)
    Second_team =wc_matches['team2'].head(8)
    proj_score1 = wc_matches['proj_score1'].head(8)
    proj_score2 = wc_matches['proj_score2'].head(8)
    # Create a scatter plot
    Proj1_colour = 'Blue'
    Proj2_colour = 'Red'
    plt.figure(figsize=(15, 8))
    plt.scatter(First_team, proj_score1,c=Proj1_colour)
    plt.scatter(Second_team, proj_score2,c=Proj2_colour)
    plt.title('projection score for Team1 and Team2')
    plt.xlabel('Teams')
    plt.ylabel('projection')
    plt.legend(['Projection_score_team1','Projection_score_team2'])
    plt.show()

# Call the function to create scatter plot
create_scatter_plot(wc_matches)

# Bar_chart

# Function to create bar chart
def create_bar_chart(wc_matches):
    
    """
    Create a bar graph that displays the Probtie scores of the initial five teams of Team 1.

    Variables:
    World Cup match data is contained in the DataFrame wc_matches (DataFrame).\
        
    """
    
    # Select the first five countries in the "team1" and "Probtie" column
    teams = wc_matches['team1'].head(5)
    probtie = wc_matches['probtie'].head(5)
    #Create Bar plot
    plt.figure(figsize=(15, 8))
    plt.bar(teams, probtie, color='Skyblue')
    plt.xlabel('Teams')
    plt.ylabel('Probtie')
    plt.title('Probtie score for Team 1')
    plt.legend(['Probtie_score'])
    plt.show()
# Call the function to create bar chart
create_bar_chart(wc_matches)





