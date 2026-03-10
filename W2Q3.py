try:
    vize = float(input('Vize notunuzu girin: '))
    if not ((vize >= 0) and (vize <= 100)):
        print('Invalid, not in range.')
        exit()
    final = float(input('Final notunuzu girin: '))
    if not ((final >= 0) and (final <= 100)):
        print('Invalid, not in range.')
        exit()

    ortalama = vize*0.4 + final*0.6
    print(f'Ortalama: {ortalama:.2f}')

    puan_listesi = [
        (90 , 'AA'),
        (80 , 'BA'),
        (70 , 'BB'),
        (60 , 'CB'),
        (50 , 'CC'),
        (0 , 'FF')
    ]

    for min_puan, puan in puan_listesi:
        if ortalama >= min_puan:
            print(f'Dersi {puan} ile geçtiniz.')
            break
except ValueError as _:
    print(f'Your input is invalid, {_}')
    exit()