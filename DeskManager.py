from queue import Queue

patient_queue = Queue()

while True: 
    print("1.Register Patient")
    print("2.Remove Patient")
    print("3.Display Patient Queue")
    print("4.Exit")

    choice = input("Enter the number:")

    if choice == "1":
        patient_name = input("Enter the patient name:")
        patient_queue.put(patient_name)
        print(f"{patient_name} registered Sucessfully! ")

    elif choice == "2":
        if patient_queue.empty():
            print("No patient found")
        else:
            remove_patient = input("enter the patient name:")
            patient_queue.get(remove_patient)
            print(f"patient {remove_patient}sucessfully removed!!")

    elif choice == "3":
        if patient_queue.empty():
            print("No  patient is there")
        else:
            print("Patients in queue")
            for patient in patient_queue.queue:
                print(patient)
    elif choice == "4":
        print("Leaving the queue!!")
        break
    else:
        print("Invalid choice. Try again!!!")





        
        

    
        


    





















