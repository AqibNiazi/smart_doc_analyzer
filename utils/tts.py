import io
from gtts import gTTS

def text_to_mp3_bytes(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    buf = io.BytesIO()
    tts.write_to_fp(buf)
    buf.seek(0)
    return buf.read()
