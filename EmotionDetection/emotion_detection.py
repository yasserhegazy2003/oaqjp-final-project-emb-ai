import requests
import json

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
def emotion_detector(text_to_analyze):
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }


    response = requests.post(URL, headers=HEADERS, json=payload)

    # Convert response text to dictionary
    data = json.loads(response.text)

    # Extract emotions dictionary
    emotions = data["emotionPredictions"][0]["emotion"]

    # Build scores dictionary
    result = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }

    # Determine dominant emotion
    dominant = max(result, key=result.get)
    result["dominant_emotion"] = dominant

    return result