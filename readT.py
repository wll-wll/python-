import qrcode 
import image
import os
def reads() :
    route=input('请输入文件地址：')
    file = open(route,encoding='utf-8')
    content = file.read()
    imga = qrcode.make(content)
    imga.save("dfg123.jpg")
