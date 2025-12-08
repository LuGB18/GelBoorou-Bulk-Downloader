from json import dumps, loads, JSONDecodeError
from os import cpu_count, remove

api, userid, apikey, downloadpath, cpu_cores, allow_past_handle = None, None, None, None, None, None

#Salva Configurações DEFAULT pra config.json
def saveconfig() -> None:
    with open('config.json', 'w') as file:
        temp = {
            'gelbooru': {
                'endpoint': 'https://gelbooru.com/index.php',
            },
            'credentials': {
                'userid': '<YOUR USER ID>',
                'apikey': '<YOUR API KEY>'
            },
            'downloads': {
                'folder': '<YOUR DOWNLOAD PATH>'
            },
            'system':{
                'allow_cpu_get_overwhelmed_by_downloads': False
            }
        }
        file.write(dumps(temp, indent=4))
    return

#Retorna e define novas variaaveis.
def loadconfig():
    global api, userid, apikey, downloadpath, cpu_cores, allow_past_handle
    try:
        with open('config.json', 'r') as file:
            config = loads(file.read())
            api = config['gelbooru']['endpoint']
            userid = config['credentials']['userid']
            apikey = config['credentials']['apikey']
            downloadpath = config['downloads']['folder']
            allow_past_handle = bool(config['system']['allow_cpu_get_overwhelmed_by_downloads'])
        #OBS: Esse valor serve pra que as threads não sobrecarreguem o sistema.
        #AVISO: isso PODE deixar os Downloads mais lentos.
        if not allow_past_handle:
            print(f'''WARNING: Overwhelming the System with downloads is disabled. it CAN make the time to download\nLonger since it will wait for other threads to finish.''')
            cpu_cores = cpu_count()
        else:
            print('WARMING: Overwhelming the System with downloads is enabled. it will make your downloads "faster",\n but it will overwhelm your system and could cause crashes or apps not having enough memory.')

    # Caso não seja bem sucedido o parsing ou seja em formato incorreto, cria o arquivo denovo.
    # Caso esteja sem permissão ou sei la oque só da erro e sai do programa antes que faz mais cagada.
    except FileNotFoundError:
        print('config.json not found')
        saveconfig()
        print('config.json saved, please relaunch.')
        exit()

    except JSONDecodeError:
        print('config.json could not be decoded')
        remove('config.json')
        saveconfig()
        print('config.json saved, please relaunch.')
        exit()

    except Exception as e:
        print('error parsing config.json. EXCEPTION:', e)
        exit()

    # Apaga variavel que já foi usada pra não dar cluter na memoria.
    del config
    return