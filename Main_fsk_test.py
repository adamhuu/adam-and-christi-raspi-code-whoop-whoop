import time
import FSK_test
import busio
from digitalio import DigitalInOut, Direction, Pull
import board


CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK,MOSI=board.MOSI, MISO=board.MISO)

rfm9x = FSK_test.RFM9x(spi, CS, RESET, 915.0)

rfm9x.tx_power = 23

current_temp = rfm9x.temperature_value()

rfm9x.configure_temperature_threshold(5)

rfm9x.gaussian_filter_calibration(10)

print("gaussian filter is ",rfm9x.current_gaussian_filter_used(), "BT")

data=bytes("please work","utf-8")

print("How many packets do you want sent?:")
num_of_packets = input()

print("what gaussian filter setting?:")

gauss_fil = input()

rfm9x.gaussian_filter_calibration(gauss_fil)

print("temp threshold?:")

thresh = input()

rfm9x.configure_temperature_threshold(thresh)

print("what is the desired bitrate?")

bitrate_select = input()

rfm9x.bitrate = float(bitrate_select)



while True:
       
    rfm9x.send(data)
    
    print("data sent")
    
    print(rfm9x.temp_threshold)
    
    print(current_temp)
    
    time.sleep(2)
    
    print(data)
    
    num_of_packets = int(num_of_packets) - 1
    
    if num_of_packets == 0:
        
        print("transmission over")
        
        break
    
    

