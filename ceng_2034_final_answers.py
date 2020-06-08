#Aynur SALMAN
#!/usr/bin/python3
import os,sys,requests
from urllib.request import urlopen
import hashlib
import uuid

url =["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg","https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png","https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg","http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg","https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"]
#1

print("This is parent process.PID is ",os.getpid())
child =os.fork()
if (child==0):
       print ("This is the child process.PID is ",os.getpid())
       sys.exit(0)
#2

def download_file(url,file_name=None):
 r =requests.get(url,allow_redirects=True)
 file =file_name if file_name else str(uuid.uuid4())
 open(file,'wb').write(r.content)

for i in url:
   download_file(i,file_name=None)
#3

Os.wait()

#4

def heap_reader(f_object, heap_size=1024):
    """Generator that reads a file in heap of bytes"""
    while True:
        heap = f_object.read(heap_size)
        if not heap:
            return
        yield heap

def check_duplicates(paths, hash=hashlib.sha1):
    hashes = {}
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                hash_obj = hash()
                for heap in heap_reader(open(full_path, 'rb')):
                    hash_obj.update(heap)
                file_id = (hash_obj.digest(), os.path.getsize(full_path))
                duplicate = hashes.get(file_id, None)
                if duplicate:
                    print ("Duplicate found: %s and %s" % (full_path, duplicate))
                else:
                    hashes[file_id] = full_path

if sys.argv[1:]:
    check_duplicates(sys.argv[1:])

else:
    print ("Please pass the paths to check as parameters to the script")


for i in url:
    check_duplicates(/home/aynur)












