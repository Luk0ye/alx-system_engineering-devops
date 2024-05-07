import requests

def number_of_subscribers(subreddit):
  """
  Queries the Reddit API for the subscriber count of a subreddit.

  Args:
      subreddit: The name of the subreddit to query.

  Returns:
      The number of subscribers for the subreddit, or 0 if the subreddit
      is invalid.
  """
  url = f"https://reddit.com/r/{subreddit}/about.json?limit=0"
  headers = {'User-Agent': 'My Custom User Agent (e.g., script name v1.0)'}  # Set custom User-Agent

  try:
    response = requests.get(url, headers=headers, allow_redirects=False)  # Don't follow redirects

    response.raise_for_status()  # Raise exception for unsuccessful requests (e.g., 404)
    data = response.json()
    return data['data']['subscribers']
  except (requests.exceptions.RequestException, KeyError):
    return 0  # Handle request errors and missing subscriber data

# Example usage (assuming 0-main.py is in the same directory)
if __name__ == '__main__':
  import sys

  if len(sys.argv) < 2:
    print("Please pass an argument for the subreddit to search.")
  else:
    subscribers = number_of_subscribers(sys.argv[1])
    print(f"{subscribers:,}")  # Print with comma separators for readability