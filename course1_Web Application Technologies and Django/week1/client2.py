import urllib.request

fhand = urllib.request.urlopen('http://127.0.0.1:7000/romeo.txt')
for line in fhand:
    print(line.decode().strip())
