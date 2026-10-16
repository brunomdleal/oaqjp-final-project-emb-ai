"""
    Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Sentiment Analyzer")

@app.route("/emotionDetector")
def sent_analyzer():
    """
        This code receives the text from the HTML interface and
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence
        score for the provided text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    analise = emotion_detector(text_to_analyze)
    print(f"analise{analise}")
    if "dominant_emotion" in analise:
        dominant_emotion = analise["dominant_emotion"]
        score = analise[dominant_emotion]
        return f"The given text has been identified as {dominant_emotion} with a score of {score}."
    return analise

@app.route("/")
def render_index_page():
    """
        This function initiates the rendering of the main application
        page over the Flask channel
    """
    return render_template("index.html")

if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)

@app.errorhandler(418)
def text_to_evaluate_not_found():
    """
        This function handles the throwing error: Missing text to analyse
    """
    return {"message": "Text to analyse is missing"}, 418

@app.errorhandler(400)
def bad_request():
    """
        This function handles the throwing error: Bad request
    """
    return {"message": "Bad request"}, 400
