timenow= int(input("what's the time now?"))
hourswait=int(input("how long to wait?"))
alarmtime=(timenow+hourswait) % 24
print("alarmtime is ", alarmtime)

