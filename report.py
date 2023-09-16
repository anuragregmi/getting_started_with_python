# Write a program that accepts students marks for individuals
# and displays them collectively 

def take_input():
    print()
    roll_number = input("roll number: ")

    math_input = input("math: ")
    math = int(math_input)

    english_input = input("english: ")
    english = int(english_input)

    computer_input = input("computer: ")
    computer = int(computer_input)

    total = math + english + computer
    percentage = (total / 300) * 100

    output = f"{roll_number}\t{math}\t{english}\t{computer}\t{percentage}%"

    return output


def print_result(results):
    print()
    print("RN\tmath\tenglish\tcomputer\tpercentage")
    for result in results:
        print(result)

total_students = 3
results = []

for i in range(total_students):
    result = take_input()
    results.append(result)

print_result(results)