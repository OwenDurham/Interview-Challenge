import os
from twilio.rest import Client
import padas as pd
from datetime import date

df = pd.read_csv (r'/Users/owendurham/Downloads/Interview-Challenge-main\addressBook.csv')

account_sid = os.environ['ACa781c9ef3e203041b6949c9d347433ef']
auth_token = os.environ['ef7956361f0bd473389b050fcfd8158d']
client = Client(account_sid, auth_token)

today = date.today()

for x in df.iloc['Date of Birth']:
  if x == today:
    message = client.messages.create(
      body='Happy Birthday ' df.iloc['First Name'].values[x] 'from Owen Durham! Call me at 515-681-1414 to plan a lunch sometime.',
      from_='515-325-4937',
      to= df.iloc['Mobile Phone'].values[x]
    )

print(message.sid)
