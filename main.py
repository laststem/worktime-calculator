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

# 10:45~15:59
# 17:16~22:40 -> 5:24
# 10:45~21:23
while True:
    t = input_time('Enter the start time: ')
    if start_time is None:
        start_time = t

    t2 = input_time('Enter the end time: ')
    if end_time is None:
        end_time = t2

    if start_time != t:
        end_time += (t2 - t)

    print('%s ~ %s' % (start_time.strftime('%H:%M'), end_time.strftime('%H:%M')))
