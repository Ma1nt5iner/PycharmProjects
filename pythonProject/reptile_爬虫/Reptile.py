import os
import time
from threading import Thread

import requests
from lxml import etree

if "image" not in os.listdir():
    os.mkdir("image")
    print("[+] images文件夹不存在, 已创建.")
else:
    print("[+] images文件夹已经存在.")


def getHTMLResponse(url):
    return requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.114 Safari/537.36"})


def saveImage(url):
    # 得到一个url
    response = getHTMLResponse(url).text
    img_node = etree.HTML(response)
    image = img_node.xpath('//img[@class="main-content"]/@src')[0]
    image_source = getHTMLResponse(image).content
    image_name = image.split('//')[-1].split('/')[-1]

    # 保存图片并命名
    # fileHander = open(f"image/{image_name}", "wb")
    # fileHander.write(image_source)
    # print(f"[+] 保存{image_name}成功")
    # fileHander.close()

    with open(f"image/{image_name}", "wb") as fp:
        fp.write(image_source)
        print(f"[+] 保存{image_name}成功")


Response = getHTMLResponse('https://wall.alphacoderscom/by_sub_category.php?id=279558&name=Darling+in+the+FranXX+%E5'
                           '%A3%81%E7%BA%B8&lang=Chinese&page=2').text

node = etree.HTML(Response)

url_list: list = []

xpath1 = '//div[@class="center"]/div[@class="thumb-container-big "]'
xpath2 = './div[1]/div[1]/a/@href'
tree = node.xpath(xpath1)
for i in tree:
    inner_url = i.xpath(xpath2)
    url_list.extend(inner_url)

if __name__ == '__main__':
    for f_url in url_list:
        url = "https://wall.alphacoders.com/" + f_url
        t = Thread(target=saveImage, args=(url,))
        t.start()
        time.sleep(2)
    t.join()
