#. .venv/bin/activate
from flask import Flask, json
import time
import smbus


#*****************************************
i2c_ch = 1

# TMP102 address on the I2C bus
i2c_address = 0x48

# Register addresses
reg_temp = 0x00
reg_config = 0x01

# Calculate twos_comp(val, bits):
def twos_comp(val, bits):
	if (val & (1 << (bits - 1))) != 0:
		val = val - (1 << bits)
	return val

# Read temperature registers 
def read_temp():
	val = bus.read_i2c_block_data(i2c_address, reg_temp, 2)
	temp_c = (val[0] << 4) | (val[1] >> 4)
	temp_c = twos_comp(temp_c, 12)
	temp_c = temp_c * 0.0625
	# Celsius to fehrenheit 
	temp_c = (9/5 * temp_c) + 32
	return temp_c

bus = smbus.SMBus(i2c_ch)

val = bus.read_i2c_block_data(i2c_address, reg_config, 2)
print("Old CONFIG:", val)

val[1] = val[1] & 0b00111111
val[1] = val[1] | (0b10 << 6)

bus.write_i2c_block_data(i2c_address, reg_config, val)

val = bus.read_i2c_block_data(i2c_address, reg_config, 2)
print("New CONFIG:", val)

#*****************************************************



api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
	global companies
	temperature = round(read_temp(), 2)
	#companies = [{"temp": temperature}]
	companies = "temp, light\n" + str(temperature) + ", 0"
	#return json.dumps(companies)
	return companies

if __name__ == '__main__':
	api.run()
	
	
