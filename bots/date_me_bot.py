import os
import fbchat
from fbchat.models import *
import re
fbchat._util.USER_AGENTS    = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')

class DateMeBot(fbchat.Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        self.send(message_object, thread_id=thread_id, thread_type=thread_type)

if __name__ == '__main__':
    email = os.environ.get('EMAIL')
    password = os.environ.get('PASSWORD')
    client = DateMeBot(email, password)
