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
            tasks = add_task(tasks, title)

        elif choice == "2":
            for task in tasks:
                print(task)


        elif choice == "3":
            status = input("Введите статус: ")
            if validate_status(status):
                result = get_tasks_by_status(tasks, status)
                for task in result:
                    print(task)
            else:
                print("Ошибка статуса!")

        elif choice == "4":
            order = input("По убыанию? (y\n): ")
            reverse = order == "y"
            tasks = sort_tasks(tasks, reverse)
            print("Отсортировано")

        elif choice == "5":
            save_tasks(tasks, FILENAME)
            print("Сохоанено")

        elif choice == "0":
            save = input("Сохранить перед выходом? (y\n): ")
            if save == "y":
                save_tasks(tasks, FILENAME)
            break

        else:
            print("Ошибка ввода")

if __name__ == "__main__":
    run_cli()