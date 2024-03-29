FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of
    to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    """Write the to-do items list in the text file."""
    with open('../todos.txt', 'w') as file:
        file.writelines(todos_arg)

def konverter(feets, inches):
    sumfeet = feets * 0.3048
    suminch = inches * 0.0254
    return sumfeet + suminch

if __name__ == "__main__":
    print("Hello from functions")