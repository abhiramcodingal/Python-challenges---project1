# Python program to convert integer value to roman values

# Class to conert integer to Roman Values

class Roman:
    def __init__(self,givennum):
        self.givennum = givennum
        
    def printRoman(self,number):
        num = [1, 4, 5, 9, 10, 40, 50, 90,
            100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
     
        while number:
            div = number // num[i]
            number %= num[i]
         
            while div:
                print(sym[i], end = "")
                div -= 1
            i -= 1
         
# Main Program
num1 = int(input("Enter a integer value <= 3999: "))
objRoman = Roman(num1)
print("Roman value is:", end = " ")
objRoman.printRoman(num1)