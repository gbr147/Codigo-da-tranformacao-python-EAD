'''
javascript object notation (json) é um formato leve de troca de dados
'''


import json


with open('arquivo_leitura_em_json_gabrielsoares.json', 'r') as arquivo:
    dados_arquivos = json.load(arquivo)

dados_formatados = []

for item in dados_arquivos:

    aluno_formatado = {

        "Nome Completo": item.get ("nome") or item.get("Nome Completo"),
        "Idade": item.get("Idade"),
        "CEP": item.get("cep") or item.get("CEP"),
        "ResgMatr": item.get("resgmatr") or item.get("ResgMater"),
        "E-mail": item.get("email") or item.get("Email")
    }
    dados_formatados.append(aluno_formatado)

with open('alunos_indicadores.json', 'w', encoding='utf-8') as novo_arquivo:
    json.dump(dados_formatados, novo_arquivo, ensure_ascii=False, indent=2)

print("Novo arquivo 'alunos_indicadores.json' criado com sucesso!")