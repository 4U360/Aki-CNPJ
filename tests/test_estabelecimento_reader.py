from akicnpj.reader import AkiEstabelecimentoReader

if __name__ == "__main__":
    with AkiEstabelecimentoReader(
            r"E:\1.0 Sources\1.5 Django\4U360\AkiCNPJ\data\estabelecimento\K3241.K03200Y0.D10510.ESTABELE",
            encoding="iso-8859-1") as reader:
        for row in reader.rows:
            print(row.to_json())
