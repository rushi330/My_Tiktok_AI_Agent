# tiktok_api.py
""" Mock validation rule:
    valid music IDs start with 'music_' 
    """
    
import random

def validate_music_id(music_id):
    
    return bool(music_id and music_id.startswith("music_"))


def submit_ad(payload, access_token):

    print("📡 Submitting ad to TikTok (mock)...")

    outcomes = [
        None,
        "INVALID_TOKEN",
        "INVALID_MUSIC",
        "GEO_RESTRICTED"
    ]

    result = random.choice(outcomes)

    if result is None:
        print(" Ad created successfully")
        return {"success": True, "ad_id": "mock_ad_001"}

    if result == "INVALID_TOKEN":
        raise Exception("OAuth token expired or invalid")

    if result == "INVALID_MUSIC":
        raise Exception("Music ID rejected by TikTok")

    if result == "GEO_RESTRICTED":
        raise Exception("Ads are not supported in this region")
