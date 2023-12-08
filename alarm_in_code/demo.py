from pygame import mixer
from tkinter.ttk import *
from tkinter import *
from datetime import datetime
from time import sleep

window = Tk()
window.title("")
window.geometry('350x150')


def sound_alarm():
    mixer.music.load('the-score-revolution.ogg')
    mixer.music.play()


def alarm():
    while True:
        control = 1
        print(control)

        alarm_hour = '09'
        alarm_minute = '58'
        alarm_sec = '00'
        alarm_period = "PM".upper()

        now = datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print('Time to take a break')

                            sound_alarm()
        sleep(1)


mixer.init()
alarm()

window.mainloop()


# for i in range(1, 4):
#     for j in range(1, i + 3):
#         print('c', end=' ')
#     print('')
#
# for i in range(1, 6):
#     print('given', i, 'the corresponding area of square is ', (i * i))
#
# for i in range(-5, 6, 2):
#     print(i, end='  ')
#
# first_name = (input('\nenter the ur name:'))
# if first_name == 'gowrish':
#     print('found')
# elif first_name == '':
#     print('my crush')
# elif first_name == 'dilip':
#     print('found')
# elif first_name == 'ashish':
#     print('found')
# else:
#     print('data does not match')
#
# name = input('\nenter the name of ur gf')
# print(f'\nhello, {name}')
#
# number = int(input('enter the number'))
#
# if number <= 8:
#     print(f'the table is ready.')
# else:
#     print(f'more then  {number} means u have to wait')
#
#
# num = int(input('enter the number'))
#
# if num % 10 == 0 :
#     print(f'{num} is multiple of 10')
# else:
#     print('not multiple')
#
