x=int(input("Enter your age: "))
y=input("Are you a student? (Yes/No): ").lower()

if x<=12 or ((x>=13 and x<=18) and y=="yes"):
    print("you are eligible for the discount in the movie ticket")
else:
    print("you are not eligible for the discount in the movie ticket")
