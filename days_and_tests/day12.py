def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    with open('todos.txt', 'w') as file:
        file.writelines(todos_arg)

while True:
    user_action  = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]           # samo se upise 'add' sve nakon toga je string za unos

        todos = get_todos(filepath="todos.txt")

        todos.append(todo + '\n')

        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos(filepath="todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"

            print(row)

    elif user_action.startswith("complete"):
        try:
            todos = get_todos(filepath="todos.txt")
            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos("todos.txt", todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is not item with that number.")
            continue

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos(filepath="todos.txt")
            print('Here are existing todos: ', todos)

            new_todo = input("Enter a new ToDo: ")
            todos[number] = new_todo +'\n'

            write_todos("todos.txt", todos)

            print('Heres after the edit: ', todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command doesn't exist!")
    #if whatever in user_action:
    #    print("You have entered an unknown command!")
print("Bye!")
