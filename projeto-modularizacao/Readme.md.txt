# 🪙 Algoritmo de Cálculo de Troco Inteligente

Este projeto consiste num algoritmo desenvolvido em **Portugol** projetado para automatizar o processo de venda, validação de pagamento e cálculo otimizado do troco em formato de cédulas (notas de 100, 50, 10, 5 e 1). 

O objetivo principal é simular o fluxo lógico do operador de caixa de um estabelecimento comercial, garantindo que o troco seja entregue utilizando a menor quantidade possível de notas.

## 🛠️ Tecnologias e Conceitos Aplicados
* **Linguagem:** Portugol (Compatível com VisuAlg)
* **Estruturas Condicionais:** `SE - ENTÃO - SENÃO` para validação de saldo financeiro.
* **Operadores Matemáticos Próximos do Hardware:** * `DIV` (Divisão Inteira) para determinar a quantidade exata de cada cédula.
  * `MOD` (Resto da Divisão) para atualizar o saldo restante do troco a cada etapa.

---

## 📋 Funcionamento do Sistema

O fluxo do algoritmo divide-se em três etapas principais:

### 1. 📥 Coleta e Validação de Dados
O sistema solicita ao utilizador duas variáveis essenciais:
* `VALOR_COMPRA`: O total financeiro dos produtos adquiridos.
* `VALOR_PAGO`: O montante entregue pelo cliente para saldar a conta.

**Regra de Segurança (Validação):**
Se o `VALOR_PAGO` for menor do que o `VALOR_COMPRA`, o sistema interrompe a execução e exibe o alerta: `"Pagamento Insuficiente"` (ou `"Saldo Insuficiente"`).

---

### 2. 🧠 Lógica de Processamento e Distribuição de Cédulas
Caso o pagamento seja validado com sucesso, o algoritmo calcula o troco bruto:
$$\text{troco} = \text{VALOR\_PAGO} - \text{VALOR\_COMPRA}$$

A partir deste valor, o programa realiza divisões sucessivas em ordem decrescente de valor de nota para otimizar a entrega:

* **Notas de 100:** * `NOTAS100 = troco DIV 100` (Quantidade de notas)
  * `troco = troco MOD 100` (O que sobra vai para a próxima etapa)
* **Notas de 50:** * `NOTAS50 = troco DIV 50`
  * `troco = troco MOD 50`
* **Notas de 10:** * `NOTAS10 = troco DIV 10`
  * `troco = troco MOD 10`
* **Notas de 5:** * `NOTAS5 = troco DIV 5`
  * `troco = troco MOD 5`
* **Notas de 1:** * `NOTAS1 = troco MOD 5` (O valor unitário final restante)

---

### 3. 📤 Saída de Dados (Resultados)
Por fim, a aplicação exibe detalhadamente no ecrã o relatório das notas que devem ser entregues ao cliente:
* Quantidade de Cédulas de 100
* Quantidade de Cédulas de 50
* Quantidade de Cédulas de 10
* Quantidade de Cédulas de 5
* Quantidade de Cédulas de 1

---

## 💻 Estrutura de Variáveis Proposta

| Variável | Tipo | Descrição |
| :--- | :--- | :--- |
| `VALOR_COMPRA` | Real / Numérico | Armazena o preço final da compra |
| `VALOR_PAGO` | Real / Numérico | Armazena o montante pago pelo cliente |
| `troco` | Real / Inteiro | Diferença a ser devolvida ao cliente |
| `NOTAS100` | Inteiro | Totalizador de notas de 100 unidades |
| `NOTAS50` | Inteiro | Totalizador de notas de 50 unidades