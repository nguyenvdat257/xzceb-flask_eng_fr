import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    if english_text == '':
        return ''
    res = language_translator.translate(english_text, source='en', target='fr').get_result()
    french_text = res['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    if french_text == '':
        return ''
    res = language_translator.translate(french_text, source='fr', target='en').get_result()
    english_text = res['translations'][0]['translation']
    return english_text


if __name__ == '__main__':
    print(english_to_french('hello'))
