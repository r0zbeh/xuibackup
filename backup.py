from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from datetime import datetime, timedelta
import json
from google.oauth2 import service_account
from googleapiclient.errors import HttpError

f=open('sgdrive.json')
service_account_info = json.load(f)
f.close
SCOPES = ['https://www.googleapis.com/auth/drive']

creds = service_account.Credentials.from_service_account_info(
        service_account_info, scopes=SCOPES)
service = build('drive', 'v3', credentials=creds)

#upload
vul1='1uAi0cZ9raw1P9KVrKqKU4AZna3W0IRNr'
zh2='1mfEzrPycqQCgKCSiTw0QYU2pZX6Si2fD'
s3='14kxE_TvIOWOq0kBGwievh7-s-I_peNyU'
ir4='1OcJji_z7kuM4J4VV4xJoyKxLYmKDxyUj'
z1='1PWYTqLsLhCwOnY_0AZl7chLiQW7Es2Ux'
z3='1CQh9Ax4nDt-z0v6Sd9cJ4BpFjB2JdPh2'

file_metadata={
    'name':'x-ui.db',
    'parents':[vul1]
}
media_content= MediaFileUpload('/etc/x-ui/x-ui.db',mimetype='application/db')

file = service.files().create(

    body=file_metadata,
    media_body=media_content
    
).execute()

expdate = datetime.now()-timedelta(days=6)
expdate=expdate.strftime('%Y-%m-%dT%H:%M:%S')
try:
        # create drive api client
            files = []
            page_token = None
            response = service.files().list(q=f"createdTime < '{expdate}' and mimeType != 'application/vnd.google-apps.folder'",
                                            spaces='drive',
                                            fields='nextPageToken, '
                                                   'files(id)', pageToken=page_token).execute()
            if  response.get('files', []) != None:   
                for file in response.get('files', []):
                    # print(F'Found file: {file.get("name")}, {file.get("id")}, {file.get("mimeType")}')
                    service.files().delete(fileId=file.get("id")).execute()
                files.extend(response.get('files', []))
                page_token = response.get('nextPageToken', None)

except HttpError as error:
        print(F'An error occurred: {error}')

        
