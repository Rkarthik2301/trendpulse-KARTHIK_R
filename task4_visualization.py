import pandas as pd
import matplotlib.pyplot as plt
import os
from task3_analysis import perform_analysis

filename = "data/trends_analysed.csv"
analysis = perform_analysis(filename)
df = analysis.df

os.makedirs("data/outputs", exist_ok=True)

#Chart 1
top_stories = df.nlargest(10, "score").copy()
short_titles = []
for title in top_stories["title"]:
    if len(title) > 50:
        title = title[:47] + "..."
    short_titles.append(title)

plt.figure(figsize=(10, 6))
plt.barh(
    short_titles,
    top_stories["score"]
)
plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(
    "data/outputs/chart1_top_stories.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
plt.close()

#Chart-2
category_counts = df["category"].value_counts()
plt.figure(figsize=(8, 5))
colors = [
    "tab:blue",
    "tab:orange",
    "tab:green",
    "tab:red",
    "tab:purple"
]

plt.bar(
    category_counts.index,
    category_counts.values,
    color=colors[:len(category_counts)]
)
plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.tight_layout()
plt.savefig(
    "data/outputs/chart2_categories.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
plt.close()

#Chart-3
popular = df[df["is_popular"] == True]
non_popular = df[df["is_popular"] == False]
plt.figure(figsize=(8, 5))
plt.scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular"
)
plt.scatter(
    non_popular["score"],
    non_popular["num_comments"],
    label="Not Popular"
)
plt.title("Score vs Number of Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.legend()
plt.tight_layout()
plt.savefig(
    "data/outputs/chart3_scatter.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
plt.close()

#Dashboard
fig, axes = plt.subplots(
    2,
    2,
    figsize=(16, 10)
)
#Chart-1 in dashboard
axes[0, 0].barh(
    short_titles,
    top_stories["score"]
)
axes[0, 0].set_title("Top 10 Stories by Score")
axes[0, 0].set_xlabel("Score")
axes[0, 0].set_ylabel("Story")

#Chart-2 in dashboard
axes[0, 1].bar(
    category_counts.index,
    category_counts.values,
    color=colors[:len(category_counts)]
)
axes[0, 1].set_title("Stories per Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Number of Stories")

#Chart-3 in dashboard
axes[1, 0].scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular"
)
axes[1, 0].scatter(
    non_popular["score"],
    non_popular["num_comments"],
    label="Not Popular"
)
axes[1, 0].set_title("Score vs Number of Comments")
axes[1, 0].set_xlabel("Score")
axes[1, 0].set_ylabel("Number of Comments")
axes[1, 0].legend()

#Removing the 4th position
axes[1, 1].axis("off")

# Overall dashboard title
fig.suptitle(
    "TrendPulse: What's Actually Trending Right Now",
    fontsize=18
)

plt.savefig(
    "data/outputs/dashboard.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
plt.close()

print("\nAll charts created successfully!")
print("Charts saved in the outputs/ folder.")