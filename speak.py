import json
import os
import subprocess

# JSON-Datei einlesen
json_file = "dialogue.json"
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Zähler initialisieren
counter = 1
wav_files = []

# Schleife durch jeden Dialog-Eintrag
for entry in data["dialogue"]:
    person = entry["person"]
    text = entry["text"]
    filename = f"{counter}.wav"
    
    # TTS-Befehl erstellen und ausführen
    if person == "PERSON1":
        tts_command = f"tts --model_name tts_models/de/thorsten/vits --text \"{text}\" --out_path \"{filename}\""
    elif person == "PERSON2":
        tts_command = f"tts --model_name tts_models/de/css10/vits-neon --text \"{text}\" --out_path \"{filename}\""
    
    # TTS ausführen
    subprocess.run(tts_command, shell=True)
    
    # Die generierte Datei zur Liste hinzufügen
    wav_files.append(filename)
    
    # Zähler erhöhen
    counter += 1

# SOX-Befehl zum Zusammenfügen der Dateien
sox_command = "sox " + " ".join(wav_files) + " output.wav pad 0 2"

# Zusammenführen der WAV-Dateien
subprocess.run(sox_command, shell=True)

print("Die Audiodateien wurden erfolgreich zusammengeführt in 'output.wav'.")

