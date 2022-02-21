import sched
from datetime import datetime
from time import strftime
from send_notification import send_notification

events_list = [
    ['WARNING - Group Selection deadline: 27-2-2022 23:59', datetime(2022, 2, 22, 00, 55)],
    ['WARNING - Pre-theme Selection deadline: 6-3-2022 23:59', datetime(2022, 3, 5, 23, 55)]
]

s = sched.scheduler()

for e, t in events_list:
    trigger_in = t - datetime.now()
    event = s.enterabs(trigger_in.total_seconds(), 1, send_notification, argument = (e,))
    print("Event created: ", event)

s.run()
