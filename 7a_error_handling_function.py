"""Module responsible for emotion detection using Watson NLP."""
import json
import requests


def emotion_detector(text_to_analyse):
    """
    Sends a POST request to Watson EmotionPredict API, extracts scores,
    and returns a dictionary with each emotion score and the dominant emotion.
    Returns None for all values if status code is 400 or input is invalid.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=my_obj, headers=headers)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant_emotion,
        }

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }