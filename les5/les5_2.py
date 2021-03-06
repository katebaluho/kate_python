"""2
Дан словарь с кодированием строк азбуки Морзе
2.1 Реализовать функцию кодирующую текст в морзе строку на вход которой подается строка текста, 
в ответ возвращается 
строка закодированная азбукой морзе. В качестве разделителя морзе символов использовать пробел. 
Пробел кодируется тоже как пробел

2.2 Реализовать функцию декодирующую морзе строку обратно в читаемый текст. 
Обратите внимание что используется только символы латинского Алфавита в lower case. 
При этом строка должна всегда начинаться с заглавной буквы
"""

MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }



def crypted_morze(text):
    invert_morze = {value:key for key,value in MORSE.items()}
    return "".join(map(lambda letter: invert_morze[letter]+' ' if letter != ' ' else ' ', text.lower()))    
      
print("Crypted morze text: "+crypted_morze('Q6 Io p1 m22'))
#result Crypted morze text: --.- -....  .. ---  .--. .----  -- ..--- ..---

def encrypted_morze(text):
    encrypted_morze = "".join(map(lambda letter: MORSE[letter] if letter else ' ', text.split(' ')))
    return encrypted_morze[0].upper() + encrypted_morze[1::]

print("Encrypted morze text: "+ encrypted_morze('--.- -....  .. ---  .--. .----  -- ..--- ..---'))
#result Encrypted morze text: Q6 io p1 m22