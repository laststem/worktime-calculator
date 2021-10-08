from datetime import datetime, timedelta
import sys

def input_time(s):
    try:
        return datetime.strptime(input(s), '%H:%M')
    except KeyboardInterrupt:
        sys.exit()
    except ValueError:
        return input_time(s)

start_time, end_time, delta = None, None, None

while True:
    t = input_time('Enter the start time: ')
    if start_time is None:
        start_time = t

    t2 = input_time('Enter the end time: ')
    if end_time is None:
        end_time = t2

    if start_time != t:
        end_time += (t2 - t)

    print('work time: %s ~ %s' % (start_time.strftime('%H:%M'), end_time.strftime('%H:%M')))
