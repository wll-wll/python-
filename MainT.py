from baseT import encode_base64,decode_base64
from dictT import converts
from readT import reads
a='!q'        #退出变量1赋值
while a!='q':         #判断是否退出
    b='!q'
    list=['1 base','2 dictconvert','3 readtxt'] #初始化退出变量2和列表
    for index in list:        #首先显示菜单
        print (index)
    print ('退出q')        #补上的退出功能
    temp1=input('请选择你想使用的功能：')
    if temp1 in ('1','base') :        #判断键入的值在字典中
        list=['encode','decode']      #新的菜单
        while b!='q' :      
            for i,index in enumerate(list): 
                print (i+1,index)         #再次显示菜单
            print ('退出q')        #补上的退出功能
            temp2=input('请选择你想使用的功能：') 
            if temp2 in ('1','encode') : 
                encode_base64()
                temp3=input('enter any key to continue：')
            elif temp2 in ('2','decode') :
                decode_base64()
                temp3=input('enter any key to continue：')
            elif temp2=='q' :
                b='q'
            else :
                print('输入有误，请重新输入')
    elif temp1 in ('2','dictconvert') :     
        converts()
        temp3=input('enter any key to continue：')
    elif temp1 in ('3','readtxt') :    
        reads() 
        temp3=input('enter any key to continue：')
    elif temp1=='q' :           #判断键入的是不是退出字符
        a='q'            #赋值，终止循环
    else:
        print('输入有误，请重新输入')    
else:
   print ('已退出')