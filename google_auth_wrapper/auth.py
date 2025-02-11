from google_auth_oauthlib.flow import InstalledAppFlow


def authenticate(
    scopes=None, path_to_credentials="credentials.json", path_to_refresh="refresh.txt"
):
    flow = InstalledAppFlow.from_client_secrets_file(path_to_credentials, scopes)
    creds = flow.run_local_server(port=0)

    with open(path_to_refresh, "w") as f:
        f.write(creds.refresh_token)
