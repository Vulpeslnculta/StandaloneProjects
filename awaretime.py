import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print(f"Naive local time {local_time}")
print(f"Naive UTC {utc_time}")

aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print(f"Aware local time {aware_local_time}")
print(f"Aware UTC {aware_utc_time}")