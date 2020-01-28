import speedtest
from hurry.filesize import size

s = speedtest.Speedtest()

option = int(input('''What do you want to know:
1. Upload speed
2. Download speed
3. Ping \n'''))

if option == 1:
    print('Loading...')
    print('Upload speed is: ' + size(s.upload()) + '/s')
elif option == 2:
    print('Loading...')
    print('Download speed is: ' + size(s.download()) + '/s')
elif option == 3:
    server = []
    s.get_servers(server)
    print('Loading...')
    print('Ping speed is: ' + size(s.results.ping) + '/s')
else:
    print('Invalid option')
