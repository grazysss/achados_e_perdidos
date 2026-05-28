# 🎒 Sistema de Achados e Perdidos - Grêmio Estudantil

Este projeto consiste em uma API REST de um sistema de **Achados e Perdidos** customizado para o gerenciamento de objetos esquecidos no campus, operado diretamente pelos membros do Grêmio Estudantil.

O projeto foi desenvolvido como parte da atividade prática da disciplina de **Programação com Acesso a Banco de Dados** do Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte (IFRN).

---

## 🛠️ Especificações Técnicas & Stack

A aplicação segue estritamente as restrições arquiteturais impostas, utilizando consultas SQL puras e nativas (Raw SQL), sem o auxílio de frameworks ORM.

* **Linguagem:** Python
* **Framework Web:** FastAPI
* **Driver do Banco de Dados:** asyncpg (Operações 100% assíncronas)
* **Validação de Dados:** Pydantic
* **Banco de Dados Relacional:** PostgreSQL

---

## 🗄️ Estrutura do Banco de Dados

O modelo de dados é composto por 4 tabelas interconectadas por chaves estrangeiras (FK), garantindo a integridade referencial:

* **`gremistas`**: Cadastro dos membros autorizados a gerenciar os itens.
* **`categorias`**: Classificação dos tipos de objetos (ex: Eletrônicos, Documentos, Vestuário).
* **`locais`**: Mapeamento de salas, laboratórios e blocos do campus.
* **`itens`**: Tabela central que registra as características do objeto, o local, e os gremistas responsáveis pelo recebimento e pela devolução.

---

## 🚀 Funcionalidades e Endpoints (CRUD)

A API disponibiliza operações completas testadas e documentadas nativamente via **Swagger UI** (disponível em `/docs` ao rodar a aplicação).

| Método | Endpoint | Descrição Prática no Sistema |
| :--- | :--- | :--- |
| **POST** | `/items` | **Registrar Achado:** Cadastra um item perdido associando uma categoria, local e o gremista que o recolheu. |
| **GET** | `/items` | **Painel do Grêmio:** Lista todos os itens cadastrados integrando os nomes correspondentes através de SQL Joins. |
| **GET** | `/items/{id}` | **Busca Detalhada:** Localiza um objeto específico por ID para verificar detalhes e histórico de triagem. |
| **PUT** | `/items/{id}` | **Efetuar Devolução:** Atualiza o status do item para 'devolvido', registrando o aluno que o recuperou e o gremista que realizou a entrega. |
| **DELETE** | `/items/{id}` | **Remover Registro:** Exclui permanentemente o item do banco de dados (ex: em casos de erro de digitação). |

---