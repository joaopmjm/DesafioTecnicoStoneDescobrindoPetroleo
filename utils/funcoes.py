def readCommands(comando):
    comandos = []
    with open(comando,encoding="utf-8") as f:
        line = 0
        current = f.readline()
        while(current != ""):
            current = current.rstrip("\n")
            comandos.append(current)
            current = f.readline()
    return comandos