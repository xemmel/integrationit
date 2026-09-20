## Simple code

```bash

import os
from azure.identity import DefaultAzureCredential
import azure.cognitiveservices.speech as speechsdk


location = os.environ["FOUNDRY_LOCATION"]
account = os.environ["FOUNDRY_ACCOUNT"]

credential = DefaultAzureCredential()

speech_config = speechsdk.SpeechConfig(
    endpoint=f"https://{account}.cognitiveservices.azure.com/",
    token_credential=credential
)


speech_config.speech_synthesis_voice_name = "en-US-AvaMultilingualNeural"

audio_config = speechsdk.audio.AudioOutputConfig(
        filename="output.wav"
)

synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=audio_config
)

result = synthesizer.speak_text_async(
    "Hello from Microsoft Foundry."
).get()

print(result.reason)

```