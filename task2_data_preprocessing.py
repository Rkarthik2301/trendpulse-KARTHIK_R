import pandas as pd
from datetime import datetime

# Creating file name
date_string = datetime.now().strftime("%Y%m%d")
input_file = f"data/trends_{date_string}.json"

# Opening the json file as a dataframe
df = pd.read_json(input_file)
print(f"Loaded {len(df)} stories from {input_file}")

# Removing duplicate stories
df = df.drop_duplicates(subset="post_id")
print(f"\n After removing duplicates: {len(df)}")

# Removing rows where post_id, title, or score is missing
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Converting score and num_comments to numeric values
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce")

# Removing rows where score could not be converted
df = df.dropna(subset=["score"])

# Converting score and num_comments to integers
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Removing stories with scores less than 5
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Removing whitespaces
df["title"] = df["title"].str.strip()

# Saveing the dataframe as csv
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved {len(df)} rows to {output_file}")


# Print the number of stories in each category
print(f"\nStories per category:")
print(df["category"].value_counts())