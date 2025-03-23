import unittest
from gerenciador_tarefas import task_manager


class TestGerenciadorTarefas(unittest.TestCase):
    def setUp(self):
        """Configuração inicial antes de cada teste."""
        self.add_task, self.list_tasks, self.filter_tasks, self.complete_task, self.remove_task, self.sort_tasks = task_manager()

    def test_add_task(self):
        self.add_task("Testar função add_task", 1)
        self.assertEqual(len(self.list_tasks()), 1)

    def test_complete_task(self):
        self.add_task("Finalizar relatório", 2)
        self.complete_task("Finalizar relatório")
        completed_tasks = [t for t in self.filter_tasks("concluída")]
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(completed_tasks[0]["description"], "Finalizar relatório")

    def test_remove_task(self):
        self.add_task("Apagar depois", 3)
        self.remove_task("Apagar depois")
        self.assertEqual(len(self.list_tasks()), 0)

    def test_sort_tasks(self):
        self.add_task("Tarefa Média", 2)
        self.add_task("Tarefa Alta", 3)
        self.add_task("Tarefa Baixa", 1)
        sorted_tasks = self.sort_tasks()
        self.assertEqual(sorted_tasks[0]["description"], "Tarefa Alta")
        self.assertEqual(sorted_tasks[1]["description"], "Tarefa Média")
        self.assertEqual(sorted_tasks[2]["description"], "Tarefa Baixa")


if __name__ == "__main__":
    unittest.main()