import time

print(time.time())
print(time.localtime())
print(time.gmtime())
print(time.localtime(0))
print(time.gmtime(0))

now_time = int(time.time())
print(now_time)

SEC_PER_MIN = 60
SEC_PER_HOUR = 3600 #60 seconds per min * 60 minutes per hour
HOUR_PER_DAY = 24
DAY_PER_YEAR = 365

num_days = now_time // SEC_PER_HOUR // HOUR_PER_DAY
print(num_days, "days since epoch.")

num_years = num_days // DAY_PER_YEAR
print(num_years, "years since epoch\n",
      "epoch start year 1970 +", num_years, "=", num_years + 1970)

#Time Stamp
#seconds from epoch to start of today
midnight_today = num_days * HOUR_PER_DAY * SEC_PER_HOUR
print(midnight_today)
seconds_since_midnight = now_time - midnight_today
print(seconds_since_midnight)
hours = seconds_since_midnight // SEC_PER_HOUR
minutes = (seconds_since_midnight - (hours * SEC_PER_HOUR)) // 60
seconds = seconds_since_midnight - (hours * SEC_PER_HOUR + minutes * 60)

time_of_day = "%s:%s:%s" % (hours, minutes, seconds)

print(time_of_day, "on", num_days, "days since epoch")


