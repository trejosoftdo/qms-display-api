import pyttsx3
import io
import os 


current_dir = os.path.dirname(os.path.realpath(__file__))



VOICE_PROPERTY = "voice"
SPEECH_RATE_PROPERTY = "rate"
VOLUME_PROPERTY = "volume"
FEMALE_GENDER = "f"
MALE_GENDER = "m"
DEFAULT_VARIANT = 5
ES_LANGUAGE = "es-la"
EN_LANGUAGE = "en-us"
SPEECH_RATE = 170
VOLUME = 1.0
TEMP_FILE = f"{current_dir}/voice.wav"
TEMP_FILE_MODE = "rb"


def text_to_audio(
    text: str,
    language: str = ES_LANGUAGE,
    gender: str = FEMALE_GENDER,
    variant: str = DEFAULT_VARIANT,
    speech_rate: str = SPEECH_RATE,
) -> io.BytesIO:
    """_summary_

    Args:
        text (str): Text to convert to audio
        language (str, optional): Language of the audio. Defaults to ES_LANGUAGE.
        gender (str, optional): Gender of the speaker. Defaults to FEMALE_GENDER.
        variant (str, optional): Variant of the speaker. Defaults to DEFAULT_VARIANT.
        speech_rate (str, optional): Speech rate. Defaults to SPEECH_RATE.

    Returns:
        io.BytesIO: Audio information
    """
    print("Init engine")
    engine = pyttsx3.init()
    engine.setProperty(VOICE_PROPERTY, f"{language}+{gender}{variant}")
    engine.setProperty(SPEECH_RATE_PROPERTY, speech_rate)
    engine.setProperty(VOLUME_PROPERTY, VOLUME)
    print("Saving audio")
    engine.save_to_file(text, TEMP_FILE)
    engine.runAndWait()

    print("Reading audio")
    with open(TEMP_FILE, TEMP_FILE_MODE) as file:
        audio_bytes = io.BytesIO(file.read())

    return audio_bytes
