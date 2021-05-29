from akicnpj.reader import AkiSimplesReader

if __name__ == "__main__":
    with AkiSimplesReader(r"E:\1.0 Sources\1.5 Django\4U360\AkiCNPJ\data\tabela\simples\F.K03200$W.SIMPLES.CSV.D10510", encoding="iso-8859-1") as reader:
        for row in reader.rows:
            print(row.to_json())