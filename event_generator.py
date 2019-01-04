from datetime import date
import json

events = dict()

for year in range(2019, 2031):
    for month in range(1,13):
        week_counter = 0
        for day in range(1,32):
            try:
                today = date(year, month, day)
            except ValueError:
                pass
            else:
                if today.weekday() == 3:
                    week_counter += 1
                    ftoday = '{}-{:02d}-{:02d}'.format(today.year, today.month, today.day)
                    if week_counter == 1:
                        events[ftoday] = {'url': '#prime'}
                    elif week_counter == 2:
                        events[ftoday] = {'url': '#north'}
                    elif week_counter == 3:
                        events[ftoday] = {'url': '#west'}
                    elif week_counter == 4:
                        events[ftoday] = {'url': '#east'}

with open('js/calendar-dates.js', 'w') as calfile:
    calfile.write('calendar_events = ' + json.dumps(events))