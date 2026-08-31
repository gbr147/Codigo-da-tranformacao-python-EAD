import os

# Variável global para o histórico
historico_detalhado = []

def limpar_e_converter(valor):
    """Converte a entrada para float ou int dependendo do conteúdo."""
    try:
        if '.' in valor:
            return float(valor)
        return int(valor)
    except ValueError:
        return None

def realizar_calculo():
    """Gerencia a parte de cálculos aritméticos."""
    v1 = input("Primeiro número: ")
    v2 = input("Segundo número: ")
    
    n1 = limpar_e_converter(v1)
    n2 = limpar_e_converter(v2)

    if n1 is None or n2 is None:
        print("[ERRO] Por favor, digite números válidos.")
        return

    print("Operações: [1]+ [2]- [3]* [4]/")
    op_mat = input("Operação: ")
    
    simbolo, res = "", 0
    
    if op_mat == '1': simbolo, res = "+", n1 + n2
    elif op_mat == '2': simbolo, res = "-", n1 - n2
    elif op_mat == '3': simbolo, res = "*", n1 * n2
    elif op_mat == '4':
        if n2 == 0:
            simbolo, res = "/", "Indeterminado"
        else:
            simbolo, res = "/", n1 / n2
    else:
        print("[ERRO] Operação inválida.")
        return

    registro = f"Cálculo: {n1} {simbolo} {n2} | Resultado: {res}"
    print(f"\n>> {registro}")
    historico_detalhado.append(registro)

def gerenciar_porcentagem():
    """Gerencia os cálculos de porcentagem."""
    try:
        v_porcent = float(input("Valor da porcentagem: "))
        v_total = float(input("Valor base: "))
        
        print("1. Parte (X% de Y) | 2. Acréscimo (Y + X%) | 3. Desconto (Y - X%)")
        tipo_p = input("Opção: ")
        
        parte = (v_porcent / 100) * v_total
        
        if tipo_p == '1':
            msg = f"{v_porcent}% de {v_total} é {parte}"
        elif tipo_p == '2':
            msg = f"{v_total} com acréscimo de {v_porcent}% = {v_total + parte}"
        elif tipo_p == '3':
            msg = f"{v_total} com desconto de {v_porcent}% = {v_total - parte}"
        else:
            print("[ERRO] Opção inválida.")
            return
            
        print(f"\n>> {msg}")
        historico_detalhado.append(msg)
    except ValueError:
        print("[ERRO] Digite valores numéricos.")

def exibir_historico():
    """Mostra o histórico acumulado."""
    print("\n--- HISTÓRICO DE OPERAÇÕES ---")
    if not historico_detalhado:
        print("Nenhum cálculo realizado.")
    else:
        for i, item in enumerate(historico_detalhado, 1):
            print(f"{i}. {item}")

# --- LOOP PRINCIPAL (MENU) ---
while True:
    print("\n==============================")
    print("      CALCULADORA PYTHON")
    print("==============================")
    print("1. Calcular (Inteiro/Decimal)")
    print("2. Porcentagem")
    print("3. Ver Histórico Detalhado")
    print("0. Sair")
    
    escolha = input("\nOpção: ")

    if escolha == '1':
        realizar_calculo()
    elif escolha == '2':
        gerenciar_porcentagem()
    elif escolha == '3':
        exibir_historico()
    elif escolha == '0':
        print("Encerrando... Até à próxima!")
        break
    else:
        print("Opção Inválida!")