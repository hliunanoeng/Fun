import sys
import subprocess
import requests


if 'darwin' in sys.platform:
    print('Running \'caffeinate\' on MacOSX to prevent the system from sleeping')
    subprocess.Popen('caffeinate')

folder = "/Users/hliu/Desktop/imgs1"
suffix = [str(i) for i in range(1,1282)]

for s in suffix:
    filename = "/"+s+".jpg"
    save = folder+filename
    print(save)
    url_suffix=("0000"+s)[-4:]
    url = "https://ourartnet.com/Siku_03/0840/0840_146_004/images/"+url_suffix+"_jpg.jpg"
    print(url)
    with open(save,"wb") as handle:
        response = requests.get(url).content
        handle.write(response)
