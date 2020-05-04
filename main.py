import boto3


def handler(event, context):
    print(event)
    languagecodes = {'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Azerbaijani': 'az', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Chinese (Simplified)': 'zh', 'Chinese (Traditional)': 'zh-TW', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dari': 'fa-AF', 'Dutch': 'nl', 'English': 'en', 'Estonian': 'et', 'Finnish': 'fi', 'French': 'fr', 'French (Canada)': 'fr-CA', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Hausa': 'ha', 'Hebrew': 'he', 'Hindi': 'hi', 'Hungarian': 'hu',
                     'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Latvian': 'lv', 'Malay': 'ms', 'Norwegian': 'no', 'Persian': 'fa', 'Pashto': 'ps', 'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro', 'Russian': 'ru', 'Serbian': 'sr', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Spanish (Mexico)': 'es-MX', 'Swahili': 'sw', 'Swedish': 'sv', 'Tagalog': 'tl', 'Tamil': 'ta', 'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Vietnamese': 'vi'}
    client = boto3.client('translate')
    text = event.get("text")
    sourceLanguage = event.get("source")
    targetLanguage = event.get("target")
    response = client.translate_text(
        Text=text,
        SourceLanguageCode=languagecodes[sourceLanguage],
        TargetLanguageCode=languagecodes[targetLanguage]
    )
    return {"result": response['TranslatedText']}
