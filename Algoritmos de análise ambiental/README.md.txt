
# 🌦️ Análise de Microclima e Simulação de Evacuação

## 📝 Descrição do Projeto
Este repositório contém dois algoritmos de simulação aplicados a cenários cotidianos. O primeiro analisa dados meteorológicos de pontos específicos da Zona Leste (IQA, temperatura e umidade) para gerar notas de bem-estar. O segundo é um simulador de movimentação espacial que utiliza uma máquina de estados para guiar um agente por uma residência até a saída, gerenciando recursos como energia e itens de inventário (chave).

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.10
* **Estruturas:** Listas aninhadas (`nested lists`), Loops `while` e Condicionais complexas.
* **Destaque:** Uso da estrutura `match-case` para classificação de qualidade do ar.

## 📊 Resultados e Aprendizados
O projeto alcançou resultados sólidos na modelagem de decisões lógicas.
* **Pensamento Computacional:** Aprendi a decompor o ato físico de navegação em uma sequência lógica de condições.
* **Gestão de Estados:** Implementei um sistema de retrocesso onde o agente volta espaços ao encontrar obstáculos sem a chave necessária.
* **Lógica Ambiental:** Desenvolvi uma fórmula de penalização matemática para avaliar o conforto térmico local.

## 🔧 Como Executar
1. Clone o repositório.
2. Execute o comando: `python microclima_evacuacao.py`.

---
[Voltar ao início](https://github.com/douglas-lourenco-lima/douglas-lourenco-lima)
