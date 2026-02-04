# oauth.py
''' 
    MOCK OAuth Authorization Code Flow

    Reason:
    1)TikTok Ads requires verified business & advertiser account
    2)TikTok is geo-restricted in India
    '''
from token_store import save_token, load_token

def authenticate():

    token = load_token()
    if token:
        print("🔐 Using stored access token")
        return token["access_token"]

    print("🔐 Simulating TikTok OAuth flow...")

    token_data = {
        "access_token": "mock_access_token_123",
        "token_type": "Bearer",
        "expires_in": 86400
    }

    save_token(token_data)
    print("✅ Mock OAuth successful")

    return token_data["access_token"]
