import random

# Funcție pentru a afișa tabla de joc
def afiseaza_tabla(tabla):
    for i in range(3):
        print(" | ".join(tabla[i]))
        if i < 2:
            print("-" * 9)

# Funcție pentru a verifica dacă un jucător a câștigat
def verifica_castigator(tabla, jucator):
    for i in range(3):
        # Verifică liniile
        if tabla[i][0] == tabla[i][1] == tabla[i][2] == jucator:
            return True
        # Verifică coloanele
        if tabla[0][i] == tabla[1][i] == tabla[2][i] == jucator:
            return True
    # Verifică diagonalele
    if tabla[0][0] == tabla[1][1] == tabla[2][2] == jucator:
        return True
    if tabla[0][2] == tabla[1][1] == tabla[2][0] == jucator:
        return True
    return False

# Funcție pentru a verifica dacă tabla este completă (egalitate)
def este_plina(tabla):
    for i in range(3):
        for j in range(3):
            if tabla[i][j] == " ":
                return False
    return True

# Funcție pentru a alege o mișcare aleatorie (AI)
def miscare_ai(tabla, jucator):
    posibile_miscari = []
    for i in range(3):
        for j in range(3):
            if tabla[i][j] == " ":
                posibile_miscari.append((i, j))
    
    # Alege o mișcare aleatorie
    return random.choice(posibile_miscari)

# Funcție principală care gestionează jocul cu 2 jucători sau 1 jucător vs AI
def joc_tic_tac_toe():
    print("Bine ai venit la Tic Tac Toe!")
    # Alegerea modului de joc
    while True:
        mod_joc = input("\nAlegeți modul de joc:\n1. 2 Jucători\n2. Jucător vs AI\nAlege (1 sau 2): ")
        if mod_joc == '1' or mod_joc == '2':
            break
        else:
            print("Opțiune invalidă. Încercați din nou.")
    
    # Alegerea simbolului
    while True:
        simbol = input("\nAlegeți simbolul: X sau O: ").upper()
        if simbol == 'X' or simbol == 'O':
            break
        else:
            print("Simbol invalid. Încercați din nou.")
    
    if simbol == 'X':
        jucatori = ["X", "O"]
    else:
        jucatori = ["O", "X"]

    tura = 0  # Tura începe cu 0
    tabla = [[" " for _ in range(3)] for _ in range(3)]  # Creează tabla goală
    
    while True:
        afiseaza_tabla(tabla)
        jucator_curent = jucatori[tura % 2]
        
        if mod_joc == '1' or (mod_joc == '2' and jucator_curent == simbol):
            # Jucătorul uman
            print(f"\nEste rândul jucătorului {jucator_curent}")
            while True:
                try:
                    linie = int(input("Alege linia (0, 1, 2): "))
                    coloana = int(input("Alege coloana (0, 1, 2): "))
                    if tabla[linie][coloana] == " ":
                        tabla[linie][coloana] = jucator_curent
                        break
                    else:
                        print("Locul este deja ocupat. Alege altă poziție.")
                except (ValueError, IndexError):
                    print("Input invalid. Încearcă din nou.")
        else:
            # AI (alege o mișcare aleatorie)
            print(f"\nEste rândul AI-ului (simbolul {jucator_curent})")
            linie, coloana = miscare_ai(tabla, jucator_curent)
            tabla[linie][coloana] = jucator_curent
            print(f"AI-ul a ales linia {linie}, coloana {coloana}")

        # Verifică dacă jucătorul curent a câștigat
        if verifica_castigator(tabla, jucator_curent):
            afiseaza_tabla(tabla)
            print(f"\nJucătorul {jucator_curent} a câștigat!")
            break
        
        # Verifică dacă tabla este completă (egalitate)
        if este_plina(tabla):
            afiseaza_tabla(tabla)
            print("\nEste o remiză!")
            break
        
        # Schimbă tura
        tura += 1

# Meniu principal
def meniu_principal():
    while True:
        joc_tic_tac_toe()
        raspuns = input("\nVrei să joci din nou? (da/nu): ").lower()
        if raspuns != 'da':
            print("Mulțumim că ai jucat! La revedere!")
            break

# Pornește jocul
meniu_principal()
