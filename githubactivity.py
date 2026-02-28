import sys
import urllib.request
import json

def main():
    
    if len(sys.argv) > 1:
        
        username = sys.argv[1]

        url = f'https://api.github.com/users/{username}/events'
        try:
            with urllib.request.urlopen(url) as f:
                response = json.loads(f.read())
                # print(json.dumps(response, indent=4))

                for i in response:
                    if i['type'] == 'WatchEvent':
                         print(f'Starred {i['repo']['name']}')
                    elif i['type'] == 'PushEvent':
                        print(f'Pushed {i['repo']['name']}')
                    elif i['type'] == 'IssuesEvent':
                        print(f'Opened a new issue in {i['repo']['name']}')

        except:
            print('Error with finding a user')
            

    else:
        print('No Username Passed!')

if __name__ == '__main__':
    main()