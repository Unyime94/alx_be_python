# Prompt the user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Default message for the reminder
message = ""

# Match Case to handle priority levels
match priority:
    case "high":
        message = f"'{task}' is a high priority task."
    case "medium":
        message = f"'{task}' is a medium priority task."
    case "low":
        message = f"'{task}' is a low priority task."
    case _:
        message = f"'{task}' has an unknown priority level."

# Modify the message if the task is time-sensitive
if time_bound == "yes":
    message += " It requires immediate attention today!"
elif time_bound == "no":
    message += " Consider completing it when you have free time."

# Provide a customized reminder
print("\nReminder:", message)
