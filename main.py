import os
import requests
import colorama
#Discord:https://discord.gg/RC4KEDakbd

colorama.init(convert=True)

R = colorama.Fore.RED
G = colorama.Fore.GREEN
B = colorama.Fore.BLUE
C = colorama.Fore.CYAN
X = colorama.Fore.RESET

def main():
    print(f'''{C}
        

 ██▓███  ▓█████  ██ ▄█▀ ██░ ██  █    ██  ▄▄▄▄   
▓██░  ██▒▓█   ▀  ██▄█▒ ▓██░ ██▒ ██  ▓██▒▓█████▄ 
▓██░ ██▓▒▒███   ▓███▄░ ▒██▀▀██░▓██  ▒██░▒██▒ ▄██
▒██▄█▓▒ ▒▒▓█  ▄ ▓██ █▄ ░▓█ ░██ ▓▓█  ░██░▒██░█▀  
▒██▒ ░  ░░▒████▒▒██▒ █▄░▓█▒░██▓▒▒█████▓ ░▓█  ▀█▓
▒▓▒░ ░  ░░░ ▒░ ░▒ ▒▒ ▓▒ ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░▒▓███▀▒
░▒ ░      ░ ░  ░░ ░▒ ▒░ ▒ ░▒░ ░░░▒░ ░ ░ ▒░▒   ░ 
░░          ░   ░ ░░ ░  ░  ░░ ░ ░░░ ░ ░  ░    ░ 
            ░  ░░  ░    ░  ░  ░   ░      ░      
                                              ░ 
                         
    </> Credit  > PekHub
    </> Discord > https://discord.gg/RC4KEDakbd
    </> Github  > https://github.com/PekHub
    {X}''')

    for code in range(0, 10000):
        filename = f'By-PekHub{str(code).zfill(4)}.png'
        with open(f'./Emoji/{filename}', 'wb') as out:
            try:
                data = requests.get(f'https://www.larvalabs.com/cryptopunks/cryptopunk{str(code).zfill(4)}.png').content
                out.write(data)
                print(f'{B}[+] Discord => https://discord.gg/RC4KEDakbd')
            except Exception as ex:
                print(f'{R}[!] Discord => https://discord.gg/RC4KEDakbd')

if __name__ == '__main__':
    try:
        if os.path.exists('./Emoji'):
            pass
        else:
            os.mkdir('Emoji')

        main()
    except:
        pass
