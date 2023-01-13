#from functions import get_todos, write_todos
#OR
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("\033[91mIt is",now,"\033[0m")

while True:
    # Get user input and trip space characters in it
    user_action = input("Type add, show, edit, complete or exit: ")
    # REMOVING ANY WHITE SPACE
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()

        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        # USE ENUMERATE FUNCTION TO PRINT THE INDEX OF THE LIST
        todos = functions.get_todos()
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}- {item}"
            item = item.title()
            print('\033[92m', row)
        print('\033[0m')
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print('\033[91mYour command is not valid')
            print('\033[0m')
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"To do {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print('\033[91mThere is no item with that number')
            print('\033[0m')
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print('\033[91m Hey you enter an unknown command')
    print('\033[0m')

print("Bye")
