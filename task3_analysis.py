import pandas as pd 
import numpy as np

#reading the file
filename = "data/trends_cleaned.csv"
df = pd.read_csv(filename)

print(df.head()) #Printing the first 5 rows
print("\n shape:",df.shape) #Printing the shape of the dataframe
print("Columns:\n",df.columns) #Printing the columns of the csv file

category_counts = df["category"].value_counts() #Calculating No of stories in each category

average_score = df["score"].mean() #Calculating Mean

median_score = df["score"].median() #Calculating Median

highest_score = np.max(df["score"]) #Calculating highest score 

highest_score_story_details = df.loc[df["score"].idxmax()] #Getting the data of the highest scoring story

highest_score_story = highest_score_story_details["title"] # Getting the title of the story

Average_Score_by_Category = df.groupby("category")["score"].mean() #Calculating Mean per category
Average_num_comments_by_Category = df.groupby("category")["num_comments"].mean() #Calculating Comments per category

#Printing all the calculated values
print("No of Stories in each category: \n", category_counts)
print(f"\n Average score = {average_score:.2f} ")
print(f"\n Median of the score = {median_score:.2f} ")
print(f"\n Highest Score = {highest_score:.2f}")
print(f"\nAverage score in each category :\n {Average_Score_by_Category}")
print(f"\nAverage comments in each category :\n {Average_num_comments_by_Category}")
print(f"\n Story with the highest score is: \n {highest_score_story}")