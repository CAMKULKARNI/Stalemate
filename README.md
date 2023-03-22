# Stalemate

This project deals with the analysis of various games of chess and answers some simple questions based on the analysis.
Lot of information is contained within a single chess game, let alone a full dataset of multiple games. It is 
primarily a game of patterns, and data science is all about detecting patterns in data, which is why chess has 
been one of the most invested in areas of AI in the past. In this project we proceed to analyze the various 
variables present in a chess game and the unknown relations and interpretations which exist between them.

We first perform some exploratory data analysis on the multiple chess games by 
describing the various variables present in the dataset. We clean the dataset of missing data by examining and 
imputing and remove all unwanted observations not required. That is followed by classifying the variables into 
different categories and visualising the values.  
  
It is then normalised using z-statistics for easy manipulation and comparison of data followed by hypothesis 
testing. In hypothesis testing we make several possible predictions and check whether they are supported or 
rejected by using p-value tests. Finally, we finish with correlation by graphing various variables and checking 
for their shapes and obtaining inferences.


The original dataset has been taken from https://www.kaggle.com/datasnaek/chess. It contains information of 
about 20000 games of chess collected from a selection of users on the site Lichess.org. It consists of 16 columns 
initially and over 20000 rows. Here is the list of the columns.  
 
• Id – Unique id generated for every chess game  
• Rated – Whether the game was a rated game where if a player wins or loses it improves or decreases the profile rank.  
• Start time (Omitted) – The time at which the game started  
• End time (Omitted) – The time at which the game ended  
• Game time – The duration of the game obtained by subtracting start time from end time  
• Turns – Number of turns played in the game    
• Victory_status – The result of the game whether it was checkmate, draw, the players gave up or time ran out   
• Winner – The winner of the game  
• Increment_code – The increment code of the game. In chess increment code is of the format X+Y where X is time in minutes for a player to make the first move and Y is the increment in seconds added to each move’s time if a move is played within Y seconds  
• White_id – The player id of white   
• White_rating – Rank or rating of white’s player  
• Black_id – The player id of black   
• Black_rating – Rank or rating of black’s player  
• Moves – List of moves played in the game in standard chess notation  
• Opening_eco – Standardised code given for every game’s opening move  
• Opening_name – Name of the opening move  
• Opening_ply – Number of moves in the opening phase

The files can be viewed in the following order:
1. nanValuesCreation.ipynb - This notebook contains the code for creating the nan values in the dataset. If you do not want to insert nan values randomly in the dataset this file can be overlooked

2. handlingNullValues.ipynb - This notebook contains the code for handling the null values in the dataset.

3. handlingOutliers.ipynb - This notebook contains the code for handling the outliers in the dataset.

4. normalization.ipynb - This notebook contains the code for normalizing the dataset.

5. correlations.ipynb - This notebook contains the code for correlation analysis. How the variables are related with each other, is depicted graphically in this file.

6. visualizations.ipynb and columnVariableTypes.ipynb - This notebook contains the code for visualizing the data.


For more information, please look at the Project Report.pdf and Project Presentation.pdf
