YouTube Comments Sentiment Analysis
Analyze and rate YouTube playlist comments with real-time sentiment analysis. This Django-based project scrapes comments from YouTube videos in a playlist, performs sentiment analysis, and displays results with a visually engaging rating system.

📌 Features
Sentiment Analysis: Processes YouTube comments and categorizes them as positive or negative.
Dynamic Rating System: Calculates an average sentiment rating (1 to 10) based on comments and visualizes it with emoji reactions.
Interactive UI: Display an engaging star rating component using Tailwind CSS, with stars filled based on the calculated sentiment score.
📁 Project Structure
Backend: Django framework for managing data processing and serving analysis results.
Frontend: Tailwind CSS for styling, with a rating display that dynamically reflects sentiment scores.
APIs: Utilizes the YouTube Data API for comment extraction.
⚙️ Requirements
Python 3.x
Django
YouTube Data API Key
Tailwind CSS
For more details, see requirements.txt.

🚀 Setup Guide
Clone the repository:

bash
Copy code
git clone https://github.com/ayushwagh2/your-repo-name.git
cd your-repo-name
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure environment variables:

Create a .env file in the root directory with the following variables:
bash
Copy code
YOUTUBE_API_KEY=your_api_key
Run Migrations:

bash
Copy code
python manage.py migrate
Start the server:

bash
Copy code
python manage.py runserver
Access the app: Open your browser and go to http://localhost:8000.

💡 Usage
Analyze Comments: Enter a YouTube playlist URL to fetch and analyze comments.
View Sentiment: See an aggregated rating and emoji reaction based on sentiment analysis.
Customize: Modify the rating criteria and emoji reactions as desired.
📊 Example Output

🛠 Future Enhancements
Detailed Analysis Report: Breakdown of sentiment scores by individual comment.
User Feedback: Option for users to input additional comments or feedback on analysis accuracy.
Enhanced UI Components: Additional interactive features like comment filtering and sorting.
📝 License
This project is licensed under the MIT License.

🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests.
