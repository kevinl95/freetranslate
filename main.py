from boto3 import client


def handler(event, context):
    print(event)
    text = event.get("text")
    sourceLanguage = event.get("source")
    targetLanguage = event.get("target")
    response = client.translate_text(
        Text=text,
        SourceLanguageCode=sourceLanguage,
        TargetLanguageCode=targetLanguage
    )
    return {"result": response['TranslatedText']}
