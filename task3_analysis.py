import pandas as pd 
import numpy as np


class perform_analysis():
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = pd.read_csv(self.filepath)
        
    def head(self):
        return self.df.head()

    def shape(self):
        return self.df.shape

    def average_score(self):
        return self.df["score"].mean()

    def average_comments(self):
        return self.df["num_comments"].mean()

    def mean_score(self):
        scores = self.df["score"].to_numpy()
        return np.mean(scores)

    def median_score(self):
        scores = self.df["score"].to_numpy()
        return np.median(scores)

    def std_score(self):
        scores = self.df["score"].to_numpy()
        return np.std(scores)

    def highest_score(self):
        scores = self.df["score"].to_numpy()
        return np.max(scores)

    def lowest_score(self):
        scores = self.df["score"].to_numpy()
        return np.min(scores)

    def most_common_category(self):
        categories = self.df["category"].to_numpy()
        unique_categories, counts = np.unique(categories,return_counts=True        )
        index = np.argmax(counts)
        return unique_categories[index], counts[index]

    def most_commented_story(self):
        index = np.argmax(self.df["num_comments"].to_numpy())
        story = self.df.iloc[index]
        return story["title"], story["num_comments"]

    def add_new_columns(self):
        self.df["engagement"] = (
            self.df["num_comments"] /
            (self.df["score"] + 1)
        )
        average_score = self.average_score()
        self.df["is_popular"] = (
            self.df["score"] > average_score
        )

if __name__ == "__main__":
    input_file = "data/trends_clean.csv"
    output_file = "data/trends_analysed.csv"
    analysis = perform_analysis(input_file)
    
    print(f"Loaded data: {analysis.shape()}")
    print("\nFirst 5 rows:")
    print(analysis.head())
    print(f"\nAverage score : {analysis.average_score():.2f}")
    print(f"Average comments: {analysis.average_comments():.2f}")
    print("\n--- NumPy Stats ---")
    print(f"Mean score   : {analysis.mean_score():.2f}")
    print(f"Median score : {analysis.median_score():.2f}")
    print(f"Std deviation: {analysis.std_score():.2f}")
    print(f"Max score    : {analysis.highest_score()}")
    print(f"Min score : {analysis.lowest_score()}")
    
    category, count = analysis.most_common_category()
    print(f"\nMost stories in: {category} ({count} stories)")

    title, comments = analysis.most_commented_story()
    print(f'\nMost commented story: {title} — {comments} comments')

    analysis.add_new_columns()
    print("\nNew columns added:")
    print(f"engagement \n", analysis.df["engagement"].head())
    print(f"is_popular\n", analysis.df["is_popular"].head())
    
    analysis.df.to_csv(output_file,index=False)
    print(f"\nSaved to {output_file}")