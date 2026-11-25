# Welcome to the Grade Analyzer

# Scores already known and stored in a list

scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

counts = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0,
}  # To help count how many scores fall into each grade category later on

print("=" * 40)
print("The Grade Analyzer")
print("=" * 40)

print(f"The scores are: {scores}")

print("-" * 85)

# Categorize each score, count grades, and count pass/fail in a single loop

passed_count = 0
failed_count = 0

for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else: 
        grade = "F"
        
    counts[grade] += 1
    
    if grade == "F":
        failed_count += 1
    else: 
        passed_count += 1

    if grade == "A" or grade == "F":
        print(f"{score} is an {grade}")
    else:
        print(f"{score} is a {grade}")
        
print()

print("Grade Distribution:")
for letter, count in counts.items():
    print(f"{letter}: {count} students")

print("-" * 85)

# Statistics of Scores
total_number = len(scores)
print(f"{total_number} scores in total!")

average_score = sum(scores) / len(scores)
print(f"{average_score:.1f} is the mean!")

passing_percent = passed_count / total_number * 100
failing_percent = failed_count / total_number * 100

print(f"Passing: {passed_count} ({passing_percent:.1f}%)")
print(f"Failing: {failed_count} ({failing_percent:.1f}%)")

print("-" * 85)

# Min and Max Scores
lowest_score = min(scores)
highest_score = max(scores)

print(f"Lowest score: {lowest_score}")
print(f"Highest score: {highest_score}")

print("-" * 85)

# Add new scores with a while loop
while True:
    append_scores = input("Enter new scores separated by commas (or type 'done' to finish): ")

    if append_scores.strip().lower() == "done":
        break

    try:
        new_scores = [int(score.strip()) for score in append_scores.split(",")]
        scores.extend(new_scores)
        print(f"Added {len(new_scores)} scores. Current list: {scores}")
        print(f"Updated average: {sum(scores) / len(scores):.1f}")
    except ValueError:
        print("Invalid input! Please enter scores separated by commas only.")

print("-" * 85)

# Final average after all scores are added
final_average = sum(scores) / len(scores)
print(f"Final average: {final_average:.1f}")
print("=" * 40)
