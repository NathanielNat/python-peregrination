import time

attendance = {}
attendance_list =[]


name =''
while name != 'q':
    print('Enter employee name : ')
    print('You can enter q to quit : ')
    name = input()
    attendance[name] = time.time()

attendance_list = [(k, v) for k, v in attendance.items()] 


print(attendance_list)