Este projeto tem como objetivo construir uma aplicação de lista de tarefas (To-Do List) com níveis de dificuldade progressiva, desde a implementação básica em Python até a criação de uma API com FastAPI e banco de dados. A aplicação evolui em complexidade, com cada nível abordando um novo conceito e desafio. O objetivo é criar um projeto completo e funcional, com as melhores práticas de desenvolvimento.

Estrutura do Projeto
O projeto está dividido em 8 níveis, cada um com requisitos definidos de entrada e saída. O progresso para o próximo nível só será possível quando o nível atual estiver satisfatório.

Níveis:
🟢 Nível 1 — Python Básico:
Implementação básica com lógica, input/output, if, while. A aplicação deve ser capaz de adicionar e listar tarefas simples no terminal, utilizando apenas memória.

🟡 Nível 2 — Estruturas de Dados:
Uso de listas e dicionários para gerenciar tarefas. Cada tarefa terá título, descrição e prioridade. As tarefas devem ser armazenadas em memória.

🟠 Nível 3 — Orientação a Objetos:
Criação das classes Tarefa e ListaDeTarefas, com métodos como adicionar, remover, e concluir. A estrutura de dados será aprimorada utilizando conceitos de orientação a objetos.

🟣 Nível 4 — Persistência de Dados:
As tarefas serão salvas e carregadas de arquivos .json utilizando as funções json.dump() e json.load(). A aplicação manterá dados persistentes entre reinicializações.

🟤 Nível 5 — Testes Automatizados:
Implementação de testes para os métodos da aplicação utilizando a biblioteca unittest para validar a funcionalidade do código. (Nota: Não será abordado pytest)

🔵 Nível 6 — API com FastAPI:
A aplicação será transformada em uma API RESTful utilizando FastAPI. Serão criadas rotas para operações como GET, POST, PUT, e DELETE para gerenciar as tarefas.

🔘 Nível 7 — Banco de Dados:
A persistência de dados será movida para um banco de dados relacional como SQLite ou PostgreSQL, utilizando a biblioteca SQLAlchemy ou databases para interagir com o banco.

🔴 Nível 8 — Deploy:
A aplicação será implantada em um serviço de cloud como Render ou Railway. A configuração do ambiente será feita com um arquivo, requirements.txt e Procfile para permitir o deploy e escalabilidade.
