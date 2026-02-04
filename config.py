# config.py
# Mock configuration only (no real TikTok dependency)

TIKTOK_CLIENT_ID = "mock_tiktok_client_id"
TIKTOK_CLIENT_SECRET = "mock_tiktok_client_secret"
TIKTOK_REDIRECT_URI = "http://localhost:8000/callback"

AUTHORIZATION_URL = "https://mock.tiktok.com/oauth/authorize"
TOKEN_URL = "https://mock.tiktok.com/oauth/token"

SCOPES = "ads.management"

USE_MOCK_API = True
