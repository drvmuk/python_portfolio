from shared_repository import MORSECODE

# sample_morse = ['..', ' ', '.-', '--', ' ', '-..', '....', '.-.', '..-', '...-']
text = input('Enter text: ')
morse_code = eval(input('Enter morse code: '))

if text:
    obj_ = MORSECODE(text_=text.upper())
    morse = obj_.text_to_morse()
    print(f'Morse code of "{text}" is ::: {morse}')
elif morse_code:
    obj_ = MORSECODE(morse_=morse_code)
    text = obj_.morse_to_text()
    print(f'Regular text of "{morse_code}" is ::: {text}')
else:
    print('Input is missing')
