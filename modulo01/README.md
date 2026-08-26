# pensamento_computacional_projeto

# 🏎️ Sistema de Vendas de Carros (CLI)

O **Sistema de Vendas de Carros** é uma aplicação em linha de comando (CLI) desenvolvida em **Python** para gerenciar o estoque, cadastro e a venda de veículos de uma concessionária digital. 

O projeto foi estruturado seguindo o modelo de histórias de usuários de múltiplos stakeholders (PO, QA, Dev, UX, IA) para garantir eficiência de terminal antes da futura migração para interfaces gráficas (GUI).

---

## 📌 Índice
* [Sobre as Visões do Projeto](#-sobre-as-visões-do-projeto)
* [Funcionalidades Principais](#-funcionalidades-principais)
* [Tecnologias Utilizadas](#-tecnologias-utilizadas)
* [Estrutura de Dados Interna](#-estrutura-de-dados-interna)
* [Ciclo de Vida do Desenvolvimento](#-ciclo-de-vida-do-desenvolvimento)
* [Como Executar o Projeto](#-como-executar-o-projeto)

---

## 👥 Sobre as Visões do Projeto

A concepção do sistema atende às necessidades de diferentes perfis mapeados no escopo:
* **Product Owner (PO):** Controle total de vendas e acompanhamento de produtos em estoque.
* **Quality Assurance (QA / Cliente):** Interface rápida para simular a compra de veículos favoritos de forma ágil.
* **Tech / Dev:** Código modular focado em estruturas eficientes para regras de negócio do setor automotivo.
* **UX Designer:** Construção lógica e limpa de menus no terminal visando facilidade na experiência do usuário.
* **Analista de Dados (IA):** Coleta e estrutura primária de dados para futuras análises de consumo e otimização de estoque.

---

## ✨ Funcionalidades Principais

* **Cadastro Limitado de Veículos (Vagas):** Sistema com limite dinâmico de até 5 produtos cadastrados simultaneamente no estoque para garantir otimização de memória.
* **Listagem Detalhada:** Exibição em tempo real do catálogo contendo Nome, Preço, Unidades em Estoque, Marca e Cores disponíveis.
* **Venda com Baixa Automática:** Registro de transações por busca nominal do veículo (ignora maiúsculas/minúsculas) com cálculo automático do valor total e validação se há estoque disponível.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem Base:** Python 3
* **Interface:** CLI (Command Line Interface) via Terminal.
* **Controle de Fluxo:** Estruturas condicionais (`if`, `elif`, `else`) e loops contínuos (`while True`).

---

## 📊 Estrutura de Dados Interna

O sistema já inicializa com um catálogo de demonstração pré-populado com os seguintes modelos do mercado brasileiro:
* **Volkswagen T-Cross:** 27 unidades em estoque.
* **Fiat Argo:** 13 unidades em estoque.
* **Chevrolet Onix:** 19 unidades em estoque.
* **Hyundai HB20:** 23 unidades em estoque.
* **Toyota Corolla:** 29 unidades em estoque.

---

## 🔄 Ciclo de Vida do Desenvolvimento

O repositório segue rigorosamente as seguintes etapas de engenharia de software:
1. **Planejamento:** Definição e levantamento de requisitos de negócios automotivos.
2. **Análise:** Modelagem de dados baseada em variáveis de atributos (Nome, Preço, Marca, Cores e Estoque).
3. **Desenvolvimento:** Escrita do algoritmo puramente em terminal.
4. **Testes:** Validação de fluxos de entrada (`input`) e saídas financeiras.
5. **Implantação & Manutenção:** Estágio atual do projeto focado em ajustes antes da expansão para GUI.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Você precisa apenas do **Python 3** configurado na sua máquina.

### Execução via Terminal
1. Clone este repositório no seu computador:
   ```bash
   git clone https://github.com
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Rode o script principal:
   ```bash
   python nome_do_seu_arquivo.py
   ```

---

## 👤 Autor
* **Gabriel Soares** - Meu GitHub:(https://gbr147).
