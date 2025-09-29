import json
import os

FILE_NAME = "tasks.json"

# Garantir que o arquivo existe
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

def load_tasks():
    """Carrega as tarefas do arquivo JSON."""
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    """Salva as tarefas no arquivo JSON."""
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"Tarefa adicionada: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return
    print("\nSuas tarefas:")
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. {task['description']} - {status}")

def complete_task(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"Tarefa {index} concluída!")
    except IndexError:
        print("Tarefa não encontrada.")

def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Tarefa removida: {removed['description']}")
    except IndexError:
        print("Tarefa não encontrada.")

def menu():
    while True:
        print("\n--- GERENCIADOR DE TAREFAS ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            desc = input("Descrição da tarefa: ")
            add_task(desc)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            index = int(input("Número da tarefa: "))
            complete_task(index)
        elif choice == "4":
            index = int(input("Número da tarefa: "))
            delete_task(index)
        elif choice == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
