from akicnpj.reader import AkiMunicipioReader

if __name__ == "__main__":
    with AkiMunicipioReader(r"E:\1.0 Sources\1.5 Django\4U360\AkiCNPJ\data\tabela\municipio\F.K03200$Z.D10510.MUNICCSV") as reader:
        for row in reader.rows:
            print(row.to_csv())