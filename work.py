def main():
    class_dictionary = {
        "class_1" : [
            ("Ama", 80, 70, 60),
            ("Kojo", 85, 71, 30),
            ("Kwame", 60, 44, 87),
            ("Kwesi", 40, 70, 20),
            ("Ernest", 74, 32, 10),
            ("Abena", 34, 57, 68),
            ("Araba", 80, 70, 60),
            ("Kelvin", 85, 43, 34),
            ("Patience", 60, 50, 60),
            ("Dale", 90, 90, 90)
            ],
        "class_2" : [
            ("Fifi", 78, 70, 50),
            ("Sisi", 35, 78, 87),
            ("Jessy", 44, 76, 57),
            ("Daniel", 80, 48, 56),
            ("Aba", 80, 70, 60),
            ("Yaa", 19, 65, 24),
            ("Christabel", 68, 49, 32),
            ("Julia", 97, 56, 89),
            ("Kevin", 44, 76, 87),
            ("Beth", 78, 67, 57)
            ],
        "class_3" : [
            ("Seth", 85, 75, 95),
            ("Adam", 25, 35, 22),
            ("Eve", 76, 59, 70),
            ("Ruth", 55, 50, 60),
            ("Nathaniel", 87, 67, 88),
            ("Marfo", 80, 50, 60),
            ("Esther", 85, 78, 90),
            ("Sam", 70, 80, 50),
            ("Alfred", 55, 67, 87),
            ("Richard", 88, 87, 93)
            ]
    }
    
    class_1_scores = list_for_class_1(class_dictionary)
    class_2_scores = list_for_class_2(class_dictionary)
    class_3_scores = list_for_class_3(class_dictionary)
    average_score_for_student = average_score_across_all_subjects(class_1_scores,class_2_scores,class_3_scores)
    
    
    
    class_average_in_each_subject(class_1_scores,class_2_scores,class_3_scores)
    best_score_in_each_subject(class_1_scores,class_2_scores,class_3_scores)
    worst_score_in_each_subject(class_1_scores,class_2_scores,class_3_scores)
    average_score_across_all_subjects(class_1_scores,class_2_scores,class_3_scores)
    best_overall_student(average_score_for_student)
    
    
def list_for_class_1(class_dictionary):
    class_1_list = []
    class_1_students = []
    class_1_score_science = []
    class_1_score_math = []
    class_1_score_english = []
    
    # For class 1
    for lists_in_dictionary in class_dictionary["class_1"]:
        class_1_list.append(lists_in_dictionary)
    
    for each_tuple in class_1_list:
        class_1_students.append(each_tuple[0])
        class_1_score_science.append(each_tuple[1])
        class_1_score_math.append(each_tuple[2])
        class_1_score_english.append(each_tuple[3])

    return class_1_score_science,class_1_score_math,class_1_score_english, class_1_students


def list_for_class_2(class_dictionary):
    class_2_list = []
    class_2_students = []
    class_2_score_science = []
    class_2_score_math = []
    class_2_score_english = []
    
    # For class 2
    for lists_in_dictionary in class_dictionary["class_2"]:
        class_2_list.append(lists_in_dictionary)
    
    for each_tuple in class_2_list:
        class_2_students.append(each_tuple[0])
        class_2_score_science.append(each_tuple[1])
        class_2_score_math.append(each_tuple[2])
        class_2_score_english.append(each_tuple[3])

    return class_2_score_science,class_2_score_math,class_2_score_english,class_2_students
    
    
def list_for_class_3(class_dictionary):
    class_3_list = []
    class_3_students = []
    class_3_score_science = []
    class_3_score_math = []
    class_3_score_english = []
    
    # For class 3
    for lists_in_dictionary in class_dictionary["class_3"]:
        class_3_list.append(lists_in_dictionary)
    
    for each_tuple in class_3_list:
        class_3_students.append(each_tuple[0])
        class_3_score_science.append(each_tuple[1])
        class_3_score_math.append(each_tuple[2])
        class_3_score_english.append(each_tuple[3])


    return class_3_score_science,class_3_score_math,class_3_score_english,class_3_students
    
    
def class_average_in_each_subject(class1_scores, class2_scores, class3_scores):
    class1_science = class1_scores[0]
    class1_math = class1_scores[1]
    class1_english = class1_scores[2]
    
    class2_science = class2_scores[0]
    class2_math = class2_scores[1]
    class2_english = class2_scores[2]
    
    class3_science = class3_scores[0]
    class3_math = class3_scores[1]
    class3_english = class3_scores[2]
    
    class1_science_average = sum(class1_science) / len(class1_science)
    class1_math_average = sum(class1_math) / len(class1_math)
    class1_english_average = sum(class1_english) / len(class1_english)
    
    class2_science_average = sum(class2_science) / len(class2_science)
    class2_math_average = sum(class2_math) / len(class2_math)
    class2_english_average = sum(class2_english) / len(class2_english)
    
    class3_science_average = sum(class3_science) / len(class3_science)
    class3_math_average = sum(class3_math) / len(class3_math)
    class3_english_average = sum(class3_english) / len(class3_english)
    
    
    print("The Class 1 average for Science is: ", class1_science_average, 
        "for Math is: ", class1_math_average, " for English is : ", class1_english_average)
    
    print("The Class 2 average for Science is: ", class2_science_average,
        "for Math is: ", class2_math_average, " for English is : ", class2_english_average)
    
    print("The Class 3 average for Science is: ", class3_science_average, 
        "for Math is: ", class3_math_average, " for English is : ", class3_english_average)


