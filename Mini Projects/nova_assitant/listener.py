# listener.py

import speech_recognition as sr
import time
import config

def listen_for_wake_word(callback):
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("🎧 Calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("✅ Mic ready")

    while True:
        if not config.ASSISTANT_ON or config.IS_LISTENING_COMMAND:
            time.sleep(0.3)
            continue

        with sr.Microphone() as source:
            try:
                print("👂 Listening for wake word...")
                audio = r.listen(source, phrase_time_limit=3)

                text = r.recognize_google(audio, language="en-IN").lower()
                print("🗣️ Heard:", text)

                for wake in config.WAKE_WORDS:
                    if wake in text:
                        print("🔥 Wake word detected")
                        config.IS_LISTENING_COMMAND = True
                        callback()
                        break

            except sr.UnknownValueError:
                pass
            except Exception as e:
                print("❌ Listener error:", e)
