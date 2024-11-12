VOICE_F = "de-DE-KatjaNeural"
VOICE_M = "de-DE-FlorianMultilingualNeural"
Language_En = "en-US"
Language_De = "de-DE"

def doctor_selection():
    geschlecht = input("Enter Option Male(m) or Female(f): ")
    if geschlecht == "f":
        return VOICE_F
    elif geschlecht == "m":
        return VOICE_M
    
def language_selection():
    language = input("Enter Option language: ")
    if language == "us":
        return Language_En
    elif language == "de":
        return Language_De