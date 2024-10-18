# Task list initialized as an empty list
task_list = []

# Function to add a new task to the list
def add_task(priority, due_date):
    task = (priority, due_date)
    task_list.append(task)  # Add the task to the task list

# Function to display all tasks
def display_tasks():
    if not task_list:
        print("No tasks available.")
    else:
        print("Tasks:")
        for task in task_list:
            print(f"Priority: {task[0]}, Due Date: {task[1]}")

# Function to implement Bubble Sort to sort tasks by priority
def bubble_sort_tasks():
    n = len(task_list)
    for i in range(n):
        for j in range(0, n-i-1):
            # Sort by highest priority first
            if task_list[j][0] < task_list[j+1][0]:
                task_list[j], task_list[j+1] = task_list[j+1], task_list[j]

# Function to find the task with the highest priority
def find_highest_priority_task():
    if not task_list:
        print("No tasks available.")
        return None
    # Find the task with the highest priority
    highest_priority_task = task_list[0]
    for task in task_list:
        if task[0] > highest_priority_task[0]:
            highest_priority_task = task
    print(f"Highest priority task: Priority {highest_priority_task[0]}, Due Date {highest_priority_task[1]}")
    return highest_priority_task

# Function to remove a task by its priority
def remove_task_by_priority(priority):
    for task in task_list:
        if task[0] == priority:
            task_list.remove(task)
            print(f"Task with priority {priority} removed.")
            return
    print(f"No task found with priority {priority}.")

# Adding tasks to the list
add_task(5, "2024-09-22")
add_task(3, "2024-10-21")
add_task(1, "2024-11-20")

# Display tasks
display_tasks()

# Sort the tasks by priority
bubble_sort_tasks()

# Display tasks after sorting
print("\nAfter Sorting:")
display_tasks()

# Find the highest priority task
print("\nFinding highest priority task:")
find_highest_priority_task()

# Remove task with priority 
print("\nRemoving task with priority :")
remove_task_by_priority(3)

# Display tasks after removing a task
print("\nAfter Removing Task:")
display_tasks()
