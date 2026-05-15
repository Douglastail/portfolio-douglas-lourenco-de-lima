
# Sistema de Auditoria de Recursos Corporativos
> Diego Marques de Carvalho
"""

import time
@auditor
def calcular_orcamento(TI, *recursos_humanos, **financeiro):
  print(f"Setor de tecnologia da informação: {TI}")
  print(f"Recursos humanos: {recursos_humanos}")
  print(f"Financeiro: {financeiro}")
  orcamento_total = 0
  if TI:
    print("\n Tecnologias de tecnologia da informação:")
    for TI, quantidade in TI.items():
      print(f"- {TI}: {quantidade}")

  if recursos_humanos:
    print("\n Recursos humanos:")
    for recursos_humanos, quantidade in recursos_humanos[0].items():
      print(f"- {recursos_humanos}: {quantidade}")

  if financeiro:
    print("\n Financeiro:")
    for financeiro, quantidade in financeiro.items():
      print(f"- {financeiro}: {quantidade}")
      orcamento_total += quantidade
  print(f"Orçamento geral:", orcamento_total)

empresa_data = {
    "Matriz": {
        "TI": {
            "Infraestrutura": {
                "Servidores": 50000,
                "Seguranca": 30000
            },
            "Desenvolvimento": {
                "Frontend": 20000,
                "Backend": 25000,
                "DevOps": 15000
            }
        },
        "RH": {
            "Recrutamento": 10000,
            "Treinamento": 12000,
            "Cultura": {
                "Eventos": 5000,
                "Brindes": 2000
            }
        },
        "Financeiro": 40000
    }
}

import time

def auditor(func):
  def wrapper(*args, **kwargs):
        print("\n--- Auditoria: Início do Cálculo ---")
        print(f"Função sendo auditada: {func.__name__}")
        print(f"Argumentos posicionais: {args}")
        print(f"Argumentos nomeados: {kwargs}")

        start_time = time.time()
        resultado = func(*args, **kwargs)
        end_time = time.time()

        print(f"Tempo de execução do código: {end_time - start_time:.4f} segundos")
        return resultado
  return wrapper

calcular_orcamento(
    empresa_data["Matriz"]["TI"],
    empresa_data["Matriz"]["RH"],
    empresa_data["Matriz"]["Financeiro"]
)
