"""Class responsible to deal with the sentiment analyzer"""
import requests, json

def sentiment_analyzer(text_to_analyse):
    """
        Sends a 'POST' request to an API in order to get the sentiment analise
        :argument text_to_analyse -> is the text we want to analise
    """
    url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    my_obj = { "raw_document": { "text": text_to_analyse } }
    res = requests.post(url, json=my_obj, headers=header)
    if res.status_code == 200:
        formated_res = json.loads(res.text)
        label = formated_res["documentSentiment"]["label"]
        score = formated_res["documentSentiment"]["score"]
    else:
        label = None
        score = None
    # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)
