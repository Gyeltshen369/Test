number = int(input("Enter the number for which you want the multiplication table : "))
mult_num = int(input("Enter the limit up to which you want the table generate: "))

i = 1
print(f"Multiplication table of {number} : ")
while i <= mult_num :
    multiplication = number * i 
    print(f"{number} x {i} = {multiplication}")
    i+=1

    

    






