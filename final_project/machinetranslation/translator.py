import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
InstanceOfTranslator = LanguageTranslatorV3(version="2018-05-01", authenticator=authenticator)
InstanceOfTranslator.set_service_url(url)

def english_to_french(english_text):
    french_text = InstanceOfTranslator.translate(text=english_text, model_id="en-fr").get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    english_text = InstanceOfTranslator.translate(text=french_text, model_id="fr-en").get_result()
    return english_text.get("translations")[0].get("translation")

print(english_to_french("Hi there"))

print(french_to_english("Oui"))