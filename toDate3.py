def toDate3(date):
	import time,datetime
	dt = date+datetime.timedelta(hours=9)
	
	return dt

if __name__ == "__main__":
	import datetime
	date = "2008-02-24 06:39:37"
	
	print toDate3(date)
	print datetime.datetime.today()
	
