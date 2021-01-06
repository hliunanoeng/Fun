import sys
import requests
import subprocess

if 'darwin' in sys.platform:
    print('Running \'caffeinate\' on MacOSX to prevent the system from sleeping')
    subprocess.Popen('caffeinate')

folder = "/Users/hliu/Desktop/imgs"
suffix = [str(i) for i in range(1,150)]

for s in suffix:
    filename = "/"+s+".jpg"
    save = folder+filename
    url_suffix=("000"+s)[-3:]
    url = "http://b.gmzm.org/2018/%E6%96%87%E5%8F%B2%E7%A4%BE%E7%A7%91/%E8%A5%BF%E6%B8%85%E5%8F%A4%E9%89%B4/%E9%92%B1%E5%BD%95/%E8%A5%BF%E6%B8%85%E5%8F%A4%E9%89%B4.%E9%92%B1%E5%BD%95.%E5%8D%81%E5%85%AD%E5%8D%B7.%E6%B8%85%E6%A2%81%E8%AF%97%E6%AD%A3%E7%AD%89%E7%BC%96.%E6%B8%85%E4%B9%BE%E9%9A%86%E6%97%B6%E6%9C%9F%E5%86%85%E5%BA%9C%E5%88%8A%E6%9C%AC_%E9%A1%B5%E9%9D%A2_"+url_suffix+".jpg"

    with open(save,"wb") as handle:
        response = requests.get(url).content
        handle.write(response)
