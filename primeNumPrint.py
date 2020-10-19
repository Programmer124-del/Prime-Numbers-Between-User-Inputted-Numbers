'''
Take in the start and the end values
then print all of the prime numbers 
from that range
'''

startNum = int(input("Please enter a number: "))
endNum = int(input("Please enter a number: "))

print("Prime numbers from", startNum, "to", endNum, "is: ")

for num in range(startNum, endNum + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
