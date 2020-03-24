from datetime import datetime

# Convert strings to datetime objects

# Convert hh:mm time string to datetime object
def str_to_time(time_str):
	d = datetime.strptime(time_str,"%H:%M")
	return d

# Convert from date string of custom format to datetime object
def str_to_date(date_str, date_format):
	d = datetime.strptime(date_str, date_format)
	return d
# Get datetime object from a time string
def get_time_str(time_str):
	d = str_to_time(time_str)
	return d.time()

# Get datetime.date() object from a date string
def get_date_str(date_str, date_format="%Y-%M-%D"):
	d = str_to_date(date_str, date_format)
	return d.date()

# Get the datetime.time() object from a string of a 
# time period delimited by '-'
# Example: 12:00-15:00
# Returns a tuple with the start and end time
def get_times_from_period(period_str):
	str_list = period_str.split('-')
	start = get_time_str(str_list[0])
	end = get_time_str(str_list[1])
	time_tup = (start, end)
	return time_tup

# Test if a datetime.time() object lies between two times
# time - a tuple of datetime.time() objects
def is_between(test, times_tp):
	if (test >= times_tp[0] and test < times_tp[1]):
		return True
	else:
		return False

# Get the current date and time as a string
def now():
	return str(datetime.now())

def main():
	'''
	times = get_times_from_period('9:30-15:45')
	test = get_time_str('15:44')
	is_between(test, times[0], times[1])
	print(times[0])
	print(times[1])
	'''
	print(now())

