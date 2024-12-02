from flask import Flask, request, render_template
from serpapi import GoogleSearch  # Import SerpAPI library
from textblob import TextBlob

app = Flask(__name__)

# Replace with your SerpAPI API Key
API_KEY = "fd93b1955999144f4bffc646cf635d8590c911f904a571801806ecf40f3f153e"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/scrape', methods=['POST'])
def scrape():
    topic = request.form.get('topic')

    if not topic:
        return "Error: Topic missing!", 400

    query = f"{topic}"

    # Set up the SerpAPI request parameters
    params = {
        "q": query,
        "hl": "en",
        "gl": "us",
        "api_key": API_KEY
    }

    # Perform the Google search using SerpAPI
    search = GoogleSearch(params)
    results = search.get_dict()

    if "error" in results:
        return f"Error: {results['error']}", 500

    snippets = []
    search_results = []
    if 'organic_results' in results:
        for result in results['organic_results']:
            title = result.get('title')
            snippet = result.get('snippet', '')  # Extract snippets
            link = result.get('link')
            search_results.append({"title": title, "snippet": snippet, "url": link})
            snippets.append(snippet)

    if not search_results:
        return "No results found.", 404

    # Analyze sentiment of snippets
    sentiments = analyze_sentiment(snippets)

    # Add sentiment scores to search results
    for i, result in enumerate(search_results):
        result["sentiment"] = sentiments[i] if i < len(sentiments) else 0  # Default to 0 if sentiment unavailable

    # Sort results by sentiment score (descending)
    search_results.sort(key=lambda x: x["sentiment"], reverse=True)

    return render_template('results.html', results=search_results)


def analyze_sentiment(snippets):
    sentiments = []
    for snippet in snippets:
        blob = TextBlob(snippet)
        polarity = blob.sentiment.polarity  # Polarity ranges from -1 (negative) to 1 (positive)
        sentiments.append(polarity)
    return sentiments


if __name__ == "__main__":
    app.run(debug=True)
