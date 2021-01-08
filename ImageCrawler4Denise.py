import sys
import requests
import subprocess

if 'darwin' in sys.platform:
    print('Running \'caffeinate\' on MacOSX to prevent the system from sleeping')
    subprocess.Popen('caffeinate')

folder = "/Users/hliu/Desktop/imgs"
suffix = [str(i) for i in range(1,1953)]

for s in suffix:
    filename = "/"+s+".jpg"
    save = folder+filename
    print(save)
    url_suffix=("0000"+s)[-4:]
    url = "http://gmzm.org/bbooks/%E5%8F%A4%E4%BB%A3%E5%AD%97%E7%94%BB/%E9%92%A6%E5%AE%9A%E8%A5%BF%E6%B8%85%E5%8F%A4%E9%89%B4/%E9%92%A6%E5%AE%9A%E8%A5%BF%E6%B8%85%E5%8F%A4%E9%89%B4.40%E5%8D%B7.%E9%99%84%E9%92%B1%E5%BD%95.16%E5%8D%B7.%E6%B8%85%E6%A2%81%E8%AF%97%E6%AD%A3.%E8%92%8B%E6%BA%A5%E7%AD%89.%E6%B8%85%E5%85%89%E7%BB%AA14%E5%B9%B4%E8%BF%88%E5%AE%8B%E4%B9%A6%E9%A6%86%E9%93%9C%E7%89%88%E5%8D%B0%E6%9C%AC_%E9%A1%B5%E9%9D%A2_"+url_suffix+".jpg"

    with open(save,"wb") as handle:
        response = requests.get(url).content
        handle.write(response)
