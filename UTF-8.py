texte = str(input("Tapez votre texte à convertir en UTF-8"))
for lettre in texte:
    binary = str(bin(ord(lettre)))[2:]
    if len(binary) < 8:
        print(f"0{binary}", end=" ")
    elif len(binary) < 12:
        for i in range(11-len(binary)):
            binary = "0" + binary
        print(f"110{binary[:5]} 10{binary[5:]}", end=" ")
    elif len(binary) < 17:
        for i in range(16-len(binary)):
            binary = "0" + binary
        print(f"1110{binary[:4]} 10{binary[5:9]} 10{binary[9:]}", end=" ")
    else:
        for i in range(21-len(binary)):
            binary = "0" + binary
        print(f"11110{binary[:3]} 10{binary[4:8]} 10{binary[8:14]} 10{binary[14:]}", end=" ")
