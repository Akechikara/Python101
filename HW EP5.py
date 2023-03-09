# แสดงค่าพลังโจมตีและจุดอ่อนของโปเกมอน

def checkpow(pokemon):
    for f in pokemon.items():
        if f[1] >= 5:
            print(f[0], f[1])

def checkweak(pokemon):
    for f in pokemon.items():
        if f[1] <= 18:
            print(f[0], f[1])

pokemon = {
    'Agumon':5, 'Biyomon':4, 'Gabumon':5, 'Greymon':20, 'Birdramon':18, 'Garurumon':19, 'MetalGreymon':50}

checkpow(pokemon)
checkweak(pokemon)

