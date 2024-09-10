cores = ["branco", "preto", "cinza", "vermelho", "amarelo", "verde"]

if __name__ == "__main__":
    for cor in cores:
        print(f"{cor} é uma cor!")
        
    cores.append("ciano")
    
    for indexador, cor in enumerate(cores):
        print(f"{cor} é uma cor na posição: {indexador}!")
        
    cores.remove("branco")
    
    for indexador, cor in enumerate(cores):
        print(f"{cor} é uma cor na posição: {indexador}!")