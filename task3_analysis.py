import pandas as pd 
import numpy as np


class perform_analysis():
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = pd.read_csv(self.filepath)
        
    def head(self):
        return self.df.head() #Return the first 5 rows
    
    def shape(self):
        return (self.df.shape) #Return the shape of the dataframe
    
    def columns(self):
        return self.df.columns #Return the columns of the csv file
    
    def category_counts(self):
        category_counts = self.df["category"].value_counts() #Calculating No of stories in each category
        return category_counts
    
    def average_score(self):
        average_score = self.df["score"].mean() #Calculating Mean
        return average_score
    
    def median_score(self):
        median_score = self.df["score"].median() #Calculating Median
        return median_score
    
    def highest_score_story(self):
        highest_score_story_details = self.df.loc[self.df["score"].idxmax()] #Getting the data of the highest scoring story
        highest_score_story = highest_score_story_details["title"] # Getting the title of the story
        return highest_score_story
    
    def highest_score(self):
        highest_score = np.max(self.df["score"]) #Calculating highest score 
        return highest_score    
    
    def SCM(self):
        Average_Score_by_Category = self.df.groupby("category")["score"].mean() #Calculating Mean per category
        return Average_Score_by_Category
    
    def CCM(self):
        Average_comments_by_Category = self.df.groupby("category")["num_comments"].mean() #Calculating Comments per category
        return Average_comments_by_Category
if __name__ == "__main__":
    #reading the file
    filename = "data/trends_cleaned.csv"
    #Creating Object
    df = perform_analysis(filename)

    #Printing the values
    print(f"First 5 rows for inspection \n{df.head()}")
    print(f"\nshape:{df.shape()}") 
    print(f"\nColumns:\n{df.columns()}")
    print(f"\nNo of Stories in each category: \n{df.category_counts}")
    print(f"\n Average score = {df.average_score():.2f} ")
    print(f"\n Median of the score = {df.median_score():.2f} ")
    print(f"\nAverage score in each category :\n {df.SCM()}")
    print(f"\nAverage comments in each category :\n {df.CCM()}")
    print(f"\n Highest Score = {df.highest_score():.2f}")
    print(f"\n Story with the highest score is: \n {df.highest_score_story()}")