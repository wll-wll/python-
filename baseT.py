import base64
def decode_base64():  # 解密base64
    data = input('请输入要解密的字符：')
    missing_padding = 4- len(data) %4
    if missing_padding:
        data += '=' * missing_padding
    print('解密结果如下：')
    print(base64.b64decode(data))
def encode_base64(): # 加密base64
    data = input('请输入要加密的字符：')   # data= "{'name':'kkk','age':22}"
    print('加密结果如下：')
    print(base64.b64encode(data.encode()))  # data必须是bytes类型，如果是字符串，则通过encode()转换
if __name__ == '__main__':
    decode_base64()
    print (base64.b64encode(b'asdasd'))
    print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
    #coding:utf-8'''