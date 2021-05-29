from akicnpj.reader import AkiCnaeReader

if __name__ == "__main__":
    with AkiCnaeReader(r"E:\1.0 Sources\1.5 Django\4U360\AkiCNPJ\data\tabela\cnae\F.K03200$Z.D10510.CNAECSV",
                       encoding="iso-8859-1") as reader:
        for row in reader.rows:
            print(row.to_csv())
