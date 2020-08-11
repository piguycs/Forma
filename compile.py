import requests, os
key = "forma is great"
command = "sudo llc -relocation-model=pic -filetype=obj output.ll"
f = open("output.ll","r")
data= f.read() 
f.close()
print("Uploading")
os.system("scp output.ll root@161.35.159.211:/root/output.ll")
url = "http://161.35.159.211:4042/"+str(key)+"/"+str(command)
print("Downloading")
os.system("scp root@161.35.159.211:/root/output.o output.o")
#r = requests.get(url = url) 
#print(r.text[:100])
#Now I'll set up a webserver shit thing on the ixserver 
#also try vscode(mc titles be like)
print("====== Output ======")
os.system("chmod +x compile && ./compile")