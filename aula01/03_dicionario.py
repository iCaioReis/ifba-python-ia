cadastros = {
    "descricao": "Cadastro de pessoas",
    "pessoas": [
        {
            "nome": "pedro da silva",
            "idade": 35,
            "profissao": "dentista"
        },
        {
            "nome": "josé da silva",
            "idade": 20,
            "profissao": "mecanico"
        },
        {
            "nome": "maria da silva",
            "idade": 27,
            "profissao": "programadora"
        }
    ]
}

if __name__ == "__main__":
    pessoas = cadastros["pessoas"]
    
    for pessoa in pessoas:
        print(f"nome da pessoa: {pessoa['nome']}\nidade: {pessoa['idade']}")
        
    cadastros["versao"] = "1.0"
    
    print(f"vesão do cadastro: {cadastros['versao']}")