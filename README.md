# GoogleAuth Wrapper

This package simplifies the Google authentication flow for simple DIY use-cases.

# Flow

1. One-time refresh token generation

The following needs to be run once to generate a refresh token. The refresh token lasts indefinitely and so long as the file containing the refresh token persists, you can continue to re-create GoogleAuth credential objects.

```python
from google_auth_wrapper import authenticate

# the Google cloud scopes you would like to enable
scopes = ["https://www.googleapis.com/auth/gmail.send"]

# a path to the `credentials.json` file which you can download from the Google cloud console
path_to_credentials = "credentials.json"

# where you would like to store your refresh token for subsequent requests
path_to_refresh = "refresh.txt"

authenticate(
    scopes=scopes,
    path_to_credentials=path_to_credentials,
    path_to_refresh=path_to_refresh
)
```

2. Simple GoogleAuth credential object generation

After the refresh token has been generated and stored, you just need to specify the Google client ID and Google secret (which can be obtained from the cloud console) and you can re-generate as many credential objects as you like until Google refreshes their API keys, which happens irregularly (years, not hours).

```python
from google_auth_wrapper import credentials

creds = credentials(
    scopes=scopes,
    client="your_client_id",
    secret="your_client_secret",
    path_to_refresh=path_to_refresh
)
```
