import datetime

now = datetime.datetime.now()

while True:
    current_time = datetime.datetime.now()

    if (now.year != current_time.year
            or now.hour != current_time.hour
            or now.month != current_time.month
            or now.minute != current_time.minute
            or now.second != current_time.second):
        now = current_time
        print(now.strftime("%Y-%m-%d %H:%M:%S"))