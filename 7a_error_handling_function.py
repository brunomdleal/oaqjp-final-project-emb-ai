"""Class responsible to deal with the sentiment analyzer"""
import requests

def execute_nlp_request(text_to_analyse):
    """
        Responsible to generate the output
        :argument text_to_analyse -> is the text we want to analise
        :returns API response
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = {"raw_document": {"text": text_to_analyse}}
    return requests.post(url, json=my_obj, headers=header)

def handle_output(res, op):
    """
        Responsible to generate the output
        :argument res -> Response of the API call
        :argument op -> dictionary object
        :returns op -> dictionary object
    """
    if res.status_code == 200:
        emotions = res.json().get("emotionPredictions")[0].get("emotion")
        for e in op.keys():
            if e in emotions:
                op[str(e)] = emotions[str(e)]
        op["dominant_emotion"] = max(emotions, key=emotions.get)
    elif res.status_code == 400:
        return "There was a problem with the request input", 400
    return op


def emotion_detector(text_to_analyse):
    """
        Sends a 'POST' request to an API in order to get the sentiment analise
        :argument text_to_analyse -> is the text we want to analise
        :returns op dictionary object
    """
    op = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }
    if text_to_analyse is None or text_to_analyse == "" or type(text_to_analyse) != str:
        return "Text to analyse is missing", 418

    res = handle_output(execute_nlp_request(text_to_analyse), op)
    return res
