from akicnpj.reader import AkiSituacaoCadastralReader

if __name__ == "__main__":
    with AkiSituacaoCadastralReader(r"E:\1.0 Sources\1.5 Django\4U360\AkiCNPJ\data\tabela\situacao_cadastral\F.K03200$Z.D10510.MOTICSV", encoding="iso-8859-1") as reader:
        for row in reader.rows:
            print(row.to_json())