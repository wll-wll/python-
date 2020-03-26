import base64
def encode_base64(): # 加密base64
    data = input('请输入要加密的字符：')   # data= "{'name':'kkk','age':22}"
    print('加密结果如下：')
    print(base64.b64encode(data.encode()))  # data必须是bytes类型，如果是字符串，则通过encode()转换
def decode_base64():  # 解密base64
    a=1
    data = input('请输入要解密的字符：')
    missing_padding = 4- len(data) %4
    if missing_padding:
        data += '=' * missing_padding
    print('解密结果如下：')
    datatemp=base64.b64decode(data)
    try:
        str_base64 = str(datatemp, 'utf-8')
    except :
         print('输入有误!')
         a=a+1
    if(a==1) :
        str_base64 = str(datatemp, 'utf-8')
        print(str_base64)
if __name__ == '__main__':
    encode_base64()
    decode_base64()
