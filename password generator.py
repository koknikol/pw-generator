import random
slova = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
brojevi = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simboli = ['!', '#']

print("Dobrodosao na Generator Passworda! ")

broj_slova = int(input("Koliko zelis slova u passwordu? \n"))
broj_brojeva = int(input("Koliko zelis brojeva u passwordu? \n"))
broj_simbola = int(input("Koliko zelis simbola u passwordu? \n"))

# ----------------------------LAGANI PASSWORD SA REDOSLIJEDOM -------------------------------

password = ""

for char in range(1, broj_slova + 1):
    password += random.choice(slova)

for char in range(1, broj_brojeva + 1):
    password += random.choice(brojevi)

for char in range(1, broj_simbola + 1 ):
    password += random.choice(simboli)

print("Laksi password sa redoslijedom: ", password)



# ================================= TEZI PASSWORD KOJI JE IZMIJESAN (SHUFFLE) =================================


password_lista = []

for char in range(1, broj_slova + 1):
    password_lista.append(random.choice(slova))

for char in range(1, broj_simbola + 1):
    password_lista.append(random.choice(simboli))

for char in range(1, broj_brojeva + 1):
    password_lista.append(random.choice(brojevi))

random.shuffle(password_lista)

password = ""
for char in password_lista:
    password += char
print(f"Tezi password koji je izmijesan: {password}")