def plural(palavra):
    saida = list(palavra)
    ultimo = (len(saida)-1)
    if saida[ultimo] == "l":
        saida.pop(ultimo)
        saida.append("i")
        saida.append("s")
    elif saida[ultimo] == "r" or saida[ultimo] == "s" or saida[ultimo] == "z":
        saida.append("e")
        saida.append("s")
    elif saida[ultimo] == "m":
        saida.pop(ultimo)
        saida.append("n")
        saida.append("s")
    else:
        saida.append("s")
    return "".join(saida)

palavra = input("Informe a palavra: ")
print("O plural de %s é %s" %(palavra, plural(palavra)))
