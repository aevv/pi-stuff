from subprocess import check_output

def get_temp():
	return check_output(["cat"], "/sys/class/thermal/thermal_zone0/temp"])

def format_temp():
	fl_temp = float(temp) / 1000
	return "Current CPU Temp: %0.2fC" % fl_temp

print format_temp(get_temp())