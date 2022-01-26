import json
import clipboard
import sys

SAVED_DATA = 'clipboard.json'


def save_data(filepath, data):
    '''file path: json file '''
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    '''laod a json file '''
    try :
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return{}


save_data("test.json", {"key": "value"})

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save':
        print('save')
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print('Data saved!')
    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data Copied to clipboard.')
        else:
            print('The key does not exist')
    elif command == 'list':
        print(data)
    else:
        print('Unknown Command')
else:
    print("Please pass exactly one command")