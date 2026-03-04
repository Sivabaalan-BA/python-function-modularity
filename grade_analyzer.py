# Name: [Sivabaalan BA]
# Roll Number: [IITP_AIMLTN_2602254]
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Process the Scores =====")
def process_scores(students):
    averages = {}

    for name in students:
        scores = students[name]
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg

    return averages


students = {
    "Raj": [80, 70, 90],
    "Anu": [95, 92, 88]
}

result = process_scores(students)

print(result)
print("\n===== Task 2: Classify the Grades =====")
def classify_grades(averages):
    grades = {}

    for name in averages:
        avg = averages[name]

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "F"

        grades[name] = (avg, grade)

    return grades


averages = {
    "Raj": 80.0,
    "Anu": 91.67
}

result = classify_grades(averages)

print(result)
print("\n===== Task 3: Generate the Report =====")
def generate_report(classified, passing_avg=70):

    total_students = len(classified)
    passed = 0

    print("===== Student Grade Report =====")
def generate_report(classified, passing_avg=70):

    total_students = len(classified)
    passed = 0

    print("===== Student Grade Report =====")

    for name in classified:
        avg, grade = classified[name]

        if avg >= passing_avg:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"

        print(name, "| Avg:", avg, "| Grade:", grade, "| Status:", status)

    failed = total_students - passed

    print("===============================")
    print("Total Students :", total_students)
    print("Passed :", passed)
    print("Failed :", failed)


classified = {
    "Alice": (86.25, "B"),
    "Bob": (62.50, "C"),
    "Clara": (96.25, "A")
}

generate_report(classified)