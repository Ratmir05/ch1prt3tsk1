def konvert():
    far = int(input('vvedite farengeit'))
    cel = int(input('vvedite celsiya'))
    return f'rezultat {(far-32) * 5/9}' f'rezultat {cel* 9/5 +32}'
print (konvert())

    #(32 °F − 32) × 5/9 = 0 °C
    #(32 °C × 9/5) + 32 = 89,6 °F
