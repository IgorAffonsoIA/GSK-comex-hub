import pandas as pd
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import easygui as eg
from datetime import datetime

def SelecionarArquivo():
    #Abre diálogo para selecionar arquivo Excel
    #try:
        user = os.getlogin()
        path = f"C:\\Users\\{user}\\OneDrive - GSK\\*"
        file = eg.fileopenbox(msg="Selecione um arquivo", default=path)
        return file
    #except:
        #root = tk.Tk()
        #root.withdraw()
        #file = filedialog.askopenfilename(
        #    title="Selecione um arquivo",
        #    filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")]
        #)
        #return file

def SubstituirNA(df):
    #Substitui todos os valores N/A por string vazia
    df = df.replace(np.nan, "")
    print("✓ Valores N/A substituídos por string vazia\n")
    return df

def ValidarDatas(df): #Alterar para que vá direto nas colunas que possum datas. Criar um array com os nomes das colunas e colocar um limite inferior e superior plausível(ano mínimo da planilha e o ano atual +1 ou +2)

    #Valida se as colunas com datas possuem valores realistas
    print("=" * 80)
    print("VALIDAÇÃO DE DATAS")
    print("=" * 80)

    datas_invalidas = []

    #identificar colunas que podem conter datas
    for col in df.columns:
        #verificar se o nome da coluna sugere data
        col_lower = str(col).lower()
        if any(termo in col_lower for termo in ['data']):
            print(f"\n Analisando coluna: '{col}'")

            #verificar cada valor da coluna
            for idx, valor in enumerate(df[col]):
                if valor != "" and valor is not None:
                    try:
                        #tentar converter para datetime
                        if isinstance(valor, str):
                            data = pd.to_datetime(valor, errors='coerce')
                        else:
                            data = pd.to_datetime(valor)

                        #validar se a data é realista (entre 1900 e 2100)
                        if pd.notna(data):
                            ano = data.year
                            if ano < 1900 or ano > 2100:
                                linha = idx + 2  # +2 porque começa em 0 e tem cabeçalho
                                msg = f"⚠️  LINHA {linha}, COLUNA '{col}': Data inválida = {valor} (Ano: {ano})"
                                print(msg)
                                datas_invalidas.append({
                                    'linha': linha,
                                    'coluna': col,
                                    'valor': valor,
                                    'motivo': f'Ano fora do intervalo válido ({ano})'
                                })
                        else:
                            linha = idx + 2
                            msg = f"⚠️  LINHA {linha}, COLUNA '{col}': Formato de data não reconhecido = {valor}"
                            print(msg)
                            datas_invalidas.append({
                                'linha': linha,
                                'coluna': col,
                                'valor': valor,
                                'motivo': 'Formato não reconhecido'
                            })
                    except:
                        linha = idx + 2
                        msg = f"⚠️  LINHA {linha}, COLUNA '{col}': Erro ao processar = {valor}"
                        print(msg)
                        datas_invalidas.append({
                            'linha': linha,
                            'coluna': col,
                            'valor': valor,
                            'motivo': 'Erro ao processar'
                        })

    #resumo da validação
    print("\n" + "=" * 80)
    print("RESUMO DA VALIDAÇÃO")
    print("=" * 80)

    if len(datas_invalidas) == 0:
        print("✓ Nenhuma data inválida encontrada!")
    else:
        print(f"✗ Total de datas inválidas encontradas: {len(datas_invalidas)}")
        print("\nDetalhes:")
        for item in datas_invalidas:
            print(f"  - Linha {item['linha']}, Coluna '{item['coluna']}': {item['valor']} ({item['motivo']})")

    print("\n" + "=" * 80)

    return datas_invalidas

def ValidarFreightForward(df):
    #valida se a coluna 'Freight Forward' contém apenas valores permitidos
    print("=" * 80)
    print("VALIDAÇÃO FREIGHT FORWARD")
    print("=" * 80)

    valores_validos = ["CARGOLUX", "DHL", "Expeditors", "KN", "Lufttansa", "Yusen"]
    valores_invalidos = []

    #verificar se a coluna existe
    if 'Freight Forward' not in df.columns:
        print("⚠️  Coluna 'Freight Forward' não encontrada na planilha!")
        return valores_invalidos

    print(f"\n Analisando coluna: 'Freight Forward'")
    print(f"Valores válidos: {', '.join(valores_validos)}\n")

    #verificar cada valor da coluna
    for idx, valor in enumerate(df['Freight Forward']):
        if valor != "" and valor is not None:
            if valor not in valores_validos:
                linha = idx + 2  # +2 porque começa em 0 e tem cabeçalho
                msg = f"⚠️  LINHA {linha}, COLUNA 'Freight Forward': Valor inválido = '{valor}'"
                print(msg)
                valores_invalidos.append({
                    'linha': linha,
                    'coluna': 'Freight Forward',
                    'valor': valor,
                    'motivo': 'Valor não está na lista de permitidos'
                })

    #resumo da validação
    print("\n" + "=" * 80)
    print("RESUMO DA VALIDAÇÃO")
    print("=" * 80)

    if len(valores_invalidos) == 0:
        print("✓ Todos os valores de 'Freight Forward' são válidos!")
    else:
        print(f"✗ Total de valores inválidos encontrados: {len(valores_invalidos)}")
        print("\nDetalhes:")
        for item in valores_invalidos:
            print(f"  - Linha {item['linha']}: '{item['valor']}'")

    print("\n" + "=" * 80)

    return valores_invalidos

def TratarPlanilha(file):
    #função principal que lê o arquivo e chama as funções de tratamento
    try:
        #ler o arquivo Excel
        df = pd.read_excel(file, sheet_name="Sheet1")
        print(f"Arquivo carregado: {file}")
        print(f"Dimensões: {df.shape[0]} linhas x {df.shape[1]} colunas\n")

        #chamar funções de tratamento
        df = SubstituirNA(df)
        erros_datas = ValidarDatas(df)
        erros_freight = ValidarFreightForward(df)

        print("\n✓ Processamento concluído!")

        #salvar planilha tratada
        df.to_excel(file, sheet_name="Sheet1", index = False)
        print(f"✓ Arquivo salvo: {file}")

        return df, erros_datas, erros_freight

    except Exception as e:
        print(f"❌ Erro ao processar arquivo: {str(e)}")
        return None, None, None

#execução principal
if __name__ == "__main__":
    #selecionar arquivo
    arquivo = SelecionarArquivo()

    if arquivo:
        #processar planilha
        df, erros_datas, erros_freight = TratarPlanilha(arquivo)

        if df is not None:
            print(f"\nPrimeiras linhas do DataFrame:\n{df.head()}")
    else:
        print("Nenhum arquivo selecionado.")