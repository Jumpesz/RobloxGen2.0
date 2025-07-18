# ContasGeradas.py

with open("contas.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

with open("contas_impressas.txt", "w", encoding="utf-8") as arquivo_saida:
    arquivo_saida.write("Contas geradas:\n\n")
    for linha in linhas:
        # Remove espaços extras ao redor da linha e divide pelo separador " | "
        partes = linha.strip().split(" | ")
        if len(partes) == 2:
            usuario, senha = partes
            arquivo_saida.write(f"Nick: {usuario} | Senha: {senha}\n")
        else:
            print(f"⚠️ Linha ignorada (formato inválido): {linha.strip()}")

print("✅ Arquivo contas_impressas.txt criado com sucesso!")
