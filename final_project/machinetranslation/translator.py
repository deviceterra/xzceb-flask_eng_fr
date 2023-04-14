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

def englishToFrench(englishText):
    if englishText is None:
        return None
    translation_result = language_translator.translate(
        text=englishText,
        source='en',
        target='fr'
    ).get_result()
    frenchText = translation_result['translations'][0]['translation']
    return frenchText



def frenchToEnglish(frenchText):
    if frenchText is None:
        return None
    translation_result = language_translator.translate(
        text=frenchText,
        source='fr',
        target='en'
    ).get_result()
    englishText = translation_result['translations'][0]['translation']
    return englishText

