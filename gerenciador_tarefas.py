# Gerenciador de Tarefas Funcional

def task_manager():
    """Closure para gerenciar tarefas em memória."""
    tasks = []

    def add_task(description, priority):
        tasks.append({"description": description, "priority": priority, "status": "pendente"})

    def list_tasks():
        return [f"{t['description']} - Prioridade: {t['priority']} - Status: {t['status']}" for t in tasks]

    def filter_tasks(status):
        return list(filter(lambda t: t["status"] == status, tasks))

    def complete_task(description):
        for task in tasks:
            if task["description"] == description:
                task["status"] = "concluída"
                break

    def remove_task(description):
        nonlocal tasks
        tasks = [task for task in tasks if task["description"] != description]

    def sort_tasks():
        return sorted(tasks, key=lambda t: t["priority"], reverse=True)

    return add_task, list_tasks, filter_tasks, complete_task, remove_task, sort_tasks


# Criando instância do gerenciador de tarefas
add_task, list_tasks, filter_tasks, complete_task, remove_task, sort_tasks = task_manager()


# Exemplo de uso
def main():
    add_task("Estudar Python", 2)
    add_task("Fazer trabalho da faculdade", 1)
    add_task("Ler um livro", 3)

    print("\nTarefas cadastradas:")
    print("\n".join(list_tasks()))

    complete_task("Estudar Python")

    print("\nTarefas pendentes:")
    print("\n".join(f"{t['description']} - {t['status']}" for t in filter_tasks("pendente")))

    print("\nTarefas ordenadas por prioridade:")
    print("\n".join(f"{t['description']} - {t['priority']}" for t in sort_tasks()))

    remove_task("Ler um livro")
    print("\nApós remover uma tarefa:")
    print("\n".join(list_tasks()))


if __name__ == "__main__":
    main()
