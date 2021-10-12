from alarm_clock import AlarmClock
# from alarm_clock import change_time
# from alarm_clock import alarm_state




clock_one = AlarmClock ('0930', True, '1030')

configurator = print (input ('What would you like to do? Type 1 to set the time or 2 to configure the alarm. '))

if configurator == 1:
    change_time
elif configurator == 2:
    alarm_state

