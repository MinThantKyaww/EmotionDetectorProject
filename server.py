"""Serve the Emotion Detector web application."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the application's input form."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze the supplied text and display its emotion scores."""
    text = request.args.get("textToAnalyze", "")
    if not text.strip():
        return "Invalid text! Please try again!"

    scores = emotion_detector(text)
    if scores["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {scores['anger']}, 'disgust': {scores['disgust']}, "
        f"'fear': {scores['fear']}, 'joy': {scores['joy']} and "
        f"'sadness': {scores['sadness']}. "
        f"The dominant emotion is {scores['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
