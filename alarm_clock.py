class AlarmClock:
    def __init__(self, current_time, alarmOn, alarmTime):
        self.time = current_time
        self.alarmOn = alarmOn
        self.alarmTime = alarmTime

    def set_time(self):
        self.set_time = ('09:30')
        self.alarmOn = False
        self.alarmTime = ('1030')

    def display_current:


    def change_time(self):
        new_time = (input ('What is the current time: '))
        print (new_time)

    def alarm_state(self):
        alarm_check = (input ('Would you like the alarm on? 1 for yes and 2 for no please.'))
        if alarm_check == 1:
            alarmOn = True
            noisy_time = (input ('What time would you like to set the alarm? '))
            print ('Your alarm is set for: ')
            print (noisy_time)
        else:
            alarmOn = False
            print ('Your alarm is off.')

            
        
    



