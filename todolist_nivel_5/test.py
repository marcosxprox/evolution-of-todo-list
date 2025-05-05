import unittest
from tarefa import Tarefa
from lista_tarefas import ListaTarefas
from unittest.mock import patch
import os

class TarefaTest(unittest.TestCase):

    def test_criacao_tarefa(self):
        tarefa = Tarefa('Correr', 'correr 10 voltas', 'alta')
        self.assertEqual(tarefa.titulo, 'Correr')
        self.assertEqual(tarefa.descricao, 'correr 10 voltas')
        self.assertEqual(tarefa.prioridade, 'alta')
        self.assertEqual(tarefa.status, 'pendente')

    def test_converter_dict(self):
        tarefa = Tarefa('Correr', 'correr 10 voltas', 'alta')
        tarefa_dict = tarefa.converter_dict()
        esperado = {
            "titulo":'Correr',
            "descricao":'correr 10 voltas',
            "prioridade":'alta',
            "status":'pendente'
        }
        self.assertEqual(tarefa_dict, esperado)

    def setUp(self):
        self.lista = ListaTarefas()
        self.tarefa = Tarefa('Correr', 'correr 10 voltas', 'alta')
        self.lista.adicionar_tarefa(self.tarefa)

    def test_concluir_tarefa(self):
        tarefa = Tarefa('Correr', 'correr 10 voltas', 'alta')
        tarefa.concluir()
        self.assertEqual(tarefa.status, 'concluído')

    def test_adicionar_tarefa(self):
        tarefa = Tarefa('Correr', 'correr 10 voltas', 'alta')
        lista = ListaTarefas()
        lista.adicionar_tarefa(tarefa)
        self.assertIn(tarefa, lista.tarefas)

    @patch('builtins.input', return_value = 's')
    def test_remover_tarefa(self, mock_input):
        self.lista.remover_tarefa(0)
        self.assertNotIn(self.tarefa, self.lista.tarefas)

    def test_concluir_tarefa_status(self):
        tarefa = Tarefa('Correr', 'correr 10 voltas', 'alta')
        tarefa.concluir()
        self.assertEqual(tarefa.status, 'concluído')

    def test_salvar_tarefa(self):
        tarefa = Tarefa('Correr', 'correr 10 voltas', 'alta')
        lista = ListaTarefas()
        lista.adicionar_tarefa(tarefa)
        nome_arquivo = "lista.json"
        lista.salvar_em_arquivo(nome_arquivo)
        self.assertTrue(os.path.exists(nome_arquivo))

    def test_carregar_tarefa(self):
        nome_arquivo = "lista.json"
        self.lista.tarefas = []
        self.lista.adicionar_tarefa(self.tarefa)
        self.lista.salvar_em_arquivo(nome_arquivo)

        lista_carregada = ListaTarefas()
        lista_carregada.carregar_tarefas(nome_arquivo)
        self.assertEqual(len(lista_carregada.tarefas),1)
        self.assertEqual(lista_carregada.tarefas[0].titulo, self.tarefa.titulo)
        self.assertEqual(lista_carregada.tarefas[0].descricao, self.tarefa.descricao)
        self.assertEqual(lista_carregada.tarefas[0].prioridade, self.tarefa.prioridade)
        self.assertEqual(lista_carregada.tarefas[0].status, self.tarefa.status)

        os.remove(nome_arquivo)


if __name__ == "__main__":
    unittest.main()