def best_score_in_each_subject(class1_scores,class2_scores,class3_scores):
    class1_science = class1_scores[0]
    class1_math = class1_scores[1]
    class1_english = class1_scores[2]
    
    class2_science = class2_scores[0]
    class2_math = class2_scores[1]
    class2_english = class2_scores[2]
    
    class3_science = class3_scores[0]
    class3_math = class3_scores[1]
    class3_english = class3_scores[2]
    
    class1_maximum_science = max(class1_science)
    class1_maximum_math = max(class1_math)
    class1_maximum_english = max(class1_english)
    
    class2_maximum_science = max(class2_science)
    class2_maximum_math = max(class2_math)
    class2_maximum_english = max(class2_english)
    
    class3_maximum_science = max(class3_science)
    class3_maximum_math = max(class3_math)
    class3_maximum_english = max(class3_english)
    
    print("The Class 1 best for Science is: ", class1_maximum_science, 
        "for Math is: ", class1_maximum_math, " for English is : ", class1_maximum_english)
    
    print("The Class 2 best for Science is: ", class2_maximum_science,
        "for Math is: ", class2_maximum_math, " for English is : ", class2_maximum_english)
    
    print("The Class 3 best for Science is: ", class3_maximum_science, 
        "for Math is: ", class3_maximum_math, " for English is : ", class3_maximum_english)
        
        
def worst_score_in_each_subject(class1_scores,class2_scores,class3_scores):
    class1_science = class1_scores[0]
    class1_math = class1_scores[1]
    class1_english = class1_scores[2]
    
    class2_science = class2_scores[0]
    class2_math = class2_scores[1]
    class2_english = class2_scores[2]
    
    class3_science = class3_scores[0]
    class3_math = class3_scores[1]
    class3_english = class3_scores[2]
    
    class1_minimum_science = min(class1_science)
    class1_minimum_math = min(class1_math)
    class1_minimum_english = min(class1_english)
    
    class2_minimum_science = min(class2_science)
    class2_minimum_math = min(class2_math)
    class2_minimum_english = min(class2_english)
    
    class3_minimum_science = min(class3_science)
    class3_minimum_math = min(class3_math)
    class3_minimum_english = min(class3_english)
    
    print("The Class 1 worst for Science is: ", class1_minimum_science, 
        "for Math is: ", class1_minimum_math, " for English is : ", class1_minimum_english)
    
    print("The Class 2 worst for Science is: ", class2_minimum_science,
        "for Math is: ", class2_minimum_math, " for English is : ", class2_minimum_english)
    
    print("The Class 3 worst for Science is: ", class3_minimum_science, 
        "for Math is: ", class3_minimum_math, " for English is : ", class3_minimum_english)


def average_score_across_all_subjects(class1_scores,class2_scores,class3_scores):
    class1_science = class1_scores[0]
    class1_math = class1_scores[1]
    class1_english = class1_scores[2]
    class1_students = class1_scores[3]
    
    class2_science = class2_scores[0]
    class2_math = class2_scores[1]
    class2_english = class2_scores[2]
    class2_students = class2_scores[3]
    
    class3_science = class3_scores[0]
    class3_math = class3_scores[1]
    class3_english = class3_scores[2]
    class3_students = class3_scores[3]
    
    print("Average Score for Class 1")
    for l in range(len(class1_english)):
        average_score_for_student_class1 = (class1_science[l] + class1_math[l] + class1_english[l]) / 3
        print("The average score for ", class1_students[l], " across all subjects is: ", average_score_for_student_class1) 
        
        
    print("Average Score for Class 2")
    for l in range(len(class2_english)):
        average_score_for_student_class2 = (class2_science[l] + class2_math[l] + class2_english[l]) / 3
        print("The average score for ", class2_students[l], " across all subjects is: ", average_score_for_student_class2) 
        
        
    print("Average Score for Class 3")
    for l in range(len(class3_english)):
        average_score_for_student_class3 = (class3_science[l] + class3_math[l] + class3_english[l]) / 3
        print("The average score for ", class3_students[l], " across all subjects is: ", average_score_for_student_class3) 
        
     
    return average_score_for_student_class1,average_score_for_student_class2,average_score_for_student_class3
    
def best_overall_student(average_score_for_student):
    average_score_for_student_class_1 = average_score_for_student[0]
    average_score_for_student_class_2 = average_score_for_student[1]
    average_score_for_student_class_3 = average_score_for_student[2]
    
    best_student = max(average_score_for_student_class_1,average_score_for_student_class_2,average_score_for_student_class_3)
    
    print("The best student had: ", best_student, " as the best overall grade")

if __name__ == "__main__":
    main()