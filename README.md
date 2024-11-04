  
# YouTube Comments Sentiment Analysis

Analyze and rate YouTube playlist comments with real-time sentiment analysis. This Django-based project scrapes comments from YouTube videos in a playlist, performs sentiment analysis, and displays results with a visually engaging rating system.

## 📌 Features
- **Sentiment Analysis**: Processes YouTube comments and categorizes them as positive or negative.
- **Dynamic Rating System**: Calculates an average sentiment rating (1 to 10) based on comments and visualizes it with emoji reactions.
- **Interactive UI**: Displays an engaging star rating component using Tailwind CSS, with stars filled based on the calculated sentiment score.

## 📁 Project Structure
- **Backend**: Django framework for managing data processing and serving analysis results.
- **Frontend**: Tailwind CSS for styling, with a rating display that dynamically reflects sentiment scores.
- **APIs**: Utilizes the YouTube Data API for comment extraction.

## ⚙️ Requirements
- Python 3.x
- Django
- YouTube Data API Key
- Tailwind CSS

*For more details, see `requirements.txt`.*

## 🚀 Setup Guide

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ayushwagh2/your-repo-name.git
    cd your-repo-name
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure environment variables**:
    Create a `.env` file in the root directory with the following variables:
    ```bash
    YOUTUBE_API_KEY=your_api_key
    ```

4. **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Start the server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the app**:
   Open your browser and go to `http://localhost:8000`.

## 💡 Usage
- **Analyze Comments**: Enter a YouTube playlist URL to fetch and analyze comments.
- **View Sentiment**: See an aggregated rating and emoji reaction based on sentiment analysis.
- **Customize**: Modify the rating criteria and emoji reactions as desired.

## 📊 Example Output
*Example sentiment ratings and emoji reactions will be displayed here when the app is used.*

## 🛠 Future Enhancements
- **Detailed Analysis Report**: Breakdown of sentiment scores by individual comment.
- **User Feedback**: Option for users to input additional comments or feedback on analysis accuracy.
- **Enhanced UI Components**: Additional interactive features like comment filtering and sorting.

## 📝 License
This project is licensed under the MIT License.

## 🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests.
"""

# File path
file_path = '/mnt/data/README.md'

# Writing content to the README.md file
with open(file_path, 'w') as file:
    file.write(readme_content)

# Adding "How It Works" section to the README content.

how_it_works_content = """
## 🧩 How It Works
This section highlights some core functionalities and code snippets to give an inside look at the project’s structure.

### 1. Fetching Comments from YouTube
The script uses the YouTube Data API to retrieve comments from videos in a given playlist. The API key, stored in the `.env` file, authenticates the requests.

**Key Code Snippet**:
```python
def fetch_comments(video_id):
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?videoId={video_id}&key={API_KEY}&part=snippet&maxResults=100"
    response = requests.get(url)
    comments = [item['snippet']['topLevelComment']['snippet']['textDisplay'] for item in response.json().get('items', [])]
    return comments
from textblob import TextBlob

### 2. Sentiment Analysis with NLP
The comments are processed for sentiment analysis using natural language processing techniques (e.g., TextBlob or NLTK). Each comment receives a sentiment score, which is then averaged to calculate the overall rating.

**Key Code Snippet**:
```python
from textblob import TextBlob

def analyze_sentiment(comment):
    blob = TextBlob(comment)
    sentiment_score = blob.sentiment.polarity  # Ranges from -1 (negative) to 1 (positive)
    return sentiment_score
```

### 3. Calculating and Displaying the Rating
Based on the sentiment scores, an average rating is calculated for the entire playlist. The rating is displayed with a star component and a corresponding emoji on the frontend, using Tailwind CSS for styling.

**Key Code Snippet (Backend)**:
```python
def calculate_average_rating(comments):
    sentiment_scores = [analyze_sentiment(comment) for comment in comments]
    average_score = sum(sentiment_scores) / len(sentiment_scores)
    return round(average_score * 5)  # Scaled to 5-star rating system
```

**Frontend (Rating Component with Tailwind CSS)**:
```html
<div class="rating">
    {% for i in range(average_rating) %}
        <span class="star filled">★</span>
    {% endfor %}
    {% for i in range(5 - average_rating) %}
        <span class="star">☆</span>
    {% endfor %}
</div>
```

### 4. Emoji Reactions Based on Rating
The emoji reaction is determined by the final average rating, providing users with a quick visual interpretation of the sentiment.

**Key Code Snippet**:
```python
def get_emoji_reaction(rating):
    if rating >= 8:
        return "😊"  # Positive sentiment
    elif rating >= 5:
        return "😐"  # Neutral sentiment
    else:
        return "😢"  # Negative sentiment
```
