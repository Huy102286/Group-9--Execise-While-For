cel = 0
far = (cel * 9/5) + 32
print("Celcious  <->  Fahrenheit")

for i in range(100):    
    print(i  ,'<->',  far)    
    cel += 1
    far = (cel * 9/5) + 32
    