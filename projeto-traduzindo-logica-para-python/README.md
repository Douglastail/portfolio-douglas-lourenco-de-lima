# 🐍 Conversão de Lógica: Pseudocódigo para Python

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Logic](https://img.shields.io/badge/Logic-Algorithms-red?style=for-the-badge)

Este repositório contém a tradução de algoritmos complexos de **pseudocódigo** para a linguagem **Python**, focando no uso correto de tipos de dados, estruturas de repetição e condicionais.

## 🚀 Funções Implementadas

O script aborda quatro cenários de lógica de programação:
1.  **Processamento de Vendas:** Cálculo de total com validação de entrada e descontos progressivos (10% acima de R$ 500 e 5% acima de R$ 200).
2.  **Análise de Clima:** Coleta de temperaturas semanais, cálculo de média e emissão de alertas para climas extremos (acima de 45°C ou abaixo de -5°C).
3.  **Sistema de Notas:** Gestão de médias escolares com fluxo de decisão para Aprovação, Recuperação e Reprovação.
4.  **Simulador de Poupança:** Simulação de investimento com juros compostos e aportes mensais, incluindo monitoramento de metas financeiras.

---

## 🧠 Questões de Reflexão

### 1. Sobre Tipagem e `input()`
No Python, a função `input()` sempre retorna os dados no formato de **String**. 
*   **Consequência:** Se esquecermos de converter com `int()` ou `float()`, o Python não conseguirá realizar cálculos matemáticos. 
*   **Exemplo:** O operador `+` passará a concatenar os textos (ex: "10" + "5" vira "105") em vez de somar os valores numéricos.

### 2. Sobre o `range()` e o Comportamento do Python
Para contar de 1 até o limite exato (incluindo o último número), utilizamos:
`range(1, limite + 1)`

**Por que o Python é assim?**
Diferente do pseudocódigo tradicional, o limite superior do `range` é **exclusivo** (parada antes de atingir o valor). Isso é um padrão de design que facilita a indexação de listas (que iniciam em 0) e ajuda a determinar o número de iterações subtraindo o valor inicial do final.

---

## 🛠️ Tecnologias
*   **Python 3.x**
*   **Markdown**
*   **Bash** (Automação de documentação)

---
*Atividade desenvolvida para o curso de **Análise e Desenvolvimento de Sistemas (ADS)**.*
EOF
