from google_auth_oauthlib.flow import InstalledAppFlow
import pickle, os

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    if os.path.exists('token.pkl'):
        with open('token.pkl', 'rb') as token:
            creds = pickle.load(token)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.pkl', 'wb') as token:
            pickle.dump(creds, token)
    return creds

if __name__ == "__main__":
    creds = authenticate()
    print("✅ Google account authenticated. You are ready to read Gmail!")
