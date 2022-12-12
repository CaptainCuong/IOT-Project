from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from aiot_lcd1602 import LCD1602
from event_manager import *
import time
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20

aiot_lcd1602 = LCD1602()

event_manager.reset()

aiot_dht20 = DHT20(SoftI2C(scl=Pin(22), sda=Pin(21)))

def on_event_timer_callback_N_t_r_F_a():
	global RT, RH, SM, LUX
	aiot_dht20.read_dht20()
	RT = aiot_dht20.dht20_temperature()
	RH = aiot_dht20.dht20_humidity()
	SM = round(translate((pin0.read_analog()), 0, 4095, 0, 100))
	LUX = round(translate((pin1.read_analog()), 0, 4095, 0, 100))
	aiot_lcd1602.move_to(0, 0)
	aiot_lcd1602.putstr('RT:')
	aiot_lcd1602.move_to(3, 0)
	aiot_lcd1602.putstr(RT)
	aiot_lcd1602.move_to(7, 0)
	aiot_lcd1602.putstr('*C ')
	aiot_lcd1602.move_to(10, 0)
	aiot_lcd1602.putstr('RH:')
	aiot_lcd1602.move_to(13, 0)
	aiot_lcd1602.putstr(RH)
	aiot_lcd1602.move_to(15, 0)
	aiot_lcd1602.putstr('%')
	aiot_lcd1602.move_to(0, 1)
	aiot_lcd1602.putstr('LUX:')
	aiot_lcd1602.move_to(4, 1)
	aiot_lcd1602.putstr(LUX)
	aiot_lcd1602.move_to(6, 1)
	aiot_lcd1602.putstr('% ')
	aiot_lcd1602.move_to(10, 1)
	aiot_lcd1602.putstr('SM:')
	aiot_lcd1602.move_to(13, 1)
	aiot_lcd1602.putstr(SM)
	aiot_lcd1602.move_to(15, 1)
	aiot_lcd1602.putstr('% ')
	print((''.join([str(x) for x in ['!1:T:', RT, '#']])), end =' ')
	print((''.join([str(x2) for x2 in ['!1:H:', LUX, '#']])), end =' ')

event_manager.add_timer_event(5000, on_event_timer_callback_N_t_r_F_a)

if True:
	display.scroll('IoT')
	aiot_lcd1602.clear()
	display.scroll('OK')

while True:
	event_manager.run()
	time.sleep_ms(1000)