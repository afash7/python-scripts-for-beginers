def main():
    phone_number = input("Enter your phone number: ")

    password = input("Enter pin number(4 digits) : ")

    print("empty boxes: ")
    for i in range(1, 31):
        print(f"box number {i}")

    box_number = input("Enter the box number you want to open: ")
    print(f"box number {box_number} is open.")

    door_status = input("did you close the box?(y/n) : ").strip().lower()

    if door_status == "n":
        print("please close the box.")
        door_status = input("did you close the box?(y/n) : ").strip().lower()

    if door_status == "y":
        phone_number = input("Enter your phone number: ")

        entered_password = input("Enter pin number(4 digits) : ")

        if entered_password == password:
            print(f"the box number {box_number} is open.")
            items_taken = input("Did you pick up your belongings? (Yes/no):").strip().lower()
            if items_taken == "y":
                print("please close the box.")
                final_status = input("did you close the box?(y/n) : ").strip().lower()
                if final_status == "y":
                    print("bye ")
                else:
                    print("please close the box.")
            else:
                print("Please take your belongings.")
        else:
            print("invalid pin")
    else:
        print("please close the box.")

if __name__ == "__main__":
    main()


