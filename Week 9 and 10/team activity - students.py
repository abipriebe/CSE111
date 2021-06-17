import pandas as pd

def main():
    student_dict = create_student_dict()
    print(student_dict)
    get_inumber(student_dict)
    print()
 
def create_student_dict():
    student_dict = pd.read_csv('Week 9 and 10/students.csv', header=0, index_col=0, squeeze=True).to_dict()
    return student_dict
 
def get_inumber(dictionary):
    INUMBER_INDEX = 0
    NAME_INDEX = 1
    i_number = int(input("Please enter an I-Number (xxxxxxxxx): "))
    if i_number not in dictionary:
        print("No such student")
    else:
        value = dictionary[i_number]
        print(value)
 
if __name__ == "__main__":
    main()