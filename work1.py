import csv
from collections import Counter

def student_avg_score(info, level, index):

    first_score = info[level][index]['scores'][0]
    student_name = info[level][index]['name']
    total_score = sum(info[level][index]['scores'])
    max_score = max(info[level][index]['scores'])
    min_score = min(info[level][index]['scores'])
    average = sum(info[level][index]['scores'])/len(info[level][index]['scores'])

    print('\nThe name of the student is: {}'.format(student_name))
    print('The students total score is: {}'.format(total_score))
    print('The students average score is: {}'.format(average))
    print('The students maximum score is: {}'.format(max_score))
    print('The students minimum score is: {}\n'.format(min_score))

    with open('results.csv', mode ='w') as csv_file:
        fieldnames = ['name', 'total', 'average']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

        writer.writeheader()
        writer.writerow({'name': student_name, 'total': total_score, 'average': average})



def class_sub_avg_score(info, level, sub_index):
    all_list = []
    value = 0
    
    for value in range(0, len(info[level])):
        all_list.append(info[level][value]['scores'][sub_index])
        value = value + 1
   
    total_sub_score = sum(all_list)
    avg_sub_score = sum(all_list)/len(info[level])

    print('\nTotal class score for subject is: {}'.format(total_sub_score))
    print('Average class score for subject is {}\n'.format(avg_sub_score))


def sub_best_student(info, level, sub_index):
    all_list = []
    value = 0
    
    for value in range(0, len(info[level])):
        all_list.append(info[level][value]['scores'][sub_index])
        value = value + 1    
    
    max_score = max(all_list) 
    max_index = all_list.index(max_score)
    max_student = info[level][max_index]['name']

    print(max_student,'had the best score for subject being', max_score,'\n')


def sub_worst_student(info, level, sub_index):
    all_list = []
    value = 0
    
    for value in range(0, len(info[level])):
        all_list.append(info[level][value]['scores'][sub_index])
        value = value + 1    
    
    min_score = min(all_list) 
    min_index = all_list.index(min_score)
    min_student = info[level][min_index]['name']

    print('\n',min_student,'had the worst score for subject being', min_score,'\n')


def class_best_student(info, level):
    all_list = []
    value = 0

    for value in range(0, len(info[level])):
        all_list.append(sum(info[level][value]['scores']))
        value = value + 1 
    
    best_score = max(all_list)
    best_index = all_list.index(best_score)
    best_student = info[level][best_index]['name']
    
    print('\n',all_list)
    print(best_student,'is the best student in',level, 'with a total score of',best_score,'\n')


def same_score_students(info, level, sub_index, mark):
    all_list = []
    value = 0
    
    for value in range(0, len(info[level])):
        all_list.append(info[level][value]['scores'][sub_index])
        value = value + 1 
    
    print("Count displayed as:{score : number of students}")
    print(Counter(all_list))
    print(all_list.count(mark),'student(s) had a mark of ',mark)


def overall_best(info):
    all_scores = []
    all_names = []
    value = 0

    for key in info:
        for value in range(0, len(info[key])):
            all_scores.append(sum(info[key][value]['scores']))
            all_names.append(info[key][value]['name'])
    
    overall_best_mark = max(all_scores)
    overall_best_index = all_scores.index(overall_best_mark)
    overall_best_student = all_names[overall_best_index] 

    print('\n',all_names)
    print(all_scores)
    print('\nThe overall best student is',overall_best_student,'with a total score of',overall_best_mark,'\n')


def get_class_input():
    level = input('\nEnter the class the student belongs to as shown: ')
    return level


def get_sub_index():
    print("\n0. Science\n1. Mathematics\n2. Social Studies\n3. English")
    sub_index = int(input("Enter the index of the subject: "))
    return sub_index


def get_stu_index():
    index = int(input("\nEnter the index of the student: "))
    return index


def get_mark():
    mark = int(input('\nEnter mark to check frequency: '))
    print('\n')
    return mark


