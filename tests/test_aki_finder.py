from akicnpj.finder import AkiFinder

if __name__ == "__main__":
    for file in AkiFinder().search():
        print(file)
