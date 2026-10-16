"""Class responsible to deal with the sentiment analyzer"""
import requests, json

def emotion_detector(text_to_analyse):
    """
        Sends a 'POST' request to an API in order to get the sentiment analise
        :argument text_to_analyse -> is the text we want to analise
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyse } }
    res = requests.post(url, json=my_obj, headers=header)
    return res.text
