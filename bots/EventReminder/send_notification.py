import os
from dotenv import load_dotenv
import fbchat
from time import sleep

load_dotenv()

def send_notification(msg):
    # Log the user in
    session = fbchat.Session.login(os.environ['EMAIL'], os.environ['PASS'])
    client = fbchat.Client(session=session)

    users = client.fetch_threads(limit=20)
    for user in users:
        if (user.name == 'Teo Podobnik'):
            user.start_typing()
            sleep(5)
            user.stop_typing()
            user.send_text(msg)
    # Log the user out
    session.logout()


'''
Other useful methods:
- id
- name
- emoji
- fetch
- fetch_messages
- send_emoji
- send_files
- send_text
- send_uri
- start_typing
- stop_typing
'''

if __name__ == '__main__':
    send_notification('test')
