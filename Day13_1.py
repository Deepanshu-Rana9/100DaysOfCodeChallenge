# Student Grade Analysis
def student_grade_analysis(scores):
    avg_scores = {name: sum(marks) / len(marks) for name, marks in scores.items()}
    passed_students = [name for name, avg in avg_scores.items() if avg >= 70]
    top_scorer = max(avg_scores, key=avg_scores.get)
    return avg_scores, passed_students, top_scorer

scores = {
    "Ichigo": [85, 78, 92],
    "Rukia": [59, 63, 70],
    "Renji": [90, 88, 85],
    "Byakuya": [40, 50, 45],
    "Yhwach": [72, 80, 78]
}

avg_scores, passed_students, top_scorer = student_grade_analysis(scores)
print("Average Scores:", avg_scores)
print("Passed Students:", passed_students)
print("Top Scorer:", top_scorer)
