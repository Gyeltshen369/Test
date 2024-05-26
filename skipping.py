for i in range(1,10):
    print(i)
    if i==3:
        print("Skipping 3 in innner loop")
        continue

    if i==7:
        print("Reached 7 breaking outer loop")
        break
    
    