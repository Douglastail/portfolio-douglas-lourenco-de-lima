# 🏢 Auditoria de Orçamentos Corporativos (Python)
 
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-concluído-brightgreen.svg)]()
 
## 📖 Sobre o Projeto
Este projeto foi desenvolvido como parte da disciplina de [Programação de Computadores] do curso de [Ciência da Computação]. O objetivo do script é processar e calcular o orçamento de uma estrutura organizacional complexa (dicionários aninhados) de uma multinacional, aplicando regras de negócio dinâmicas e auditoria de execução.
 
A solução foi arquitetada utilizando conceitos avançados de Python para garantir flexibilidade, performance e rastreabilidade.
 
## 🚀 Funcionalidades
- **Cálculo Hierárquico:** Varredura completa da estrutura corporativa, independentemente do nível de profundidade.
- **Filtros Dinâmicos:** Capacidade de ignorar setores específicos e todos os seus subsetores na hora do cálculo financeiro.
- **Conversão de Câmbio:** Suporte a parâmetros opcionais para conversão de moedas em tempo de execução.
- **Sistema de Auditoria:** Monitoramento automatizado de tempo de execução e registro (logging) dos parâmetros utilizados na transação financeira.
 
## 🛠️ Tecnologias e Conceitos Aplicados
Este projeto foi construído utilizando Python puro (Standard Library), com foco nos seguintes paradigmas e recursos:
* **Funções Recursivas (Recursion):** Utilizadas para a navegação na árvore de dados (dicionários aninhados).
* **Decorators:** Implementação do `@auditor` para injetar comportamentos de log e cronometragem sem modificar a lógica de negócios.
* **Empacotamento de Argumentos (`*args` e `**kwargs`):** Utilizados tanto no decorator quanto na função principal para permitir a passagem dinâmica de departamentos a serem ignorados e taxas de câmbio.
 
## ⚙️ Como Executar
 
### Pré-requisitos
* Python 3.8 ou superior instalado.
 
### Passo a Passo
1. Clone este repositório:
   ```bash
   git clone [https://github.com/Douglastail/portfolio-douglas-lima](https://github.com/SeuUsuario/seu-repositorio.git)
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Execute o script principal:
   ```bash
   python main.py
   ```
 
## 🧠 Lógica e Estrutura do Código
Breve explicação de como o código foi organizado:
Projeto desenvolvido em Python para simular a estrutura financeira de uma empresa utilizando dicionários aninhados, recursividade e decorators.

O sistema realiza a análise de departamentos e subsetores corporativos, permitindo calcular automaticamente o orçamento total da empresa de forma dinâmica e escalável..
* **Dados:**Os dados simulados da empresa foram estruturados em um dicionário aninhado, onde cada chave representa um departamento da empresa e os valores podem ser números (orçamentos) ou novos dicionários contendo subsetores internos. Essa estrutura hierárquica simula o funcionamento organizacional de uma empresa real, permitindo navegar e calcular informações de forma recursiva.
 
## 👤 Autor
 
* **[Douglas Lima]** * LinkedIn: [https://www.linkedin.com/in/douglas-louren%C3%A7o-de-lima-981579150]
* E-mail: [dgs.core@hotmail.com]
 
---
*Projeto acadêmico com foco na aplicação prática de conceitos avançados da linguagem Python.*