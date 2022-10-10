from akicnpj.downloader import *

if __name__ == "__main__":
    for file in AkiEmpresaDownloader().download():
        print(file)
    exit(0)
    AkiEstabelecimentoDownloader().download()
    AkiSocioDownloader().download()
    AkiSimplesDownloader().download()
    AkiCnaeDownloader().download()
    AkiMunicipioDownloader().download()
    AkiNaturezaJuridicaDownloader().download()
    AkiPaisDownloader().download()
    AkiQSADownloader().download()
    AkiSituacaoCadastralDownloader().download()
