import time
import botbook_gpio as gpio
 
def measureDistance():
        trigPin = 22                           # ��������� ����� �������� Raspberry Pi, � �������� ��������� Trig ������� ������� HC-SR04
        echoPin = 27                           # ��������� ����� �������� Raspberry Pi, � �������� ��������� Echo ������� ������� HC-SR04
 
        v=(331.5+0.6*20)                       # �������� ����� ��� ����������� 20 �������� �������(�� ������ ������� ���� �������� ������ 20) � �/�
 
        gpio.mode(trigPin, "out")              # ������������� ������� ��� �����
 
        gpio.mode(echoPin, "in")               # ������������� ������� ��� ����
        gpio.interruptMode(echoPin, "both")    # ����� ����������, ����� ������� pulseInHigh ��������� ������������ �������� ������� � 0 �� 1 � �� 1 �� 0
 
        gpio.write(trigPin, gpio.LOW)          # ������������� ������ ������� �������
        time.sleep(0.5)                        # �������� � ��� �������
 
        gpio.write(trigPin, gpio.HIGH)         # ������������� ������� ������� �������
        time.sleep(1/1000000.0)                # �������� � 1 ���
        gpio.write(trigPin, gpio.LOW)          # ������������� ������ ������� �������
 
        t = gpio.pulseInHigh(echoPin)          # ��������� ������������ �������
 
        d = t*v*50                             # ��������� ���������� ����������
        return d                               # ���������� ��������
 
d = measureDistance()                          # �������� ������� � ��������� ������������ �������� � ����������       
print "Distance: %.2f cm" % d                  # ������� ��������