def main():

    info = {'class 1' :[
        {'index': 0, 'name': 'Isaac', 'scores': (75, 64, 57, 93)}, 
        {'index': 1, 'name': 'Evans', 'scores': (45, 22, 67, 75)},
        {'index': 2, 'name': 'Sarah', 'scores': (85, 87, 65, 70)},
        {'index': 3, 'name': 'Wendy', 'scores': (74, 99, 46, 62)},
        {'index': 4, 'name': 'Vera', 'scores': (85, 71, 78, 68)},
        {'index': 5, 'name': 'Kofi', 'scores': (79, 36, 45, 94)},
        {'index': 6, 'name': 'Gabby', 'scores': (85, 73, 100, 68)} 
            ],
            'class 2' :[
        {'index': 0, 'name': 'Sam', 'scores': (88, 75, 86, 91)}, 
        {'index': 1, 'name': 'Vero', 'scores': (45, 78, 45, 87)},
        {'index': 2, 'name': 'Kwame', 'scores': (79, 56, 67, 76)},
        {'index': 3, 'name': 'Johnny', 'scores': (54, 36, 39, 96)},
        {'index': 4, 'name': 'David', 'scores': (39, 79, 89, 86)},
        {'index': 5, 'name': 'Paul', 'scores': (64, 88, 51, 73)},
        {'index': 6, 'name': 'Peter', 'scores': (12, 56, 62, 35)},
        {'index': 7, 'name': 'Josh', 'scores': (46, 46, 73, 91)} 
            ],
            'class 3' :[
        {'index': 0, 'name': 'John', 'scores': (69, 65, 96, 78)}, 
        {'index': 1, 'name': 'Fred', 'scores': (39, 38, 87, 87)},
        {'index': 2, 'name': 'Kwaku', 'scores': (69, 56, 67, 76)},
        {'index': 3, 'name': 'James', 'scores': (84, 76, 59, 86)},
        {'index': 4, 'name': 'Daniel', 'scores': (69, 69, 89, 36)},
        {'index': 5, 'name': 'Patrick', 'scores': (74, 88, 51, 73)},
        {'index': 6, 'name': 'Petra', 'scores': (35, 76, 62, 35)},
        {'index': 7, 'name': 'Omar', 'scores': (56, 46, 73, 91)} 
            ],
            'class 4' :[
        {'index': 0, 'name': 'Sandra', 'scores': (88, 65, 86, 91)}, 
        {'index': 1, 'name': 'Vivian', 'scores': (85, 78, 75, 67)},
        {'index': 2, 'name': 'Kpodo', 'scores': (75, 86, 77, 76)},
        {'index': 3, 'name': 'Winner', 'scores': (59, 36, 39, 96)},
        {'index': 4, 'name': 'Ruth', 'scores': (32, 69, 59, 76)},
        {'index': 5, 'name': 'Bismark', 'scores': (48, 79, 71, 83)},
        {'index': 6, 'name': 'Robert', 'scores': (36, 56, 62, 95)},
        {'index': 7, 'name': 'Enoch', 'scores': (75, 42, 73, 81)} 
            ],
            'class 5' :[
        {'index': 0, 'name': 'Romeo', 'scores': (45, 57, 45, 96)}, 
        {'index': 1, 'name': 'Lois', 'scores': (65, 55, 58, 66)},
        {'index': 2, 'name': 'Ama', 'scores': (79, 56, 77, 96)},
        {'index': 3, 'name': 'Joseph', 'scores': (56, 36, 39, 96)},
        {'index': 4, 'name': 'Gifty', 'scores': (79, 89, 73, 76)},
        {'index': 5, 'name': 'Joshua', 'scores': (81, 76, 63, 74)},
        {'index': 6, 'name': 'Bernard', 'scores': (62, 71, 97, 76)},
        {'index': 7, 'name': 'Mary', 'scores': (47, 49, 77, 61)} 
            ],
            'class 6' :[
        {'index': 0, 'name': 'Ben', 'scores': (38, 46, 76, 81)}, 
        {'index': 1, 'name': 'Emma', 'scores': (72, 75, 68, 78)},
        {'index': 2, 'name': 'Patience', 'scores': (68, 45, 37, 78)},
        {'index': 3, 'name': 'Juliet', 'scores': (34, 75, 67, 21)},
        {'index': 4, 'name': 'Roland', 'scores': (69, 56, 98, 69)},
        {'index': 5, 'name': 'Matilda', 'scores': (45, 88, 51, 73)},
        {'index': 6, 'name': 'Peter', 'scores': (88, 76, 52, 85)},
        {'index': 7, 'name': 'William', 'scores': (46, 43, 73, 79)} 
            ]
    }

    """ displaying the operating to the user"""
    print("\n\t**** OPERATIONS *****")
    print('1. Information on specific student\n2. Class average score in a subject\n3. Best student in a subject')
    print('4. Worst student in a subject\n5. Best student in a class\n6. Students with same score in a class\n7. Overall best')
    choice = input('Enter the operation you want carried out: ')

    if choice == '1':
        level = get_class_input()
        index = get_stu_index()
        student_avg_score(info, level, index)
    elif choice == '2':
        level = get_class_input()
        sub_index = get_sub_index()
        class_sub_avg_score(info, level, sub_index)
    elif choice == '3':
        level = get_class_input()        
        sub_index = get_sub_index()        
        sub_best_student(info, level, sub_index)
    elif choice == '4':
        level = get_class_input()        
        sub_index = get_sub_index()
        sub_worst_student(info, level, sub_index)
    elif choice == '5':
        level = get_class_input()                
        class_best_student(info, level)
    elif choice == '6':
        level = get_class_input()        
        sub_index = get_sub_index()
        mark = get_mark()
        same_score_students(info, level, sub_index, mark)
    elif choice == '7':
        overall_best(info)
    else:
        print("invalid input")
    


    """
    # writing to csv file
    with open('results.csv', mode ='w') as csv_file:
        fieldnames = ['student_name', 'total_score', 'average']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

        writer.writeheader()
        writer.writerow({'student_name': student_name, 'total_score': total_score, 'average': average})
    """


if __name__ == '__main__':
    main()