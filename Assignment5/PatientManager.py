# TODO: complete this clas
import sys
import copy


# @ author  - Alex Guntermann -
class PatientManagement:
    # initializer method with 3 properties
    def __init__(self):
        while True:
            try:
                self.patient_dict = {}

                self.file_name = input("Enter the file Name: ")
                self.read_patients_file(self.file_name)

            except FileNotFoundError:
                print("Sorry that file was not found! Please input try another")


    # read patients from the file and save them to a dictionary.
    def read_patients_file(self, file_name):

        try:

            with open(file_name, "r") as inFile:
                count = 0
                # for each line in hte file,
                for line in inFile:
                    # if the end of the line is a break to a new line then..
                    if line[len(line) - 1] == "\n":
                        # the dictionary at key value of count is equal to the line split from beginning to last
                        # not including the new line
                        self.patient_dict[count] = line[:-1].split(',')
                    else:
                        # else add to the dictionary at key value of count and create a new string every time a comma
                        # is reached
                        self.patient_dict[count] = line.split(',')
                    # increment the counter so the index of the patient can be known
                    count += 1


                    # brainstorming idea on nested dictionary
                    # (name, ssn, age, diagnosis) = line.strip().split(',')
                    # self.patient_dict[name] = ssn,age,diagnosis
                    # self.patient_dict[name]["SSN"] = ssn
                    # self.patient_dict[name]["AGE"] = age
                    # self.patient_dict[name]["DIAGNOSIS"] = diagnosis
            # prints out the length of the dictionary, which counts the keys and lets the user know how many
            # patients were read from the file and stored
            print(str(len(self.patient_dict)) + " Patients have been loaded")

            self.main_menu()
        except FileNotFoundError:
            print("The file was not found")
        except OSError:
            print("File exists. Error reading file")

    def main_menu(self):

        # this method displays all possible fuctions and depends on user input
        print("\n* * * * * * * * * * * MAIN MENU* * * * * * * * * * * ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
        print("1. Add Patient\n" +
              "2. View Patient at Specific Index\n" +
              "3. View all patients\n" +
              "4. Search for a Patient\n" +
              "5. Exit\n")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

        while True:
            try:
                # prompt the user to choose an option from 1 to 5
                userNumber = input("Please input a valid integer option: ")
                userNumber = int(userNumber)
                # Add Patient
                if (userNumber == 1):
                    self.add_patient()
                # View Patient at Specific Index
                elif (userNumber == 2):
                    print("There are: " + str(
                        len(
                            self.patient_dict)) + " patients in the file." + " Please select a valid index between 0 and "
                          + str(len(self.patient_dict) - 1))
                    try:
                        inputIndex = int(input("Please input a valid integer index: "))
                        self.find_patient_at_index(inputIndex)
                    except ValueError:
                        print("You entered an invalid index. Please select a valid index between 0 and " + str(
                            len(self.patient_dict) - 1))
                        inputIndex = int(input("Please input a valid integer index: "))
                        self.find_patient_at_index(inputIndex)
                # View all Patients
                elif (userNumber == 3):
                    self.show_all()
                # Find Patient with Name
                elif (userNumber == 4):
                    self.find_patient_with_name()
                # Exit Program
                elif (userNumber == 5):
                    self.call_exit()

            except ValueError:
                print("Please input a valid integer option and try again")
            else:
                print("You entered a value that was not on the menu. Please choose an integer between 1 and 5")
                self.main_menu()

    def add_patient(self):
        # promt the user to input the desired name
        name = input("Please input a first and last name to be added: ")
        # this loop allows for the user input to be only entered as a string variable
        while name.replace(" ", "").isalpha() == False:
            print("That is an invalid name. Please input a valid String as the name")
            name = ("Please input a first and last name to be added")

        ssn = input(
            "Please input a SSN to be added. It must be 10 numbers with two - included after the third and 6th number: ")
        # the format for social security numbers is xxx - xxx - xxxx, so 10 total integers with 2 characters, therefore
        # the length is 12, so if anything is under 12 or over 12 then we know to re-prompt the user until correct
        # ssn length is established
        while len(ssn) != 12:
            print("The valid input for SSN is the following: ()()()-()()()-()()()()")
            ssn = input("Please input a valid SSN.")



        ageBoolean = False
        while ageBoolean == False:
            try:

                age = int(input("Please input an age to be added: "))
                ageBoolean = True
            except ValueError:
                print("Please input a valid integer for the age field")

        diagBoolean = False
        while diagBoolean == False:
            try:
                diag = input("Please input a DIAGNOSIS to be added. It must be an integer: ")
                diagBoolean = True
            except ValueError:
                print("Please input a valid integer for the diagnosis field")
        # this create a new patient with the following fields entered by the user
        newPatient = [name, ssn, age, diag]
        # now we use our current patient dictionary and add the new patients info at the last spot, which is reachable
        # by using the length of the dictionary.
        self.patient_dict[len(self.patient_dict)] = newPatient

        print("New Patient Added")

        self.main_menu()

    def find_patient_at_index(self, ind_to_returned):
        if ind_to_returned > len(self.patient_dict) - 1 or ind_to_returned < 0:
            print("Invalid Index!")
            print("There are: " + str(
                len(self.patient_dict)) + "patients in the file." + " Please select a valid index between 0 and "
                  + str(len(self.patient_dict) - 1))
            ind_to_returned = int(input("Please enter a valid index"))
            self.find_patient_at_index(ind_to_returned)
        else:
            indexPatient = copy.deepcopy(self.patient_dict[ind_to_returned])

            print("NAME\t\tSSN\t\t\t\t\t\tAGE\t\t\t\tDIAGNOSIS\n"
                  "----------------------------------------------------------------------------\n" + str(
                indexPatient[0]) +
                  "\t"
                  + str(indexPatient[1]) + "\t\t\t" + str(indexPatient[2]) + "\t\t\t\t" + str(indexPatient[3]))

            self.main_menu()

    def show_all(self):

        print("Here are all of patients: ")

        print("NAME\t\tSSN\t\t\t\t\t\tAGE\t\t\t\tDIAGNOSIS\n"
              "----------------------------------------------------------------------------\n")
        # loop through the values contained in the patient dictionary
        for patients in self.patient_dict.values():
            # an individual copy of the patients is made
            listof = copy.deepcopy(patients)
            # print each of the values stored at each index of the copied list. This includes name,ssn,age,diagnosis
            print(str(listof[0]) + "\t" + str(listof[1]) + "\t\t\t" + str(listof[2]) + "\t\t\t\t" + str(listof[3]))
            print("----------------------------------------------------------------------------\n")
        # calls back to the main menu
        self.main_menu()

    def find_patient_with_name(self):
        searchName = input("Please input a name to search for: ")
        try:
            # serach through the keys and values of the patient dictionary. If one of the values match, then save that
            # index. This means that the name being searched for exists
            patientLocation = [key for key, value in self.patient_dict.items() if value[0].lower() == searchName.lower()][0]
            # make a copy of the elements located at the index or "key" stored as "patientLocation"
            searchedFor = copy.deepcopy(self.patient_dict[patientLocation])

            print("----------------------------------------------------------------------------\n")
            print("NAME\t\tSSN\t\t\t\t\t\tAGE\t\t\t\tDIAGNOSIS\n"
                  "----------------------------------------------------------------------------\n")

            # print each of the elements from deep copied list from patient dictionary
            print(str(searchedFor[0]) + "\t" + str(searchedFor[1]) + "\t\t\t" + str(searchedFor[2]) + "\t\t\t\t" + str(
                searchedFor[3]))

            self.main_menu()
        except Exception:
            print("The name you are searching for does not exist in our records.")
            self.main_menu()

            # for key in self.patient_dict.items():
            #     if self.patient_dict.items() == searchName:
            #         print(self.patient_dict[searchName])
            # else:
            #     print("The person you are searching for does not exist.")

    def call_exit(self):

        print("\nThank you!\nNow exiting...")
        # set counter to 1 because of list-like indexing
        file_line_count = 1
        # open the file in reading mode
        with open(self.file_name, "r") as inFile:
            # increment i and read for every line inside the file
            for i, line in enumerate(inFile):
                pass
            # add the count of i to our counter
            file_line_count += i
            # close the file
            inFile.close()
        # if the length of our patient dictionary is greater than our file, then we know to write
        # newly added patients to the file
        if file_line_count < len(self.patient_dict):
            # find the end of the file by taking dict length minus the total lines
            filePointer = len(self.patient_dict) - file_line_count
            # open the file
            with open(self.file_name, "a") as outFile:
                # loop only from the desired index to the end -1
                for k in range(len(self.patient_dict) - filePointer, len(self.patient_dict)):
                    # create a new string that appends the patient information separated by commas at the desired
                    # located of k, which was established by the for loop above this comment
                    newPerson = ','.join(str(patientInfo) for patientInfo in self.patient_dict[k])
                    # we need to signify a new line at the end of each line
                    outFile.write("\n")
                    # once we skip to a new line, we write our newly created string that contains all of the patients
                    # information in a comma separated line.
                    outFile.write(newPerson)
                # close file
                outFile.close()
            # sucessfully exit the program
            sys.exit()
        else:
            print("No new patients were added during this run, so no patients will be written to the file"
                  " \nThanks for using this program!")
            # this gets reached if the length of lines in the file is the same as the length of the dictionary
            # storing the patients value
            sys.exit()


examp = PatientManagement()
