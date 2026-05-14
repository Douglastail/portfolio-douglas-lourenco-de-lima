
# 🛡️ Auditoria de Vendas: Consistência e Segurança de Dados
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-concluído-brightgreen.svg)]()

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Security](https://img.shields.io/badge/Security-Data%20Auditory-red?style=for-the-badge)
![Data Analysis](https://img.shields.io/badge/Analysis-Outliers-blue?style=for-the-badge)

Este projeto consiste em um sistema de **Auditoria de Vendas Semanais** desenvolvido para identificar anomalias financeiras, praticar o gerenciamento de escopo (Global vs. Local) e aplicar lógica de detecção de discrepâncias (*outliers*).

---

## 📖 Parte 1: Investigação e Descoberta

### 1. Discrepância de Dados (Outliers)
Um *outlier* é um valor que foge drasticamente do padrão do grupo. Ele "mente" sobre a média porque, sendo um cálculo sensível, a média é puxada em direção ao valor extremo. Em um grupo onde quase todos ganham R$ 2.000,00, se uma pessoa ganha R$ 100.000,00, a média dirá que o grupo é "rico", o que não representa a realidade da maioria.

### 2. O Conceito de Normalização
Normalizar ou ignorar extremos serve para encontrar a "tendência central". Ao remover o maior e o menor valor em amostras pequenas, eliminamos ruídos e erros de leitura, obtendo um resultado que reflete melhor o comportamento habitual dos dados.

### 3. Margem de Tolerância
Em auditoria, a margem de tolerância é o limite aceitável de erro ou variação em um registro financeiro. Se a discrepância estiver dentro dessa margem, o registro é aceito; caso contrário, o sistema dispara um alerta de investigação.

---

## 💻 Parte 2: A Aplicação (Regras de Negócio)

O programa simula uma auditoria com as seguintes características:
*   **LIMITE_SEGURANCA:** Variável global que define o teto para médias suspeitas.
*   **Detecção de Anomalia:** O sistema identifica se uma única venda é **5x maior que a média**, sugerindo revisão manual.
*   **Protocolo de Quarentena:** Bloqueio preventivo caso a média geral ultrapasse o limite global.
*   **Escopo Dinâmico:** Uso da palavra-chave `global` para permitir que gestores ajustem parâmetros de segurança em tempo de execução.

---

## 🧠 Parte 3: Reflexão e Metacognição

### O Teste de Estresse
*   **Valores:** Venda 1 = 100 | Venda 2 = 200 | Venda 3 = 5000.
*   **Resultado:** A média sobe para 1766.66. Embora a média esteja abaixo de 10.000, a Venda 3 é muito superior à média, disparando a "REVISÃO MANUAL".

### Aplicação Real em Bancos
O uso de uma variável `global` em sistemas reais é perigoso pois ela pode ser alterada por qualquer parte do código, intencionalmente ou por erro, facilitando fraudes. Em sistemas bancários, esses limites devem ser protegidos por **encapsulamento** ou armazenados em constantes imutáveis e bancos de dados seguros.

### A Experiência Individual
*(Espaço para descrever o erro de indentação ou SyntaxError encontrado durante o código, como a confusão entre o que o interpretador lê e a intenção do programador.)*

---

## 🛠️ Tecnologias
*   **Python 3.x**
*   **Markdown**
*   **Bash** (Automação)

---
*Atividade desenvolvida para o curso de **Análise e Desenvolvimento de Sistemas (ADS)**.*
EOF
