from alarm_clock import AlarmClock





clock_one = AlarmClock ('0930', True, '1030')

configurator = print (input ('What would you like to do? Type 1 to set the time or 2 to configure the alarm. '))

if configurator == 1:
    clock_one.change_time()
elif configurator == 2:
    clock_one.alarm_state()


