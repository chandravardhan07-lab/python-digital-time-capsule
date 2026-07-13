from datetime import datetime

print("===== DIGITAL TIME CAPSULE =====")

choice = input("Do you want to (1) Save a message or (2) Open a message? ")

filename = "capsule.txt"

if choice == "1":
    message = input("Enter your secret message: ")
    unlock_date = input("Enter unlock date (YYYY-MM-DD): ")

    with open(filename, "w") as file:
        file.write(unlock_date + "\n")
        file.write(message)

    print("\n✅ Your message has been locked successfully!")

elif choice == "2":
    try:
        with open(filename, "r") as file:
            unlock_date = file.readline().strip()
            message = file.read()

        today = datetime.now().date()
        unlock = datetime.strptime(unlock_date, "%Y-%m-%d").date()

        if today >= unlock:
            print("\n🔓 Time Capsule Opened!")
            print("Your Message:")
            print(message)
        else:
            print("\n🔒 This capsule is still locked.")
            print("It will unlock on:", unlock_date)

    except FileNotFoundError:
        print("No time capsule found. Please create one first.")

else:
    print("Invalid choice!")