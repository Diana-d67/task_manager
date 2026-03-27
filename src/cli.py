from src.services import add_task, get_tasks_by_status, sort_tasks
from src.storage import save_tasks, load_tasks
from src.utils import validate_status

FILENAME = "data.json"


def run_cli():
    tasks = load_tasks(FILENAME)

    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Фильр по статусу")
        print("4. Сортировка")
        print("5. Сохранить")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите задачу: ")
            tasks = add_task(title, tasks)

        elif choice == "2":
            for task in tasks:
                print(task)