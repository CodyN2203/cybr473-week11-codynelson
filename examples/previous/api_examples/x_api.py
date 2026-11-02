import requests

# Unlike the Pokémon API, the X Api requires a token to access.

# To Access the API for X you will need to make a developer account:

# Make an account
# Go to https://developer.x.com/en/portal/dashboard
# You will have to request access to the free tier

# Navigate through the developer portal until you can generate a bearer token

# You can do this by navigating to the "Projects and Apps Section"
# Go to the "Default Project..." "1234.." Then click on "Keys and Tokens.

# With the Free Tier:
# You can only retrieve 100 Posts so start small retrieving no more than 10 posts at a time (the minimum)
# This way you have plenty of space to test and adjust

# Put your Token in a .env file (YOU WILL NOT COMMIT THIS TO GITHUB)
# Look at how the .env_example file is formatted at the root of this project

# Import the .env loader
from dotenv import load_dotenv
import os

# Load from .env file
load_dotenv()

# Access environment variables - This makes sure your token is not commited to GitHub and is safe
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Now similarly to how we fetched Pokémon - we will fetch tweets. With some adjustments
# Note, with the free tier you can only do this once every 15 minutes

def get_tweets(query="Arizona", max_results=10): # Start with fetching 10 Tweets so you don't exhaust your free tier too quickly
    # Error out if there is no token
    if not BEARER_TOKEN:
        raise ValueError("Missing Bearer Token. Set TWITTER_BEARER_TOKEN as an environment variable. (See Code Comments)")

    # requests.get takes in some optional parameters. Here is were we can set the tokens.
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

    # Read https://docs.x.com/x-api/posts/search-recent-posts to understand in more detail the API's workings

    url = "https://api.twitter.com/2/tweets/search/recent" # This is the endpoint for most recent posts
    params = {
        "query": query,
        "max_results": max_results,
        "tweet.fields": "created_at,author_id,text" # These are the fields we wants back
    } # What these params do is essentially add the get query params to the url so https://api.twitter.com/2/tweets/search/recent?query=query_here...etc

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error fetching tweets: {response.status_code} - {response.text}")
        return []

    data = response.json()
    print(f"Fetched tweets: {len(data['data'])}")
    print(data)
    return data.get("data", [])

# Example usage
if __name__ == "__main__":
    query = input("What tweets shall we search for?")
    if not query:
        query = "Arizona"

    get_tweets(query)