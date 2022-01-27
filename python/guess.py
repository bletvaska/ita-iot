import random


def play_game(secret=9):
    print('Myslím si číslo od 1 do 20.')

    tip = None
    counter = 5

    while counter > 0:  # secret != tip and
        print(f'Počet zostávajúcich pokusov: {counter}.')
        counter = counter - 1
        tip = input('Tvoj tip: ')
        tip = int(tip)

        if tip > secret:
            print(f'Hmm... Moje číslo je menšie ako {tip}.')

        elif tip < secret:
            print(f'Hmm... Moje číslo je väčšie ako {tip}.')

        else:
            print('Ta ty génius.')
            break

    else:
        print(f'Ta ty si jaká lama. Ta si neuhádol toté tajné číslo, ktoré bolo {secret}. Ta skús nabudúce.')


if __name__ == '__main__':
    play_game(random.randint(1, 20))
    print('Created by (c)2022 mirek, mega šupa Pyton kóder.')