from requests import get
from time import sleep
from os.path import join

#Manda Baixar os dados pelo getdata e salva em disco com o savefile
def downloadpost(url, name):
    try:
        savefile(getdata(url), name)
    except OSError:
        print('could not save file. Halting.')
        exit()
#Baixa os dados em byte do arquivo no GelBooru
def getdata(url: str):
    data = get(url)
    return bytes(data.content)

#Salva arquivo em disco com os dados do getdata
def savefile(data: bytes, name: str) -> bool:
    global savepath
    try:
        with open(join(savepath, name), "wb") as file:
            file.write(data)
        print(f'Wrote Succesfully: {name}')
        return True
    except OSError or IOError or PermissionError as error:
        raise OSError(error)


#Lista os posts com as tags definidas e o numero de paginas que o usuario escolheu.
def getposts(tags: str, pages: int, api: str) -> list:
    global apikey, userid
    posts = []
    i = 1
    while len(posts) < pages:
        params = {
            'page': 'dapi',
            's': 'post',
            'q': 'index',
            'json': '1',
            'limit': '10',
            'pid': str(i),
            'tags': tags.lower(),
            'api_key': apikey,
            'user_id': userid
        }
        bulk = get(api, params=params).json()
        if bulk.status_code != 200:
            raise ConnectionError('conection error')
        for post in bulk['post']:
            posts.append(post['file_url'])
        sleep(1)
        i += 1
    del i
    return posts


