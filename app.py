# app.py
from oauth import authenticate
from Myagent import run_conversation
from validate import validate_payload
from tiktok_api import submit_ad

def main():
    print("\n TikTok Ads AI Agent (Mock Mode)\n")

    try:
        access_token = authenticate()
        payload = run_conversation()

        validate_payload(payload)
        submit_ad(payload, access_token)

    except Exception as e:
        print("\n Error occurred")
        print("Reason:", str(e))
        print("Suggested action: Review inputs or retry")

if __name__ == "__main__":
    main()
