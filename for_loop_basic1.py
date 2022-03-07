"""
1. Basic - Print all integers from 0 to 150.

for i in range(150):
    print(i)
"""
"""
2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range (1000):
    if i%5 == 0:
        print(i)
"""
"""
3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for i in range(1,101):
    if i%10 == 0:
        print("Coding Dojo")
    elif  i%5 == 0:
        print("Coding")
    else: 
        print(i)
"""
"""
4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

Oddtotal = 0

for num in range(1, 500000+1):
    if num%2 != 0:
        Oddtotal = Oddtotal + num
        print(Oddtotal)
"""
"""
5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for pos in range(2018,1, -4):
    if pos%2 == 0:
        print(pos)
"""
"""
6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 15
highNum = 84
mult = 9
for i in range(lowNum, highNum):
    if i%mult == 0:
        print(i)
"""
