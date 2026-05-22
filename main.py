from datetime import datetime
json.load()
tasks = []
def add_task():
    print("\n=== Add Study Task ===")
    name = input("Task Name: ")
    due_date = input("Due Date (DD/MM/YYYY): ")
    priority = input("Priority (High / Medium / Low): ")
    task = {
        "name": name,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!\n")
def view_tasks():
    print("\n=== Study Tasks ===")
    if len(tasks) == 0:
        print("No tasks available.\n")
        return
    sort_tasks()
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(f"""
Task {i + 1}
-------------------------
Name: {task["name"]}
Due Date: {task["due_date"]}
Priority: {task["priority"]}
Status: {status}
""")
def sort_tasks():
    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }
    tasks.sort(
        key=lambda task: (
            datetime.strptime(
                task["due_date"],
                "%d/%m/%Y"
            ),
            priority_order.get(
                task["priority"],
                4
            )
        )
    )
def generate_study_plan():
    print("\n=== Today's Study Plan ===")
    pending_tasks = []
    for task in tasks:
        if task["completed"] == False:
            pending_tasks.append(task)
    if len(pending_tasks) == 0:
        print("No pending tasks.\n")
        return
    sort_tasks()
    for task in pending_tasks[:3]:
        print(f"""
Study Task:
- {task["name"]}
Priority: {task["priority"]}
Deadline: {task["due_date"]}
""")
def complete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        choice = int(
            input("Enter task number to mark complete: ")
        )
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            print("Task completed!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")
def show_statistics():
    print("\n=== Study Statistics ===")
    total_tasks = len(tasks)
    completed_tasks = 0
    for task in tasks:
        if task["completed"]:
            completed_tasks += 1
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    if total_tasks > 0:
        completion_rate = (
            completed_tasks / total_tasks
        ) * 100
        print(
            f"Completion Rate: {completion_rate:.1f}%"
        )
    show_stress_level()
    print()
def show_stress_level():
    today = datetime.today()
    urgent_tasks = 0
    for task in tasks:
        if task["completed"] == False:
            due_date = datetime.strptime(
                task["due_date"],
                "%d/%m/%Y"
            )
            days_left = (
                due_date - today
            ).days
            if days_left <= 3:
                urgent_tasks += 1
    if urgent_tasks >= 3:
        print("Stress Level: HIGH")
    elif urgent_tasks >= 1:
        print("Stress Level: MEDIUM")
    else:
        print("Stress Level: LOW")
def main():
    while True:
        print("""

1. Add Study Task
2. View Tasks
3. Generate Study Plan
4. Complete Task
5. Study Statistics
6. Exit
""")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            generate_study_plan()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            print("Thank you for using StudySprint!")
            break
        else:
            print("Invalid option.\n")
def test_add_task():

    test_task = {
        "name": "Test Task",
        "due_date": "24/05/2026",
        "priority": "High",
        "completed": False
    }
    tasks.append(test_task)

    assert len(tasks) > 0

    assert tasks[-1]["name"] == "Test Task"

    print("test_add_task passed!")
def test_sort_tasks():

    sort_tasks()

    for i in range(len(tasks) - 1):

        current_date = datetime.strptime(
            tasks[i]["due_date"],
            "%d/%m/%Y"
        )

        next_date = datetime.strptime(
            tasks[i + 1]["due_date"],
            "%d/%m/%Y"
        )

        assert current_date <= next_date

    print("test_sort_tasks passed!")
test_add_task()
test_sort_tasks()
main()

