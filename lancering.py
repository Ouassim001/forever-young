import time

print("de raketlancering zal over 30 seconden plaatsvinden")
time.sleep(1)

for lancering in range(29,-1,-1):
    time.sleep(1)
    print(lancering)
   

if lancering == 0:
    print("raket is gelanceerd")