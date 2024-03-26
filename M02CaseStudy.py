############################################
##   Ryan Hayes
##   M02 Case Study GPATester
##   App accepts student first and last names and GPA, and tells whether the student made the honor roll or Dean's list.
############################################
def process_student_records():
    while True:
        # Ask for and accept the student's last name
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
        if last_name.lower() == 'zzz':
            print("Quitting student records processing.")
            break
        
        # Ask for and accept the student's first name
        first_name = input("Enter the student's first name: ")
        
        # Initialize GPA variable
        gpa = None
        
        # Keep asking for GPA until a valid float is entered
        while gpa is None:
            try:
                gpa_input = input("Enter the student's GPA: ")
                gpa = float(gpa_input)
                if gpa < 0 or gpa > 4.0: # Assuming GPA scale is 0.0 to 4.0
                    print("Please enter a GPA between 0.0 and 4.0.")
                    gpa = None
            except ValueError:
                print("Invalid GPA entered. Please enter a numeric value.")
        
        # Capitalize the first and last names
        first_name = first_name.capitalize()
        last_name = last_name.capitalize()
        
        # Test if the student's GPA is 3.5 or greater
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        # Test if the student's GPA is 3.25 or greater
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for the Dean's List or the Honor Roll.")

if __name__ == "__main__":
    process_student_records()
