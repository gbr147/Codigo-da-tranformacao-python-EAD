# 📔 Estruturas de Dados e Agenda de Contatos em Python

Este repositório reúne scripts em **Python 3** desenvolvidos para praticar a manipulação de variáveis, a atribuição de tipos primitivos e o uso avançado de estruturas de dados dinâmicas, culminando no desenvolvimento de um CRUD completo em terminal utilizando dicionários.

---

## 📌 Índice
* [1. Conceitos de Variáveis e Tipos Primários](#1-conceitos-de-variáveis-e-tipos-primários)
* [2. Projeto Central: Agenda de Contatos](#2-projeto-central-agenda-de-contatos)
* [✨ Funcionalidades do Sistema](#-funcionalidades-do-sistema)
* [🛠️ Estruturas de Programação Utilizadas](#️-estruturas-de-programação-utilizadas)
* [🚀 Como Executar o Projeto](#-como-executar-o-projeto)

---

## 1. Conceitos de Variáveis e Tipos Primários

O primeiro bloco do repositório aborda como o Python estrutura os dados internamente na memória. Foram mapeados os quatro tipos primitivos fundamentais:
* **`int` (Inteiro):** Utilizado para contagens e idades (Ex: `idade = 25`).
* **`float` (Ponto Flutuante):** Utilizado para números decimais precisos (Ex: `altura = 1.75`).
* **`str` (String/Texto):** Cadeia de caracteres para nomes e textos (Ex: `nome = "João"`).
* **`bool` (Booleano):** Estados lógicos condicionais Verdadeiro/Falso (Ex: `estudante = True`).

> 💡 **Nota de Desenvolvimento:** O foco deste trecho é demonstrar que a exibição direta dessas variáveis nem sempre é necessária para o usuário final, priorizando a sua **manipulação em lógica de background** para alimentar sistemas maiores.

---

## 2. Projeto Central: Agenda de Contatos

O desafio prático principal consiste em um **Sistema de Agenda de Contatos** interativo via CLI (Command Line Interface). O programa simula uma base de dados local na memória utilizando **dicionários aninhados** (`dict`), onde a chave primária é o nome do contato.

### ✨ Funcionalidades do Sistema

* **1. Adicionar Contato:** Cadastra o nome do contato, telefone e e-mail. Possui validação interna para impedir a duplicação de nomes existentes na base.
* **2. Remover Contato:** Exclui o registro da memória a partir do nome informado, emitindo um alerta caso o contato não exista.
* **3. Buscar Contato:** Consulta a base pelo nome e exibe um painel formatado com o telefone e e-mail atrelados àquela chave.
* **4. Ver Todos os Contatos:** Percorre todo o dicionário e renderiza uma lista com todos os usuários salvos. Retorna uma mensagem amigável caso a agenda esteja vazia.
* **5. Sair:** Encerra o loop de repetição e finaliza a aplicação com segurança.

---

## 🛠️ Estruturas de Programação Utilizadas

* **Dicionários (`{}`):** Utilizados como banco de dados temporário. Armazenam os contatos no formato `{Nome: {"telefone": X, "email": Y}}`.
* **Loops Controlados (`while True`):** Mantêm o menu do terminal ativo infinitamente até que o comando de parada (`break`) seja acionado pelo usuário.
* **Condicionais Complexas (`if / elif / else`):** Filtram a opção escolhida no menu e direcionam o fluxo do programa para a função correta.
* **Operadores de Associação (`in`):** Verificam de forma rápida se uma chave já existe dentro do dicionário antes de realizar operações de escrita ou exclusão.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Você precisa apenas do **Python 3** instalado em seu sistema operacional.

---

## 👤 Autor
* **Gabriel Soares** - [Meu GitHub](https://gbr147).
