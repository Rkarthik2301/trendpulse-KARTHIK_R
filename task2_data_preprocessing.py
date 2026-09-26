import json
import os
import csv
from datetime import datetime
date_string = datetime.now().strftime("%Y%m%d")
filename = f"data/trends_{date_string}.json"

if not os.path.exists(filename):
    print(f"{filename} does not exist")
    exit()

cleaned_stories = []

with open(filename, "r", encoding="utf-8") as file :
    stories = json.load(file)
   
required_fields =  [
    "post_id",
    "title",
    "category",
    "score",
    "num_comments",
    "author",
    "collected_at"
]  
    
for story in stories:
    if not all(field in story for field in required_fields):
        continue
    title = story["title"].strip()
    if title == "" :
        continue
    score = story.get("score", 0)
    num_comments = story.get("num_comments",0)

    cleaned_story = {
    "post_id": story["post_id"],
    "title": title,
    "category": story["category"],
    "score": score,
    "num_comments": num_comments,
    "author": story["author"],
    "collected_at": story["collected_at"]
    
    }

    cleaned_stories.append(cleaned_story)
    
output_file = f"data/trends_cleaned_{date_string}.csv"

with open (output_file, "w", encoding = "utf-8") as file :
   fieldnames = [
        "post_id",
        "title",
        "category",
        "score",
        "num_comments",
        "author",
        "collected_at"
    ]
   
   writer = csv.DictWriter(file, fieldnames = fieldnames)
   writer.writeheader()
   writer.writerows(cleaned_stories)

print(f"Cleaned {len(cleaned_stories)} files")
print(f"Saved to File {output_file}")

