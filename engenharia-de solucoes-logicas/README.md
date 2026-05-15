# 🚦 Controle de Semáforo Inteligente

Este é um projeto desenvolvido em **Portugol** que simula o funcionamento de um sistema de controle de tráfego e semáforos inteligentes. O objetivo principal é gerenciar o tempo de sinal verde e tomar ações de redirecionamento ou segurança com base no fluxo de veículos, presença de pedestres e condições de congestionamento em tempo real.

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Portugol (compatível com o VisuAlg)
* **Paradigma:** Lógica de Programação e Estruturas Condicionais/Repetição

---

## 📋 Sobre o Projeto

O algoritmo simula um loop contínuo de monitoramento urbana. Ele coleta dados das vias, processa o tempo necessário para o sinal verde e decide se há necessidade de intervenções (como desvios por congestionamento ou paradas de emergência para pedestres).

### 📥 Coleta de Dados (Entradas)
O sistema interage com o usuário solicitando as seguintes informações a cada ciclo:
* **Nível de Tráfego:** Estado atual da via (ex: "intenso").
* **Velocidade Média:** Velocidade dos veículos na via.
* **Quantidade de Veículos:** Número total de automóveis contabilizados.
* **Congestionamento:** Identificação se a via está travada (`verdadeiro` / `falso`).
* **Presença de Pedestres:** Identificação de pedestres aguardando para atravessar (`verdadeiro` / `falso`).

---

## 🧠 Lógica de Decisão e Regras de Negócio

O sistema baseia-se em um tempo inicial padrão de **10 segundos** para o sinal verde e aplica as seguintes regras:

### 🔹 Decisão 1: Trânsito Intenso
Se o nível de tráfego for igual a `"intenso"`, o sistema adiciona tempo extra para escoar os veículos:
$$\text{tempo\_verde} = \text{tempo\_verde} + 5$$

### 🔹 Decisão 2: Redirecionamento de Fluxo
Caso seja detectado congestionamento (`congestionamento = verdadeiro`):
* O sistema dispara o alerta: `Ação: Redirecionar`.
* Caso contrário, mantém o monitoramento normal.

### 🔹 Decisão 3: Preferência de Pedestres
Se houver pedestres tentando atravessar (`pedestre = verdadeiro`):
* O sistema prioriza a segurança e altera o estado para: `Ação: Sinal de Pedestres`.
* Caso contrário, mantém o fluxo `NORMAL`.

---

## 🔄 Estrutura de Repetição e Encerramento

O algoritmo roda dentro de um bloco `enquanto (continuar = verdadeiro)`. No final de cada ciclo, o sistema:
1. Atualiza o status geral (`"Sistema atualizado"`).
2. Pergunta ao usuário se a tarefa deve continuar operando.
3. Se o usuário decidir encerrar, o loop é quebrado e exibe a mensagem: `"SISTEMA ENCERRADO"`.

---

## 💻 Estrutura das Variáveis

O código utiliza as seguintes variáveis globais para o controle:

| Variável | Tipo | Descrição |
| :--- | :--- | :--- |
| `trafego` | Caractere | Armazena o nível do fluxo (ex: "intenso") |
| `velocidade` | Inteiro | Mede a velocidade média da via |
| `veiculos` | Inteiro | Conta a quantidade de veículos |
| `tempo-verde` | Inteiro | Controla o tempo de abertura do sinal |
| `congestionamento` | Logico | Define se há retenção total na via |
| `pedestre` | Logico | Indica presença de pedestres para travessia |
| `continuar` | Logico | Condição de parada do loop principal |

---

## 🚀 Como Executar

1. Baixe e instale o **VisuAlg** (ou utilize um interpretador Portugol de sua preferência).
2. Copie o código fonte do arquivo principal.
3. Cole no editor do VisuAlg.
4. Pressione `F9` para rodar e interaja com o console inserindo os dados solicitados.
