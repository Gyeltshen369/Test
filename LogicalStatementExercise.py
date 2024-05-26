x = int(input("Enter your age: "))
y = str(input("Are you student? (yes/no) "))

if x == 12 or x < 12 and y =="yes":
    print("You are eligible for a discount on the movie ticket. ")

elif x > 13 or x == 13 and y =="yes":
    print("You are eligible for a discount on the movie ticket. ")

elif x > 13 or x == 13 and y =="no":
    print("You are not eligible for a discount on the movie ticket. ")

else: 
    print("You are not eligible for a discount on the movie ticket. ")

