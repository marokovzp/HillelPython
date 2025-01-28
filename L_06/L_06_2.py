# in_sec = 0# -> 0 днів, 00:00:00
# in_sec = 224930# -> 2 дні, 14:28:50
# in_sec = 466289# -> 5 днів, 09:31:29
# in_sec = 950400# -> 11 днів, 00:00:00
# in_sec = 1209600# -> 14 днів, 00:00:00
# in_sec = 1900800# - > 22 дні, 00:00:00
# in_sec = 8639999# -> 99 днів, 23:59:59
# in_sec = 22493# -> 0 днів, 06:14:53
# in_sec = 7948799# -> 91 день, 23:59:59
in_sec = int(input ("type number between 0 and 8640000: "))

print(in_sec, end=' ')
print('->', end=' ')

minutes = in_sec/60
hours = minutes/60
# days = int(hours/24)

days = int(hours // 24)
if days > 10 and days < 20: days_str = 'днів'
else:
    leftover = (days % 10)
    if leftover == 1: days_str = 'день'
    elif leftover == 2 or leftover == 3: days_str = 'дні'
    else: days_str = 'днів'

hours = int((hours - (days * 24)) % 60)
if len(str(hours)) < 2: hours_str = str(0) + str(hours)
else: hours_str = str(hours)

minutes = int((minutes - (hours * 60)) % 60)
if len(str(minutes)) < 2: minutes_str = str(0) + str(minutes)
else: minutes_str = str(minutes)

sec = int((in_sec - (minutes * 60)) % 60)
if len(str(sec)) < 2:
    sec_str = str(0) + str(sec)
else: sec_str = str(sec)

print(days, end=' ')
print(days_str, end=' ')
print(hours_str, end=':')
print(minutes_str, end=':')
print(sec_str)