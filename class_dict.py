def main():
    class_dictionary = {
        'class1' : [
            ('Ama',78,82,90),
            ('James',67,83,79),
            ('Esi',89,70,88),
            ('Gideon',92,95,96),
            ('John',87,84,82),
            ('Daniel',67,45,52),
            ('Dennis',70,78,72),
            ('Solomon',80,84,86),
            ('Bright',92,82,87),
            ('Jane',58,66,80)
            ],

        'class2':[
            ('Fancis',88,86,90),
            ('Nana',72,82,83),
            ('Padi',90,73,80),
            ('Alfred',92,89,91),
            ('Serwah',86,94,93),
            ('Kate',89,84,90),
            ('Elorm',78,75,80),
            ('Maxwell',80,96,78),
            ('Andy',67,60,65),
            ('Paul',70,85,82)
            ],
        'class3':[
            ('Jones',79,76,73),
            ('Mary',56,45,60),
            ('Chris',76,72,80),
            ('Joel',82,83,81),
            ('Adwoa',78,76,87),
            ('Mawuli',97,98,93),
            ('Abena',93,97,96),
            ('Enam',89,85,90), 
            ('George',79,63,90),
            ('Edmond',86,80,82)
        ]
    }
    # first_class_list(class_dictionary)
    # average score in each subject
    student_details =  list(class_dictionary.values())
    overall_best = max(all_marks(student_details))
    overall_worst = min(all_marks(student_details))
    average_score = average_scores(all_marks(student_details))
    print(f'The overall best student had a mark of {overall_best}')
    print(f'The overall best student had a mark of {overall_worst}')
    print(f'The the average score across all classes is  {average_score}')
    first_class_scores = class1_list(class_dictionary)
    second_class_scores = class2_list(class_dictionary)
    third_class_scores = class3_list(class_dictionary)

    first_class_computations = class_computations(first_class_scores)
    second_class_computations = class_computations(second_class_scores)
    third_class_computations = class_computations(third_class_scores)
    print(f'The best students in each subject in the first class is : English - {first_class_computations[1]}, Maths  - {first_class_computations[2]},  Science  - {first_class_computations[0]}')
    
    print(f'The best students in each subject in the second class is : English - {second_class_computations[1]}, Maths  - {second_class_computations[2]},  Science  - {second_class_computations[0]}')
    print(f'The best students in each subject in the second class is : English - {third_class_computations[1]}, Maths  - {third_class_computations[2]},  Science  - {third_class_computations[0]}')


    print(f'\nThe worst students in each subject in the first class is : English - {first_class_computations[5]}, Maths  - {first_class_computations[4]},  Science  - {first_class_computations[3]}')
    
    print(f'The worst students in each subject in the second class is : English - {second_class_computations[5]}, Maths  - {second_class_computations[4]},  Science  - {second_class_computations[3]}')
    print(f'The worst students in each subject in the second class is : English - {third_class_computations[5]}, Maths  - {third_class_computations[4]},  Science  - {third_class_computations[3]}')



    print(f'\nThe average score per subject in the first class is : English - {first_class_computations[8]}, Maths  - {second_class_computations[7]},  Science  - {second_class_computations[6]}')

    print(f'The average score per subject in the second class is : English - {first_class_computations[8]}, Maths  - {first_class_computations[7]},  Science  - {first_class_computations[6]}')




    print(f'The average score per subject in the first class is : English - {third_class_computations[8]}, Maths  - {third_class_computations[7]},  Science  - {third_class_computations[6]}')


    
    
   # get all marks obtained by students

def all_marks(student_details):
    """returns a list of marks accross all classes"""
    marks = [] 
    for one_class in student_details:
        for student in one_class: 
            for item  in student: 
                if isinstance(item, int):
                    marks.append(item)
    return marks

# def classes(class_dictionary):
#     """returns a list of all classes in the dictionary"""
#     class_list = []
#     for class_name  in class_dictionary.keys():
#         class1 =  class_list.append(class_name)
#     return class_list



def class1_list(class_dictionary):
    """fetch list of all students details in the first class"""
    first_class_list = []
    first_class_students = []
    first_class_science_score = []
    first_class_maths_score = []
    first_class_english_score = []

    
    for student in class_dictionary["class1"]:
        first_class_list.append(student)

    for student  in first_class_list:
        first_class_students.append(student[0])
        first_class_science_score.append(student[1])
        first_class_maths_score.append(student[2])
        first_class_english_score.append(student[3])
        #  return tuple containing student names, and socres for respective subjects
    return first_class_students,first_class_science_score,first_class_maths_score, first_class_english_score

def class2_list(class_dictionary):
    second_class_list = []
    second_class_students = []
    second_class_science_score = []
    second_class_maths_score = []
    second_class_english_score = []
    for student in class_dictionary["class2"]:
        second_class_list.append(student)

    for student  in second_class_list:
        second_class_students.append(student[0])
        second_class_science_score.append(student[1])
        second_class_maths_score.append(student[2])
        second_class_english_score.append(student[3])
        return second_class_students,second_class_science_score,second_class_maths_score, second_class_english_score

def class3_list(class_dictionary):
    third_class_list = []
    third_class_students = []
    third_class_science_score = []
    third_class_maths_score = []
    third_class_english_score = []
    for student in class_dictionary["class3"]:
        third_class_list.append(student)

    for student  in third_class_list:
        third_class_students.append(student[0])
        third_class_science_score.append(student[1])
        third_class_maths_score.append(student[2])
        third_class_english_score.append(student[3])
        return third_class_students,third_class_science_score,third_class_maths_score, third_class_english_score

def average_scores(class_scores):
    return sum(class_scores)/len(class_scores)

def class_computations(class_scores):
    science_scores =   class_scores[1]
    math_scores =   class_scores[2]
    english_scores =   class_scores[3]
    
    max_science = max(science_scores)
    max_maths = max(math_scores)
    max_english = max(english_scores)
    
    min_science = min(science_scores)
    min_maths = min(math_scores)
    min_english = min(english_scores)


    average_science = average_scores(science_scores)
    average_maths = average_scores(math_scores)
    average_english = average_scores(english_scores)
    
    return max_science, max_english, max_maths,min_science,min_maths,min_english,average_science,average_maths,average_english




# def class_scores

if __name__ == '__main__':
    main()
    