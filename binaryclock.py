from time import strftime, sleep
from os import system
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# set up pins
hour16 = 4
hour8 = 17
hour4 = 27
hour2 = 22
hour1 = 5
GPIO.setup(hour16, GPIO.OUT)
GPIO.setup(hour8, GPIO.OUT)
GPIO.setup(hour4, GPIO.OUT)
GPIO.setup(hour2, GPIO.OUT)
GPIO.setup(hour1, GPIO.OUT)

minute32 = 6
minute16 = 13
minute8 = 19
minute4 = 26
minute2 = 23
minute1 = 24
GPIO.setup(minute32, GPIO.OUT)
GPIO.setup(minute16, GPIO.OUT)
GPIO.setup(minute8, GPIO.OUT)
GPIO.setup(minute4, GPIO.OUT)
GPIO.setup(minute2, GPIO.OUT)
GPIO.setup(minute1, GPIO.OUT)

second32 = 25
second16 = 12
second8 = 16
second4 = 20
second2 = 21
second1 = 18
GPIO.setup(second32, GPIO.OUT)
GPIO.setup(second16, GPIO.OUT)
GPIO.setup(second8, GPIO.OUT)
GPIO.setup(second4, GPIO.OUT)
GPIO.setup(second2, GPIO.OUT)
GPIO.setup(second1, GPIO.OUT)

try:
	while True:
#		hour = int(strftime('%H'))
#		if hour <= 4:
#			hour += 19
#		elif hour >= 5:
#			print hour
#			hour -= 5
#		print hour
		
		binary_hour = bin(int(strftime('%H')))[2:]
		binary_minute = bin(int(strftime('%M')))[2:]
		binary_second = bin(int(strftime('%S')))[2:]
		
		binary_hour = '0' * (6 - len(binary_hour)) + binary_hour
		binary_minute = '0' * (6 - len(binary_minute)) + binary_minute
		binary_second = '0' * (6 - len(binary_second)) + binary_second
		
		print binary_hour + ' ' + binary_minute + ' ' + binary_second
		
		# start console section here
		hour_values = ['O' if i == '0' else 'X' for i in binary_hour]
		minute_values = ['O' if i == '0' else 'X' for i in binary_minute]
		second_values = ['O' if i == '0' else 'X' for i in binary_second]	
		
		system('clear')
		print strftime('%H:%M:%S')
		print binary_hour + ' ' + binary_minute + ' ' + binary_second
		print
		for i in hour_values:
			print i,
		print
		for i in minute_values:
			print i,
		print
		for i in second_values:
			print i,
		print
		# end console section here, begin GPIO
		GPIO.output(hour16, GPIO.HIGH if binary_hour[1] == '1' else GPIO.LOW)
		GPIO.output(hour8, GPIO.HIGH if binary_hour[2] == '1' else GPIO.LOW)
		GPIO.output(hour4, GPIO.HIGH if binary_hour[3] == '1' else GPIO.LOW)
		GPIO.output(hour2, GPIO.HIGH if binary_hour[4] == '1' else GPIO.LOW)
		GPIO.output(hour1, GPIO.HIGH if binary_hour[5] == '1' else GPIO.LOW)
		
		GPIO.output(minute32, GPIO.HIGH if binary_minute[0] == '1' else GPIO.LOW)
		GPIO.output(minute16, GPIO.HIGH if binary_minute[1] == '1' else GPIO.LOW)
		GPIO.output(minute8, GPIO.HIGH if binary_minute[2] == '1' else GPIO.LOW)
		GPIO.output(minute4, GPIO.HIGH if binary_minute[3] == '1' else GPIO.LOW)
		GPIO.output(minute2, GPIO.HIGH if binary_minute[4] == '1' else GPIO.LOW)
		GPIO.output(minute1, GPIO.HIGH if binary_minute[0] == '1' else GPIO.LOW)
		
		GPIO.output(second32, GPIO.HIGH if binary_second[0] == '1' else GPIO.LOW)
		GPIO.output(second16, GPIO.HIGH if binary_second[1] == '1' else GPIO.LOW)
		GPIO.output(second8, GPIO.HIGH if binary_second[2] == '1' else GPIO.LOW)
		GPIO.output(second4, GPIO.HIGH if binary_second[3] == '1' else GPIO.LOW)
		GPIO.output(second2, GPIO.HIGH if binary_second[4] == '1' else GPIO.LOW)
		GPIO.output(second1, GPIO.HIGH if binary_second[0] == '1' else GPIO.LOW)
		
		sleep(0.5)

except KeyboardInterrupt:
	print
	raw_input('Press Enter to Exit')
	GPIO.cleanup()

print 'All Done!'
