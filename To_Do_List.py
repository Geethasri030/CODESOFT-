def To_Do_List():
    task_list = []
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Your Task List")
        print("2. Add A New TaskTo Task List")
        print("3. Delete Copleted Task")
        print("4. Close The List")
        option= input("Choose any one option from 1 to 4:")
        if option == '1':
            print("\n The Tasks In Your List:")
            for index, task in enumerate(task_list, start=1):
                print(f"{index}. {task}")
        elif option == '2':
            new_task = input("Enter the task: ")
            task_list.append(new_task)
            print("Task added!")
        elif option == '3':
            task_num = int(input("Enter task number to delete: "))
            if 0 < task_num <= len(task_list):
                removed = task_list.pop(task_num - 1)
                print(f"Removed From The List: {removed}")
            else:
                print("Invalid task number.Please enter a valid task number.")
        elif option == '4':
            break
To_Do_List()