import os
#父进程
ret = os.fork()
if ret == 0:
    #子进程
    print("---1---")
else:
    #父进程
    print("---2---")
    
    ret = os.fork()
    if ret == 0:
        #二儿子
        print("---11---")
    else:
        #父进程
        print("---22---")
