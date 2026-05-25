import network
import urequests
import gc
import time
from machine import Pin, I2C
import ssd1306

# OLED setup (your working pins)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=50000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# WiFi
SSID = ""
PASSWORD = ""

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

oled.fill(0)
oled.text("Connecting WiFi", 0, 0)
oled.show()

# wait for WiFi
for i in range(15):
    if wifi.isconnected():
        break
    time.sleep(1)

if not wifi.isconnected():
    oled.fill(0)
    oled.text("WiFi Failed", 0, 0)
    oled.show()
    raise Exception("No WiFi")

oled.fill(0)
oled.text("WiFi OK", 0, 0)
oled.show()
time.sleep(1)

URL = "http://wttr.in/Lucknow?format=j1"

while True:
    try:
        gc.collect()  # IMPORTANT for stability

        res = urequests.get(URL)
        data = res.json()

        temp = data["current_condition"][0]["temp_C"]
        desc = data["current_condition"][0]["weatherDesc"][0]["value"]

        oled.fill(0)
        oled.text("Lucknow", 0, 0)
        oled.text("Temp: " + str(temp) + "C", 0, 20)
        oled.text(desc[:16], 0, 40)
        oled.show()

        res.close()

    except Exception as e:
        oled.fill(0)
        oled.text("ERROR", 0, 0)
        oled.text(str(e)[:20], 0, 20)
        oled.show()

    time.sleep(10)
