import numpy as np

student_scores = np.array([
    [85, 78, 90, 88],
    [92, 81, 85, 90],
    [76, 88, 84, 79],
    [89, 91, 87, 93]
])

# Calculate average score for each subject
average_scores = np.mean(student_scores, axis=0)

subjects = ["Math", "Science", "English", "History"]

# Find subject with highest average
highest_index = np.argmax(average_scores)

print("Average Scores of Each Subject")
for i in range(len(subjects)):
    print(subjects[i], ":", average_scores[i])

print("\nSubject with Highest Average:", subjects[highest_index])
print("Highest Average Score:", average_scores[highest_index])
