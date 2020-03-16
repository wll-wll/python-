import json  #导入标准库json<br>
def converts() :
    dectTs = {}
    print('请输入原字典：')
    juedge = True
    while juedge:                           #输入字典
        dectT_name = input("请输入键：")
        price = input("请输入值：")
        dectTs[dectT_name] = price
        repeat = input("是否继续输入?(y/n)")
        if repeat == 'n' or repeat =='N':
            juedge = False
    print('原字典输出如下：')
    print(dectTs)
    dectTs_json = json.dumps(dectTs,indent=4,ensure_ascii=False) #加入ASCII参数
    print('json字符串输出如下：')
    print(dectTs_json)
    print(type(dectTs_json))
    news={v: k for k, v in dectTs.items()}
    print(news)
    print(type(news))
if __name__ == '__main__':
    converts() 
