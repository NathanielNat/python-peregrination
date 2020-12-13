def computeGrade(grade):
    """Function to return grades of students based on marks provided
    
    Argument = grade
    return type string
    """
    if grade > 95:
        grade =  "Top Score"
    elif grade >= 60:
        grade  =  "Pass"
    else:
        grade =  "Fail"
    return grade


def main():
    """Accept marks from user"""
    try:
        score = float(input('Enter your grade: '))
        if score > 100 or score < 0:
            print('Enter a value between 0 and 100')
        else:
            grade = computeGrade(score)
            print(grade)
    except ValueError as e:
        print('Please enter  an number')
    # score = float(input('Enter your grade: '))
    

if __name__ == "__main__" :
    main()
