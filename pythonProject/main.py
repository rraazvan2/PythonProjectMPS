from datetime import datetime

import mysql.connector
import serial.tools.list_ports

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    port='3306',
    database="Test123"
)

serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = "COM4"
serialInst.timeout = 1
serialInst.open()
''' What time period in second when you want to insert de value in table '''
CounterTemperature = 60
counter = CounterTemperature/2
b = 10

while True:
    if serialInst.in_waiting:
        packet = serialInst.read(20)
        counter += 1
        if counter == b:
            if len(packet.decode('utf').rstrip('\n')) > 18:
                mycursor = db.cursor()
                mycursor.execute("INSERT INTO DHT11 (Name,TempAndUmidity,DateAndTime) VALUES (%s, %s, %s)", ("Timisoara", packet.decode('utf').rstrip('\n'), datetime.now()))
                db.commit()
                counter = 0
