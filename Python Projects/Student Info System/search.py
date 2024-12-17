class Search:
    def ownInfo(self, stud_id):
        with open('students', 'r') as file:
            student_data = []
            student_found = False

            for line in file:
                if f"ID: {stud_id}" in line:
                    student_found = True
                    student_data.append(line.strip())
                elif student_found:
                    # Collect the details until an empty line is encountered
                    if line.strip() == "":
                        break  # Stop collecting when a blank line is encountered
                    student_data.append(line.strip())

            # If student is found
            if student_found:
                # Collect the student entry details starting from the last captured data
                print("\n".join(student_data))
            else:
                print("Student with ID", stud_id, "not found.")