# 🛡️ Sistema de Auditoria de Vendas e Segurança de Dados

## 📝 Descrição do Projeto
Este projeto simula um motor de auditoria financeira desenvolvido para identificar anomalias em transações. O sistema utiliza lógica de média aritmética para detectar discrepâncias (outliers) e possui um mecanismo de **"Quarentena"** automática caso a média das operações supere o limite de segurança estabelecido.

O desenvolvimento focou em resolver problemas reais de execução, como o ajuste dinâmico de limites através de variáveis globais e o tratamento de entradas de dados inválidas para garantir a continuidade do serviço.

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.10
* **Conceitos:** Escopo de Variáveis (`global`), Tratamento de Exceções (`try/except`) e Casting de tipos.
* **Ferramentas:** VS Code / Terminal Python.

## 📊 Resultados e Aprendizados
O projeto demonstram a eficácia da validação de tipos e controle de fluxo.
* **Resiliência:** Implementei travas contra erros de digitação (ValueErrors), garantindo a integridade dos dados.
* **Análise Crítica:** Identifiquei os perigos do uso excessivo de variáveis globais, como a possibilidade de alterações indevidas e inconsistência de estado.
* **Correção de Estrutura:** Apliquei boas práticas de identação e espaçamento, fundamentais para a sintaxe do Python.

## 🔧 Como Executar
1. Clone o repositório.
2. Execute o comando: `python auditoria_vendas.py`.
3. Siga as instruções no console para validar as vendas.
