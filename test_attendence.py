def eligibility(classes_held, classes_attended):
    attendance = (classes_attended / classes_held) * 100
    return attendance

assert eligibility(100, 75) == 75.0

assert eligibility(80, 70) == 87.5


assert eligibility(50, 50) == 100.0

assert eligibility(40, 0) == 0.0

print("All test cases passed ✅")
