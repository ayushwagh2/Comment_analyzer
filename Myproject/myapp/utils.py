# youtube_analysis/utils.py

from googleapiclient.discovery import build
import pandas as pd
from textblob import TextBlob
import os

# Set up the YouTube API client
API_KEY = os.getenv("YOUTUBE_API_KEY")  # Set your API key as an environment variable for security
 
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_all_video_ids_from_playlists(playlist_ids):
    """Fetch all video IDs from a list of YouTube playlist IDs."""
    all_videos = []
    for playlist_id in playlist_ids:
        next_page_token = None
        while True:
            playlist_request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )
            playlist_response = playlist_request.execute()
            all_videos += [item['contentDetails']['videoId'] for item in playlist_response['items']]
            next_page_token = playlist_response.get('nextPageToken')
            if not next_page_token:
                break
    return all_videos

def get_replies(youtube, parent_id, video_id):
    """Fetch all replies for a top-level comment on a specific video."""
    replies = []
    next_page_token = None
    while True:
        reply_request = youtube.comments().list(
            part="snippet",
            parentId=parent_id,
            textFormat="plainText",
            maxResults=100,
            pageToken=next_page_token
        )
        reply_response = reply_request.execute()
        for item in reply_response['items']:
            comment = item['snippet']
            replies.append({
                'Timestamp': comment['publishedAt'],
                'Username': comment['authorDisplayName'],
                'VideoID': video_id,
                'Comment': comment['textDisplay'],
                'Date': comment['updatedAt'] if 'updatedAt' in comment else comment['publishedAt']
            })
        next_page_token = reply_response.get('nextPageToken')
        if not next_page_token:
            break
    return replies

def get_comments_for_video(video_id):
    """Fetch all top-level comments for a video and their replies."""
    all_comments = []
    next_page_token = None
    while True:
        comment_request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            pageToken=next_page_token,
            textFormat="plainText",
            maxResults=100
        )
        comment_response = comment_request.execute()
        for item in comment_response['items']:
            top_comment = item['snippet']['topLevelComment']['snippet']
            all_comments.append({
                'Timestamp': top_comment['publishedAt'],
                'Username': top_comment['authorDisplayName'],
                'VideoID': video_id,
                'Comment': top_comment['textDisplay'],
                'Date': top_comment['updatedAt'] if 'updatedAt' in top_comment else top_comment['publishedAt']
            })
            if item['snippet']['totalReplyCount'] > 0:
                all_comments.extend(get_replies(youtube, item['snippet']['topLevelComment']['id'], video_id))
        next_page_token = comment_response.get('nextPageToken')
        if not next_page_token:
            break
    return all_comments

def get_sentiment(comment):
    """Calculate the sentiment polarity of a comment using TextBlob."""
    blob = TextBlob(str(comment))
    return blob.sentiment.polarity

def sentiment_to_rating(sentiment):
    """Convert sentiment polarity to a rating from 1 to 10."""
    if sentiment > 0:
        return 5 + (sentiment * 5)  # Scale positive sentiment to rating 5-10
    elif sentiment < 0:
        return 1 + ((sentiment + 1) * 4)  # Scale negative sentiment to rating 1-5
    else:
        return 5  # Neutral sentiment receives a rating of 5

def analyze_comments(playlist_ids):
    """Analyze comments for all videos in a list of playlists and return sentiment data."""
    all_comments = []
    for video_id in get_all_video_ids_from_playlists(playlist_ids):
        video_comments = get_comments_for_video(video_id)
        all_comments.extend(video_comments)

    # Perform sentiment analysis and rating calculation
    sentiments = [get_sentiment(comment['Comment']) for comment in all_comments]
    ratings = [sentiment_to_rating(sent) for sent in sentiments]

    average_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
    average_rating = sum(ratings) / len(ratings) if ratings else 0

    # Convert to DataFrame for easy data handling in views if needed
    comments_df = pd.DataFrame(all_comments)

    return average_sentiment, average_rating, comments_df
