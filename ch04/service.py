from ch04.data import todo as data
from ch04.model import Todo

if __name__ == '__main__':
    print(data.find_all())
    data.insert_one(Todo(task = "study fastapi"))
    print(data.find_all())