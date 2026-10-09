from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init()

# Lista com os cinco níveis de água
niveis_agua = [
    "Muito baixo (CRÍTICO)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (ALERTA)"
]

# Função que define a cor de cada nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Exibe o título do sistema
print("=== SISTEMA DE MONITORAMENTO DE ÁGUA ===")
print()

# Percorre a lista e exibe cada nível com sua cor
for indice, situacao in enumerate(niveis_agua, start=1):
    cor = definir_cor(indice)
    print(cor + f"Nível {indice} - {situacao}" + Style.RESET_ALL)

print()
print("Monitoramento finalizado.")