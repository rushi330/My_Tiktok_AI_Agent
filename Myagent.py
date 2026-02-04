# agent.py
from schemas import AD_SCHEMA
from tiktok_api import validate_music_id

def run_conversation():
    payload = AD_SCHEMA.copy()
    payload["creative"] = payload["creative"].copy()

    payload["campaign_name"] = input("Campaign Name: ").strip()
    payload["objective"] = input("Objective (Traffic / Conversions): ").strip()

    payload["creative"]["text"] = input("Ad Text (max 100 chars): ").strip()
    payload["creative"]["cta"] = input("CTA: ").strip()

    print("\n Music Options")
    print("1. Existing Music ID")
    print("2. Upload Custom Music")
    print("3. No Music")

    choice = input("Choose (1/2/3): ").strip()

    if choice == "1":
        music_id = input("Enter Music ID: ").strip()
        if validate_music_id(music_id):
            payload["creative"]["music_id"] = music_id
        else:
            print(" Invalid Music ID")
            payload["creative"]["music_id"] = None

    elif choice == "2":
        payload["creative"]["music_id"] = "music_custom_001"

    elif choice == "3":
        payload["creative"]["music_id"] = None

    else:
        raise Exception("Invalid music option")

    return payload
