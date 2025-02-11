import os
import requests

from google.oauth2.credentials import Credentials


def _get_refresh_token(save_path: str):
    if not os.path.exists(save_path):
        raise Exception("Refresh token not found")

    with open(save_path, "r") as f:
        return f.read()


def _get_access_token(client: str, secret: str, refresh_token: str):
    url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": client,
        "client_secret": secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    }

    response = requests.post(url, data=data).json()

    if "access_token" not in response:
        raise Exception("Access token not found")

    return response.get("access_token")


def credentials(scopes=None, client=None, secret=None, path_to_refresh=None):
    if not scopes:
        raise Exception("Scopes are required")

    if not client:
        raise Exception("Client ID is required")

    if not secret:
        raise Exception("Client secret is required")

    r = _get_refresh_token(path_to_refresh)

    if not r:
        raise Exception("Refresh token not found")

    t = _get_access_token(client, secret, r)

    if not t:
        raise Exception("Access token not found")

    return Credentials(
        token=t,
        refresh_token=r,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client,
        client_secret=secret,
        scopes=scopes,
    )
