import datetime

class AttendanceSystem:
    def __init__(self):
        self.attendance_record = {}

    def mark_attendance(self, person_id):
        current_date = datetime.date.today()
        if person_id not in self.attendance_record:
            self.attendance_record[person_id] = []
        self.attendance_record[person_id].append(current_date)

    def view_attendance(self, person_id):
        if person_id in self.attendance_record:
            print(f"Attendance record for {person_id}:")
            for date in self.attendance_record[person_id]:
                print(date)
        else:
            print(f"No attendance record found for {person_id}.")

    def view_all_attendance(self):
        print("All attendance records:")
        for person_id, dates in self.attendance_record.items():
            print(f"{person_id}:")
            for date in dates:
                print(date)

def main():
    attendance_system = AttendanceSystem()

    while True:
        print("\nAttendance System Menu:")
        print("1. Mark Attendance")
        print("2. View Attendance for a Person")
        print("3. View All Attendance")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            person_id = input("Enter the ID of the person: ")
            attendance_system.mark_attendance(person_id)
            print(f"Attendance marked for {person_id}.")

        elif choice == "2":
            person_id = input("Enter the ID of the person: ")
            attendance_system.view_attendance(person_id)

        elif choice == "3":
            attendance_system.view_all_attendance()

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
