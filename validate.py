# validator.py

def validate_payload(payload):
    if len(payload["campaign_name"]) < 3:
        raise Exception("Campaign name must be at least 3 characters")

    if payload["objective"] not in ["Traffic", "Conversions"]:
        raise Exception("Objective must be Traffic or Conversions")

    text = payload["creative"]["text"]
    if not text or len(text) > 100:
        raise Exception("Ad text is required and must be under 100 characters")

    if not payload["creative"]["cta"]:
        raise Exception("CTA is required")

    if payload["objective"] == "Conversions" and payload["creative"]["music_id"] is None:
        raise Exception("Music is required for Conversions campaigns")

    return True
