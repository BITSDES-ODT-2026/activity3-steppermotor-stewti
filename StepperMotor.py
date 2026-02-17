from machine import Pin
import time

in1 = Pin(5,Pin.OUT)
in2 = Pin(14,Pin.OUT)
in3 = Pin(15,Pin.OUT)
in4 = Pin(19,Pin.OUT)

kio = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
oink = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

while True:
    for v in range(500):
        for i in kio:
            in1.value(i[0])
            in2.value(i[1])
            in3.value(i[2])
            in4.value(i[3])
            time.sleep_ms(5)
    for t in range(500):
        for j in oink:
            in1.value(j[0])
            in2.value(j[1])
            in3.value(j[2])
            in4.value(j[3])
            time.sleep_ms(5)
          
