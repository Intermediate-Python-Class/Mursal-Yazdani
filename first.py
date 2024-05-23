#step1
temperatures = [30, 32, 28, 26, 29, 31, 33]
#step2
totalSum = sum(temperatures)
#step3
average_temp = totalSum / len(temperatures)
#step4
days_average = 0
#step5
for temp in temperatures:
#step6
    if temp > average_temp:
#step7
        days_average += 1
#step8
print("Average temperature of a week:", average_temp)
print("Number of days:", days_average)



#Finding the missing number
my_array = [1, 2, 3, 4, 6, 5, 8, 9, 10]

def find_missing_values(nums): 
    n = len(nums) + 1
    total = n * (n+1) // 2

    actual = sum(nums)
    return total - actual

missing_num = find_missing_values(my_array)

print("The missing number is: ", missing_num)


# You are a teacher at a high school, and you have recently conducted an exam for a class of students. 
# Each student's exam grade is represented by a tuple (student_name, score),
# where student_name is a string representing the student's name,
# and score is an integer representing the exam score (out of 100). 
# Your task is to sort the students' exam grades based on their scores in ascending order. 
# If two or more students have the same score, they should be sorted alphabetically by their names.
# Write a Python function to solve this problem.
#solution
def sortGrades(grades):
    sorted_grades = sorted(grades, key=lambda x: (x[1], x[0]))
    return sorted_grades

grades = [
    ("Mursal", 85),
    ("Mozhdah", 90),
    ("kawsar", 75),
    ("Ayat", 90),
    ("Sahra", 75),
    ("Asma", 85)
]

sorted_grades = sortGrades(grades)
print(sorted_grades)



#Queue operations
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
       

    def peek(self):
        if not self.isEmpty():
            return self.items[0]


    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.items)
print(q.size())
print(q.isEmpty())
print(q.peek())
print(q.dequeue())
print(q.items)

