#Importa só o nessesario. sem deixar cluter na memoria.

#Bibilhoteca Personalizada pra evitar cluter na logica principal.
import configlib
from gelboorulib import downloadpost, getposts

from time import sleep
from threading import Thread, enumerate
from requests import get



#Define as tags que o usuario quer e o tanto de paginas que o usuario quer carregar.
def main():
    tags = str(input('Please enter tags separated by spaces: '))

    #Previne que o usuario quer cagar com o codigo com um 1,* ou string.
    try:
        pages = int(input('Please enter pages you would like to download (10 posts per page): '))
    except ValueError:
       print('please enter a valid integer.')
       main()

    #Verifica se o ser humano tem mente o suficiente e não mete um -1.
    if pages <= 0:
       print(' Please enter a valid amount of pages.')
       main()

    #Evita que o GelBooru retorne 401, 404 ou algo desse tipo.
    try:
        posts = getposts(tags, pages, configlib.api, configlib.apikey, configlib.userid)
    except ConnectionError:
        print('Connection error, please try again later.')
        exit()
    print('Downloads take time! the script is not stuck. please be patient.')
    for post in posts:
        url = post
        name = post.split('/')[-1]
        match configlib.allow_past_handle:
            case False:
                # Deixa pelo menos 1 LPU pro sistema. evita Fatal Crash.
                if not enumerate() > configlib.cpu_cores - 1:
                    Thread(target=downloadpost, args=(url, name, configlib.downloadpath), daemon=True).start()
                else:
                    sleep(0.1)
            case True:
                Thread(target=downloadpost, args=(url, name, configlib.downloadpath), daemon=True).start()
    while not len(enumerate()) == 1:
        sleep(0.5)
    exit()


if __name__ == '__main__':
    # Carrega Config
    configlib.loadconfig()
    # Executa Logica Principal.
    try:
        main()
    except KeyboardInterrupt:
        exit()