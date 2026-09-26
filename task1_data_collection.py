import requests
import json
import os
import time
from datetime import datetime

#initializing the urls and headers
TOP_STORIES_URL ="https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"
headers = {"User-Agent": "TrendPulse/1.0"}

#creating the keywords for search
keywords = {
    "technology": [
        "AI", "software", "tech", "code", "computer",
        "data", "cloud", "API", "GPU", "LLM"
    ],

    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ],

    "sports": [
        "NFL", "NBA", "FIFA", "sport", "game", "team",
        "player", "league", "championship"
    ],

    "science": [
        "research", "study", "space", "physics",
        "biology", "discovery", "NASA", "genome"
    ],

    "entertainment": [
        "movie", "film", "music", "Netflix", "game",
        "book", "show", "award", "streaming"
    ]
}

#creating a function to find  category
def classify_category(title):
    title_lower = title.lower()
    for category,words in keywords.items():
        for word in words :
            if word.lower() in title_lower:
                return category         
    return None   
        
#getting the story ids from first url
try:
    response = requests.get(
    TOP_STORIES_URL,
    headers=headers,
    timeout=10
    )
    story_ids = response.json()[:500]
    
except requests.RequestException as e:
    print(f"Failed to fetch story IDs: {e}")
    exit()
    
    
# fetching each story and storing it in a list so that fetching from api occurs only once    
fetched_stories = []
for index, story_id in enumerate(story_ids, start=1):

    url = ITEM_URL.format(story_id)

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()
        story = response.json()

    except requests.RequestException as e:
        print(f"Failed to fetch story {story_id}: {e}")
        continue

    # Make sure this is a story
    if story.get("type") != "story":
        continue

    fetched_stories.append(story)

    # Show progress every 25 stories
    if index % 25 == 0:
        print(f"Fetched {index}/500 stories")


# Store the final selected stories
stories = []

category_counts = {
    "technology": 0,
    "worldnews": 0,
    "sports": 0,
    "science": 0,
    "entertainment": 0
}


# Process each category using already-fetched stories
for category in keywords:

    for story in fetched_stories:

        # Stop when this category reaches 25 stories
        if category_counts[category] >= 25:
            break

        title = story.get("title", "")

        detected_category = classify_category(title)

        if detected_category != category:
            continue

        record = {
            "post_id": story.get("id"),
            "title": title,
            "category": detected_category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by", ""),
            "collected_at": datetime.now().isoformat()
        }

        stories.append(record)

        category_counts[category] += 1

    # 2-second wait between categories
    time.sleep(2)
    
# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)


# Create today's filename
date_string = datetime.now().strftime("%Y%m%d")

filename = f"data/trends_{date_string}.json"


# Save the stories as JSON
with open(filename, "w", encoding="utf-8") as file:
    json.dump(stories, file, indent=4, ensure_ascii=False)


# Printing final result
print(f"Collected {len(stories)} stories. Saved to {filename}")

# Printng the categories from the given response
print(category_counts)