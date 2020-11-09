import time
import datetime

attendance = {}
attendance_list =[]


name =''
while name != 'q':
    print('Enter employee name : ')
    print('You can enter q to quit : ')
    name = input()
    signIn = datetime.datetime.now()
    attendance[name] = signIn.strftime('%d-%m-%Y %Y:%M:%S%p')

attendance_list = [(k, v) for k, v in attendance.items()] 


print(attendance_list)