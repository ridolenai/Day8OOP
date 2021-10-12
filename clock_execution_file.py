from alarm_clock import AlarmClock





clock_one = AlarmClock ('0930', True, '1030')

configurator = (input ('What would you like to do? Type 1 to set the time, 2 to configure the alarm, or 3 to display current time. '))

if configurator == ('1'):
    clock_one.change_time()
elif configurator == ('2'):
    clock_one.alarm_state()
else:
    print ('0930')


