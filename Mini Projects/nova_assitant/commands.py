# commands.py

import os
import webbrowser
import pyautogui
import speech_recognition as sr
import pyttsx3
import time
import apps
import config

engine = pyttsx3.init()

# ---------------- SPEAK ----------------
def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------------- LISTEN COMMAND ----------------
def listen_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        speak("Listening")
        print("🎙️ Listening for command...")
        audio = r.listen(source, phrase_time_limit=6)

    try:
        text = r.recognize_google(audio, language="en-IN")
        print("🗣️ Command heard:", text)
        return text.lower()
    except Exception as e:
        print("❌ Command error:", e)
        speak("I did not understand")
        return ""

# ---------------- HANDLE COMMAND ----------------
def handle_command():
    command = listen_command()

    if not command:
        config.IS_LISTENING_COMMAND = False
        return

    # -------- OPEN APP --------
    if command.startswith("open"):
        for name, exe in apps.APPS.items():
            if name in command:
                os.system(f"start {exe}")
                speak(f"Opening {name}")
                config.IS_LISTENING_COMMAND = False
                return

    # -------- CLOSE APP / ALL --------
    if command.startswith("close"):
        if "all" in command:
            os.system("taskkill /f /im chrome.exe")
            os.system("taskkill /f /im msedge.exe")
            speak("Closing all windows")
            config.IS_LISTENING_COMMAND = False
            return

        for name, exe in apps.APPS.items():
            if name in command:
                os.system(f"taskkill /f /im {exe}")
                speak(f"Closing {name}")
                config.IS_LISTENING_COMMAND = False
                return

    # -------- SHUTDOWN / RESTART / SLEEP --------
    if "shutdown" in command:
        speak("Shutting down in 5 seconds")
        os.system("shutdown /s /t 5")

    if "restart" in command:
        speak("Restarting system")
        os.system("shutdown /r /t 5")

    if "sleep" in command:
        speak("Putting system to sleep")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    # -------- VOLUME CONTROL --------
    if "increase volume" in command or "volume up" in command:
        pyautogui.press("volumeup")
        speak("Volume increased")

    if "decrease volume" in command or "volume down" in command:
        pyautogui.press("volumedown")
        speak("Volume decreased")

    if "mute volume" in command or "mute" in command:
        pyautogui.press("volumemute")
        speak("Muted")

    # -------- TYPE TEXT --------
    if command.startswith("please type"):
        text = command.replace("please type", "").strip()
        pyautogui.write(text)
        speak("Typed")

    # -------- SEARCH IN APP --------
    if command.startswith("search"):
        for app, url in apps.SEARCH_ENGINES.items():
            if app in command:
                query = command.replace("search", "").replace(app, "").strip()
                webbrowser.open(url.format(query))
                speak(f"Searching {query} in {app}")
                config.IS_LISTENING_COMMAND = False
                return

    # -------- OPEN SOMETHING IN APP --------
    if command.startswith("open") and "in" in command:
        parts = command.split("in")
        query = parts[0].replace("open", "").strip()
        app = parts[1].strip()

        if app in apps.SEARCH_ENGINES:
            webbrowser.open(apps.SEARCH_ENGINES[app].format(query))
            speak(f"Opening {query} in {app}")
            config.IS_LISTENING_COMMAND = False
            return

    # -------- SCROLL --------
    if "scroll down" in command:
        pyautogui.scroll(-500)

    if "scroll up" in command:
        pyautogui.scroll(500)

    # -------- ZOOM --------
    if "zoom in" in command:
        pyautogui.hotkey("ctrl", "+")

    if "zoom out" in command:
        pyautogui.hotkey("ctrl", "-")

    speak("Command not recognized")
    config.IS_LISTENING_COMMAND = False
