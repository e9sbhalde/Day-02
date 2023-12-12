
def answer():
 Total_num= 4000000
 number1 = 0
 number2 = 1
 sum= 0

 while number2 < Total_num : 
    number3= number1 + number2
    number1 = number2
    number2 = number3
    if number3 % 2== 0:
     sum += number3
 return sum
    
print(answer())