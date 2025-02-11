import os
import requests

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from google_auth_wrapper.auth import authenticate


def refresh_token():
    if not os.path.exists("refresh.txt"):
        print("Refresh token not found. Authenticating...")
        authenticate()

    with open("refresh.txt", "r") as f:
        return f.read()


def access_token(client_id, client_secret, r):
    url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": r,
        "grant_type": "refresh_token",
    }

    response = requests.post(url, data=data).json()

    if "access_token" not in response:
        print(response)
        raise Exception("Access token not found")

    return response.get("access_token")


def credentials(client_id, client_secret, scopes):
    r = refresh_token()

    if not r:
        raise Exception("Refresh token not found")

    t = access_token(r)

    if not t:
        raise Exception("Access token not found")

    return Credentials(
        token=t,
        refresh_token=r,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        client_secret=client_secret,
        scopes=scopes,
    )


def gmail_resource():
    return build("gmail", "v1", credentials=credentials())
