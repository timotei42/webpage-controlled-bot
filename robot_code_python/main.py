import network
import socket
from machine import PWM,Pin,Pin
from utime import sleep

pwm_frq=50 #defining pwm frequency

signal_sv1 = PWM(Pin(5))
signal_sv1.freq(pwm_frq)

signal_sv2 = PWM(Pin(4))
signal_sv2.freq(pwm_frq)

#defining starting positions
pos_sv_1=1000
pos_sv_2=1000

#defining the value of the step(how much the servo will move at each iteration)
STEP=500

def move_servo (position,signal):
    signal.duty_u16(position)
    sleep(0.01)
    
def pos_init():
    move_servo(pos_sv_1,signal_sv1)
    move_servo(pos_sv_2,signal_sv2)


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
#write the name of your wifi and password here
network_name=""
network_password=""
wlan.connect(network_name, network_password)

#wait for connection
max_wait = 7
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('Waiting for connection...')
    sleep(1)

#error case
if wlan.status() != 3:
    raise RuntimeError('Network connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print('IP:', status[0])

#open socket at port 80
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
pos_init()
#begin listening to requests
while True:
    try:
        cl, addr = s.accept()
        request = cl.recv(1024)
        print(request)
        request = str(request)
        mov1 = request.find('/mov1')
        mov2 = request.find('/mov2')
        mov3 = request.find('/mov3')
        mov4 = request.find('/mov4')
        if mov1 == 6:
            for pos in range(pos_sv_1,pos_sv_1+STEP,50):
                move_servo(pos,signal_sv1)
            pos_sv_1=pos_sv_1+STEP
        if mov2 == 6:
            for pos in range(pos_sv_1,pos_sv_1-STEP,-50):
                move_servo(pos,signal_sv1)
            pos_sv_1=pos_sv_1-STEP
        if mov3 == 6:
            for pos in range(pos_sv_2,pos_sv_2-STEP,-50):
                move_servo(pos,signal_sv2)
            pos_sv_2=pos_sv_2-STEP
        if mov4 == 6:
            for pos in range(pos_sv_2,pos_sv_2+STEP,50):
                move_servo(pos,signal_sv2)
            pos_sv_2=pos_sv_2+STEP
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/plain\r\n\r\n')
        cl.send("Command received")
        cl.close()

    except OSError as e:
        cl.close()
        print('Connection closed')
