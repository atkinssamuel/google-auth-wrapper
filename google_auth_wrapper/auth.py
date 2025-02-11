from google_auth_oauthlib.flow import InstalledAppFlow


def authenticate(scopes):
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scopes)
    creds = flow.run_local_server(port=0)

    with open("refresh.txt", "w") as f:
        f.write(creds.refresh_token)
