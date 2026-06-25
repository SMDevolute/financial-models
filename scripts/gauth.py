"""Google auth helper for live Sheets/Drive editing.

Holds the OAuth flow + cached token so other scripts can just call
`get_creds()` and get an authorized credentials object.

Secrets live OUTSIDE the repo in ~/.config/financial-models-gauth/ :
  - client_secret.json  (the Desktop OAuth client)
  - token.json          (cached user token, created on first login)

Run this file directly to perform the one-time browser login:
    python3 scripts/gauth.py
"""
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

CRED_DIR = os.path.expanduser("~/.config/financial-models-gauth")
CLIENT_SECRET = os.path.join(CRED_DIR, "client_secret.json")
TOKEN = os.path.join(CRED_DIR, "token.json")

# Full read/write to Sheets and Drive (needed to convert .xlsx -> native Sheet).
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def get_creds():
    creds = None
    if os.path.exists(TOKEN):
        creds = Credentials.from_authorized_user_file(TOKEN, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
            creds = flow.run_local_server(port=0, prompt="consent")
        with open(TOKEN, "w") as f:
            f.write(creds.to_json())
        os.chmod(TOKEN, 0o600)
    return creds


if __name__ == "__main__":
    c = get_creds()
    print("Authorized OK. Token cached at", TOKEN)
