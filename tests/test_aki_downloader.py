from akicnpj.downloader import *

if __name__ == "__main__":
    AkiEmpresaDownloader().download()
    AkiEstabelecimentoDownloader().download()
    AkiSocioDownloader().download()
    AkiSimplesDownloader().download()
    AkiCnaeDownloader().download()
    AkiMunicipioDownloader().download()
    AkiNaturezaJuridicaDownloader().download()
    AkiPaisDownloader().download()
    AkiQSADownloader().download()
    AkiSituacaoCadastralDownloader().download()
