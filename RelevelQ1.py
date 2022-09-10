# your code goes here
no_of_classes = int(input('Enter number of classes'))
students_in_class = []
for i in range(no_of_classes):
	students_in_class.append(int(input('Enter students in Class')))

no_of_queries = int(input('Enter no of Queries'))
queries = []
for i in range(no_of_queries):
	queries.append(int(input('Enter Query')))

for i in range(no_of_queries):
    print(i)
    # sum_of_students = 0
    # for j in range(students_in_class):
    #     sum_of_students += j
    #     if i <= sum_of_students:
    #         print(j)
