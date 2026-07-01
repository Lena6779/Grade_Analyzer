# Welcome to the Grade Analyzer

# Scores already known and stored in a list

scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71, 79, 89]

counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0} # To help count how many scores fall into each grade category later on

print("=" * 40)
print("The Grade Analyzer")
print("=" * 40)

print(f"The scores are: {scores}")

print("-" * 85)

# To display which score falls into which grade category (A, B, C, D, F)
for score in scores:
    if score >= 90 and score <= 100:
        print(f"{score} is an A")
    elif score >= 80 and score <= 89:
        print(f"{score} is a B")
    elif score >= 70 and score <= 79:
          print(f"{score} is a C")
    elif score >= 60 and score <= 69:
         print(f"{score} is a D")
    elif score <= 59:
         print(f"{score} is a F")

print("-" * 85)
    
# To display how many scores fall into a grade category
for score in scores:
    if score <= 59:
        counts["F"] += 1
    elif score <= 69:
        counts["D"] += 1
    elif score <= 79:
        counts["C"] += 1
    elif score <= 89:
        counts["B"] += 1
    else:
        counts["A"] += 1

print(counts)

print("-" * 85)

# Statistics of Scores

total_number = len(scores)
print(str(total_number) + " scores in total!")

average_score = sum(scores)/ len(scores)
print(f"{average_score:.1f} is the mean!")

print("-" * 85)

# How many students passed and how many failed
passed_count = 0
for score in scores:
    if score >= 60:
        passed_count += 1

print(str(passed_count) + " has passed!")

failed_count = 0
for score in scores:
    if score <= 59:
        failed_count += 1

print(str(failed_count) + " have failed!")

print("-" * 85)

# Min and Max Scores
lowest_score = min(scores)
print(str(lowest_score) + " is the lowest score!")

highest_score = max(scores)
print(str(highest_score) + " is the highest score!")

print("-" * 85)

# Add new scores to the list
while True:
    append_scores = input("Enter new scores separated by commas or type 'done' to finish adding): ")
    
    if append_scores.strip().lower() == "done":
        break
    
    try:
        new_scores = [int(score.strip()) for score in append_scores.split(",")]
        scores.extend(new_scores)
        print(f"Added {len(new_scores)} scores. Current list: {scores}")
        print(f"New average score: {sum(scores)/len(scores):.1f}")
        print(f"New highest score: {max(scores)}")
        print(f"New lowest score: {min(scores)}")
    except ValueError:
        print("Invalid input! Please enter grade scores separated by commas only.")

print("-" * 85)

