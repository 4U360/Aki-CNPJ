from akicnpj.reader import AkiPaisReader

if __name__ == "__main__":
    with AkiPaisReader(r"E:\1.0 Sources\1.5 Django\4U360\AkiCNPJ\data\tabela\pais\F.K03200$Z.D10510.PAISCSV",
                       encoding="iso-8859-1") as reader:
        for row in reader.rows:
            print(row.to_csv())
