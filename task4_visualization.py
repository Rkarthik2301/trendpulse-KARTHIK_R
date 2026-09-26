import matplotlib.pyplot as plt
import numpy as np
from task3_analysis import perform_analysis as pa

df = pa("data/trends_cleaned.csv")

#Bar chart for category count
bar1_x = df.category_counts().index.tolist()
bar1_y = df.category_counts().values.tolist()
plt.figure()
plt.bar(bar1_x,bar1_y)
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Number of stories per category")
plt.show()

# Average score by category
bar2_x = df.SCM().index.tolist()
bar2_y = df.SCM().values.tolist()
plt.figure()
plt.bar(bar2_x,bar2_y)
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Average story scores per category")
plt.show()

# Average comments by category
bar3_x = df.CCM().index.tolist()
bar3_y = df.CCM().values.tolist()
plt.figure()
plt.bar(bar3_x,bar3_y)
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Average comments per category")
plt.show()

# Score vs Comments 
plt.scatter(
    df.df["score"],
    df.df["num_comments"]
)
plt.title("Score vs Number of Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.show()

# Top 10 stories by score
top_10 = df.df.nlargest(10, "score")
plt.figure(figsize=(10, 6))
plt.barh(
    top_10["title"],
    top_10["score"]
)
plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


