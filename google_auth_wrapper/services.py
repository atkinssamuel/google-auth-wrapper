from googleapiclient.discovery import build

from google_auth_wrapper import credentials


def gmail_resource():
    return build("gmail", "v1", credentials=credentials())
