import network
import urequests
import time
import gc
from machine import Pin, I2C
import ssd1306

# OLED (your working pins)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=50000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# WiFi
SSID = ""
PASSWORD = ""

# Telegram
BOT_TOKEN = ""
CHAT_ID = ""

# connect WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

oled.fill(0)
oled.text("Connecting WiFi", 0, 0)
oled.show()

while not wifi.isconnected():
    time.sleep(1)

oled.fill(0)
oled.text("WiFi Connected", 0, 0)
oled.show()
time.sleep(1)

offset = 0

def get_updates():
    global offset
    url = "https://api.telegram.org/bot" + BOT_TOKEN + "/getUpdates?offset=" + str(offset)
    res = urequests.get(url)
    data = res.json()
    res.close()
    return data

while True:
    try:
        gc.collect()

        data = get_updates()

        for item in data["result"]:
            offset = item["update_id"] + 1

            msg = item["message"]["text"]

            oled.fill(0)
            oled.text("Telegram Msg:", 0, 0)
            oled.text(msg[:20], 0, 20)
            oled.show()

            print("Message:", msg)

    except Exception as e:
        oled.fill(0)
        oled.text("Error:", 0, 0)
        oled.text(str(e)[:20], 0, 20)
        oled.show()

    time.sleep(2)
