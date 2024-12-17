task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
is_time_bound = input("Is it time-bound? (yes/no): ")

match priority:
  case "high":
    if is_time_bound == "yes":
     print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    else:
      print(f"Reminder: {task} is a high priority task that requires immediate attention soon")
  case "medium":
    if is_time_bound == "yes":
     print(f"Reminder: {task} is a medium priority task that requires attention soon!")
    else:
      print(f"Reminder: {task} is a medium priority task that requires attention") 
  case "low":
     if is_time_bound == "yes":
      print(f"{task} is a low priority task. Consider completing it soon")
     else:
      print(f"{task} is a low priority task. Consider completing it when you have free time.")