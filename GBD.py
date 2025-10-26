# Import necessary libraries
import os, sys, json #To Handle os related comands and JSON Handling
from time import sleep  # To add delays between requests
from threading import Thread  # For parallel image downloads
import wget, requests  # For HTTP requests and file downloads

# Base API URL for Gelbooru
api = 'https://gelbooru.com/index.php?page=dapi&s=post&q=index'
logfile = os.path.join(os.getcwd(), 'log.json')
log = {'logpath': logfile, 'credsloaded': None, 'finished': False, 'posts': {}}
# Collect user information
# Helper to save settings
def save_config(api_key, user_id):
    config = {'api_key': api_key, 'user_id': user_id}
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)
    print("API settings saved to file.")

# Helper to read an integer with validation and clear messages
def _input_int(prompt, min_v=None, max_v=None):
    while True:
        val = input(prompt).strip()
        if val == '':
            print('Empty input — please enter a number.')
            continue
        try:
            n = int(val)
        except ValueError:
            print('Invalid value — please enter an integer.')
            continue
        if min_v is not None and n < min_v:
            print(f'Value too small — minimum is {min_v}.')
            continue
        if max_v is not None and n > max_v:
            print(f'Value too large — maximum is {max_v}.')
            continue
        return n

try:
    # Try to load API settings from a file
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            api_key = config.get('api_key')
            user_id = config.get('user_id')
        log['credsloaded'] = True
        print("API configuration loaded from file.")
    except FileNotFoundError:
        log['credsloaded'] = False
        print("Configuration file not found, using manual input.")
        api_key = user_id = None

    # Get the max posts per page (max 100)
    limit = _input_int('Enter the limit of posts to capture (max 100): ', 1, 100)

    # Get the number of pages to process
    limitreq = _input_int('Enter the number of pages to load: ', 1, None)

    # If settings were not loaded, ask user for them
    if not api_key:
        api_key = input('Enter your APIKEY: ').strip()
        while not api_key:
            print('Empty APIKEY — please enter your APIKEY.')
            api_key = input('Enter your APIKEY: ').strip()

    if not user_id:
        user_id = input('Enter your USERID: ').strip()
        while not user_id:
            print('Empty USERID — please enter your USERID.')
            user_id = input('Enter your USERID: ').strip()

        # Ask whether to save settings
        save_choice = input('Do you want to save these settings? (y/n): ').lower()
        if save_choice == 'y':
            save_config(api_key, user_id)

    # Tags to filter desired images (allow empty for no filters)
    user_tags = input('Enter tags (leave empty for no filter): ').strip()
    # empty tags are already normalized to an empty string

except Exception as e:
    log = None
    print(f'Error while configuring necessary variables.\nException:{e}')
    raise

# Inicialização de variáveis de controle
pnum = 1  # Page counter
pran = 0  # Post counter within the page

# Manage downloads directory
if os.path.exists('downloads'):
    if os.path.isfile('downloads'):  # If 'downloads' exists as a file, remove it
        os.remove('downloads')
else:
    os.mkdir('downloads')  # Create directory if it doesn't exist


# Function to make a request to the Gelbooru API
def get_request(tags):
    global resp
    # Make the HTTP request and convert the response to JSON
    resp = requests.get(f'{api}&pid={pnum}&limit={limit}&json=1&api_key={api_key}&user_id={user_id}&tags={tags}').json()

# Function to download images in separate threads
def dw_img(link, id, ext):
    # Define output file path
    out_file = os.path.join(os.getcwd(), 'downloads', f'file{id}.{ext}')
    # Skip if file already exists to avoid duplicate downloads
    if not os.path.exists(out_file):
        # Create a new thread for the download
        t = Thread(target=wget.download, args=(link,), kwargs={'out': out_file})
        t.daemon = False  # Thread remains even after main program finishes
        t.start()  # Start the download thread

# Main loop
try:
    # Iterate over the specified number of pages
    while pnum < limitreq + 1:
        # Request posts for the current page
        get_request(user_tags)
        # Process each post on the current page
        while pran < limit:
            # Extract current post info
            url = resp['post'][pran]['file_url']  # Image URL
            ext = url.split('.')[-1]  # File extension
            id = resp['post'][pran]['id']  # Unique post ID -- Can be used for identifying the image on gelboorou
            # Print download info
            print(f'Captured: {url}, Saving as: file{id}.{ext}\n')
            # Start the image download in a separate thread
            dw_img(url, id, ext)
            # Ensure log structure exists for this page
            if pnum not in log['posts']:
                log['posts'][pnum] = []
            log['posts'][pnum].append({'url': url, 'id': id, 'org_file': url.split('/')[-1], 'saved_as': f'file{id}.{ext}'})
            pran += 1
        # Reset post counter and advance to next page
        pran = 0
        pnum += 1
        sleep(1)  # Pause to end the API Time Limit
    print("Closing...")
    log['finished'] = True
    with open(logfile, 'w') as f:
        f = json.dumps(log, indent=2)
    sys.exit() #Proper Exit Handling

# Handle user interrupt (Ctrl+C)
except KeyboardInterrupt:
    print('Closing...')
    sys.exit() #Proper Exit Handling