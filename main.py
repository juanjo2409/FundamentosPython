from functions import *

def show_menu():
    print("\n--- TASK MANAGEMENT SYSTEM ---")
    print("1. Register task")
    print("2. View all tasks")
    print("3. Search task")
    print("4. Update task")
    print("5. Delete task")
    print("6. Exit")

def run():
    while True:
        show_menu()
        option = input("Select an option: ")
        
        try:
            if option == "1":
                title = input("Title: ")
                desc = input("Description: ")
                priority = input("Priority (high/medium/low): ")
                message = register_task(title, desc, priority)
                print(message)

            elif option == "2":
                task_list = get_all_tasks()
                if not task_list:
                    print("No tasks found.")
                for t in task_list:
                    print(f"[{t['id']}] [{t['title']}] [{t['priority']}] [{t['status']}]")

            elif option == "3":
                criteria = input("Search by (id/title): ")
                value = input("Value to search: ")
                found = search_by_criteria(criteria, value)
                if not found:
                    print("No matches found.")
                for t in found: 
                    print(t)

            elif option == "4":
                id_to_modify = int(input("Task ID to modify: "))
                new_title = input("New title (leave empty to keep current): ")
                new_status = input("New status (pending/completed): ")
                if update_task(id_to_modify, new_title if new_title else None, new_status if new_status else None):
                    print("Task updated successfully.")
                else:
                    print("ID not found. Please enter a valid ID.")

            elif option == "5":
                id_to_delete = int(input("Task ID to delete: "))
                if delete_task(id_to_delete):
                    print("Task deleted successfully.")
                else:
                    print("Task not found.")

            elif option == "6":
                print("Exiting...")
                break
            else:
                print("Invalid option.")

        except ValueError:
            print("Invalid input. Please enter a numeric value where required.")

if __name__ == "__main__":
    run()