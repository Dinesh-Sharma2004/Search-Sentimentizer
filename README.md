# Search-Sentimentizer
A Python-based web application that combines web scraping and sentiment analysis to fetch search results from Google and analyze their sentiment. This project uses SerpAPI to retrieve search results and TextBlob for sentiment analysis, all integrated into a Flask web application.

#Features
Search and Scrape: Fetches search results for any topic from Google using SerpAPI.

Sentiment Analysis: Analyzes the sentiment of the search result snippets, categorizing them as positive, neutral, or negative.

Intuitive Web Interface: Simple and user-friendly interface for entering topics and viewing sentiment results.

Custom Ranking: Displays results ranked by sentiment polarity.


#Technologies Used

Python: Core programming language.
Flask: Web framework for creating the application.
SerpAPI: API for fetching Google search results.
TextBlob: Library for performing sentiment analysis.
HTML/CSS: For the frontend.

#Prerequisites

Python 3.8 or higher.
A valid SerpAPI API key.
Basic understanding of Python and Flask.


#Installation
Clone the Repository:

git clone https://github.com/Dinesh-Sharma2004/Search-Sentimentizer.git
cd Search-Sentimentizer
Set up a Virtual Environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install Dependencies:

pip install -r requirements.txt
Set up Environment Variables:

Create a .env file in the project root.
Add your SerpAPI API key:
SERPAPI_API_KEY=your_serpapi_key
🔧 Usage
Run the Application:

python app.py
Access the Web Application: Open your browser and navigate to:
http://127.0.0.1:5000/

Enter a Topic:

Enter any topic in the search bar.
Click Search to retrieve and analyze the results.
#Sentiment Analysis
Sentiment polarity ranges from -1 (very negative) to 1 (very positive).
Results are displayed in two sections:
Positive Sentiments: Top-ranked results with positive polarity.
Negative Sentiments: Lower-ranked results with negative polarity.


#Project Structure
Search-Sentimentizer/

templates/
  ├── index.html          # Homepage
  
  |── results.html        # Results page
  
  ├── app.py                  # Main application
  
  ├── requirements.txt        # Python dependencies
  
  ├── README.md               # Project documentation
  


# Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.


# Acknowledgments
1. SerpAPI for web scraping.
2. TextBlob for sentiment analysis.
