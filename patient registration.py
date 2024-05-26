from queue import Queue

# Initialize queue for patient registration
patient_queue = Queue()

# Function to register a new patient
def register_patient():
    name = input("Enter patient's name: ")
    patient_queue.put(name)
    print("Patient registered successfully.")

# Function to remove a patient after meeting the doctor
def remove_patient():
    if patient_queue.empty():
        print("Patient queue is empty.")
    else:
        removed_patient = patient_queue.get()
        print(f"Patient {removed_patient} removed after meeting the doctor.")

# Function to display the current patient queue
def display_queue():
    if patient_queue.empty():
        print("Patient queue is empty.")
    else:
        print("\nCurrent Patient Queue:")
        for index, patient in enumerate(list(patient_queue.queue), start=1):
            print(f"{index}. {patient}")

# Main menu
while True:
    print("\n===== Desk Manager's Patient Registration System =====")
    print("1. Register Patient")
    print("2. Remove Patient after Meeting Doctor")
    print("3. Display Patient Queue")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        register_patient()
    elif choice == '2':
        remove_patient()
    elif choice == '3':
        display_queue()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
