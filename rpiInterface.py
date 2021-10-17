import sys
import time
import telepot
import RPi.GPIO as GPIO
from telepot.loop import MessageLoop
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)

pwm = GPIO.PWM(16,1000)


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    print('Got command: {0} from {1}'.format(command,chat_id))
    
    if command == '/triggerAlarm':
        GPIO.output(18, GPIO.HIGH)
        pwm.start(50)
        bot.sendMessage(chat_id, 'Alarm has been triggered')
        bot.sendMessage(27838129, 'Alarm has been triggered')
    elif command == '/disableAlarm':
        GPIO.output(18, GPIO.LOW)
        pwm.stop()
        bot.sendMessage(27838129, 'Alarm has been disabled')

bot = telepot.Bot('2092432636:AAGdzPV2NYe0Jt5Jg9kI7XnwKm7kmWtqjUU')
MessageLoop(bot,handle).run_as_thread()


while True:
    sleep(30)
    
