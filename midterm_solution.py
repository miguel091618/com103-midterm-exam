project_title = input("Project : ")
group_name = input("Group : ")

task_names = [
    "Program Logic / Coding",
    "UI / Output Formatting",
    "Testing / Debugging",
    "Documentation / README",
    "Presentation Slides"
]

task_hours = [6, 3, 2, 2, 2]
print("\n=====================================")
print("    COM 103 PROJECT -- TASK TYPES")
print("=====================================")

for i in range(5):
    print(f"{i+1}. {task_names[i]}: [{task_hours[i]}h]")

print("=====================================")

assigned_tasks = []
total_points = 0
tasks_assigned = 0

for i in range(4):
    print(f"\n--- TASK {i+1} ---")
    task_num = int(input("task number (0 to skip): "))
    if task_num == 0:
        continue
    if 1 <= task_num <= 5:
        member_name = input("Enter member name: ")
        while True:
            status = input("Status (done/pending): ").lower()
            if status in ["done", "pending"]:
                break
            print("Invalid status. Please enter 'done' or 'pending'.")
        points = 2 if status == "done" else 1
        total_points += points
        tasks_assigned += 1
        assigned_tasks.append({
            "task_name": task_names[task_num-1],
            "task_hours": task_hours[task_num-1],
            "member": member_name,
            "status": status,
            "points": points
        })
