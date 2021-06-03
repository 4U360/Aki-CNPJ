from akicnpj.finder import AkiFinder
from akicnpj.reader.company import AkiCompanyReader
import pathlib
from pandas import DataFrame
import matplotlib.style
import matplotlib

matplotlib.style.use('ggplot')

ROOT = pathlib.Path(__file__).parent.parent

if __name__ == "__main__":
    df = DataFrame({"porte": [], "Contagem": []})
    portes = {}

    for file in AkiFinder(path=ROOT.joinpath("data").joinpath("extract")).search():

        if file.suffix != ".zip":
            if file.suffix == ".EMPRECSV":

                with AkiCompanyReader(filename=str(file)) as reader:

                    for row in reader.rows:
                        porte = row.tuple.porte
                        if porte == 1:
                            porte = "NÃO INFORMADO"
                        elif porte == 2:
                            porte = "MICRO EMPRESA"
                        elif porte == 3:
                            porte = "EMPRESA DE PEQUENO PORTE"
                        elif porte == 5:
                            porte = "DEMAIS"

                        if porte not in portes:
                            portes[porte] = int(0)

                        portes[porte] += int(1)

    for key, value in portes.items():
        df = df.append({"porte": key, "Contagem": value}, ignore_index=True)

    plot = df.plot(kind="pie", figsize=(6, 6), y="Contagem", labels=df["porte"], use_index=False,
                   colormap="Pastel1", autopct='%1.1f%%', explode=(0, 0, 0.1), shadow=True)
    fig = plot.get_figure()
    fig.suptitle("Empresas por Porte", fontsize=20)
    fig.savefig(pathlib.Path(__file__).stem + ".png")