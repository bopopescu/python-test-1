#!/usr/bin/python
#coding=utf-8
'''
从程序输出中不难发现，我们仅执行了一次程序，却同时运行了if判断的elif和else分之的内容，这就是fork的作用；
在rpid=os.fork()这条语句执行之前，程序只有一个进程在执行，此时程序已经初始化了两个变量，当执行fork语句后，程序创建了一个子进程，并且将这两个变量的状态传递给了这个子进程，子进程从if开始执行，直到执行完程序剩下的代码；
rpid=os.fork()之后，父进程也会继续执行，也就意味着，两个进程同时从if的位置开始执行剩下的代码，互不干扰；
os.getpid()能够获取当前进程的PID，os.getppid()能够获取当前进程的父进程PID；
那么，我们是如何知到rpid为0，就是子进程的呢？这是因为fork有三种不同的返回值：
1）在父进程中，fork返回新创建子进程的进程ID；
2）在子进程中，fork返回0；
3）如果出现错误，fork返回一个负值；
这样，我们就可以通过os.fork()这条语句执行后的返回值，来判断进程是父进程还是子进程，在子进程中，返回值是0，在父进程中，返回值是刚才新建的子进程的PID，如果创建进程失败，就会返回一个负值（通常如果系统限制了进程创建，或内存不足，或达到了系统进程上限，就会创建失败并返回一个负值）；
在创建了新的进程后，这两个进程（父进程与子进程）执行没有固定的先后顺序，哪个进程先执行要看系统的进程调度策略；
其次，fork后，fork前已经初始化的那些变量会被复制成两份，两个进程中x的值都是0，并且两个进程的变量是独立的，存在不同的地址中，这就是为什么最后打印出来的x值是1的原因（每个进程的if流程都只执行了一次x+=1）；
'''
import os
x=0
s="www.qingsword.com"
rpid=os.fork()
if rpid<0:
    pirnt("fork调用失败")
elif rpid==0:
    print("我是子进程(%s),我是父进程(%s) "%(os.getpid(),os.getppid()))
    x=x+1
else:
    print("我是父进程（%s），我的子进程是（%s）"%(os.getpid(),rpid))
    x=x+1
print(s,x)
