from akicnpj.reader import AkiCompanyReader

if __name__ == "__main__":
    with AkiCompanyReader(r"E:\1.0 Sources\1.5 Django\4U360\AkiCNPJ\data\empresa\K3241.K03200Y0.D10510.EMPRECSV") as reader:
        for row in reader.rows:
            print(row.to_json())

