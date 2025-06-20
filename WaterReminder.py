import time

print("Hours to get reminded of:")
while True:
	try:
		reminder_hour = float(input("--> "))
		if reminder_hour == 0:
			raise
		break
	except:
		print("Enter valid hour.")
print(f"Reminder started for {reminder_hour} hour.")
while True:
	time.sleep(reminder_hour*3600)
	print(f"{reminder_hour} hours are done, drink water.")