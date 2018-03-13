# coding=utf-8
# Process and Thread

# Process
#  1.Use fork(Since Unix/Linux) from os model.
#  2.Use multiprocessing

# Fork
import os

print 'current Process (%d) start ...' % (os.getpid())
pid = os.fork()
if pid < 0:
    print 'error in fork'
elif pid == 0:
    print 'I am child Process My pid is (%d) and My parent pid is (%d)' % (os.getpid(), os.getppid())

else:
    print 'I create a sub Process My pid is (%d).' % (os.getpid())

# Multiprocessing

import os

from multiprocessing import Process


def run_proc(name):
    print 'Child process %s (%s) Running...' % (name, os.getpid())


if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print 'Process will start.'
        p.start()
    p.join()
    print 'Process end.'


def call_back(count, target=None, target2=None):
    target('调用---%s' % (os.getpid()))
    target('aaa')
    target2('bbb')


def target(s):
    print('target----' + s)


def target1(s1):
    print('target2---' + s1)


call_back(1, target=target, target2=target)

# Use process pool to manager process(the pool default size is cpu numbers)

from multiprocessing import Pool
import os, random, time


def run_task(name):
    print 'Run_task %s (pid=%s) is running....' % (name, os.getpid())
    time.sleep(random.random() * 3)
    print 'Task end %s (pid=%s) is end....' % (name, os.getpid())


# if  '__name__' == '__main__':
print 'Current process %s.' % os.getpid()
p = Pool(processes=3)
for i in range(5):
    p.apply_async(run_task, args=(i,))
print 'Waiting for all subprocess done...'
p.close()
p.join()
print 'All subprocess done.'

# communication between process.We can use Queue Pipe Value+Array and others.
# Queue
#   1.Queue is a safe multithreading  put()   get(),difference thread use the same Queue to communication
from multiprocessing import Queue


# This function used to write data to the Queue
def proc_write(q, urls):
    print 'process (%s) is writing...' % (os.getpid())
    for url in urls:
        q.put(url)
        print 'Put %s to the q.' % url
        # time.sleep(random.random)


# This function used to read data from the Queue.
def proc_read(q):
    print('process (%s) is reading' % os.getpid())
    while True:
        url = q.get(True)
        print 'read url %s' % url


q = Queue()
proc_write1 = Process(target=proc_write, args=(q, ['url1', 'url2', 'url3', 'url4']))
proc_write2 = Process(target=proc_write, args=(q, ['url5', 'url6', 'url7', 'url8']))

proc_read1 = Process(target=proc_read, args=(q,))

proc_write1.start()
proc_write2.start()

proc_read1.start()

proc_write1.join()
proc_write2.join()

proc_read1.terminate()

# Pipe通信机制
import multiprocessing


def proc_send(pipe, urls):
    for url in urls:
        print 'Process(%s) send:%s"' % (os.getpid(), url)
        pipe.send(url)
        time.sleep(random.random())


def proc_recv(pipe):
    while True:
        print 'Process(%s) rev:%s' % (os.getpid(), pipe.recv())
        time.sleep(random.random())


pipe = multiprocessing.Pipe()
p1 = multiprocessing.Process(target=proc_send, args=(pipe[0], ['url_' + str(i) for i in range(10)]))
p2 = multiprocessing.Process(target=proc_recv, args=(pipe[1],))
p1.start()
p2.start()
p1.join()
p2.terminate()

array = [i for i in range(10)]
for tes in array:
    print '--------+%s' % (tes)

# multithreading的使用
# 1.use threading model to create
import threading


def thread_run(urls):
    print 'Current %s Thread is running...' % (threading.current_thread().name)
    for url in urls:
        print '%s ---->>> %s' % (threading.current_thread().name, url)
    print 'Current %s Thread is end.' % (threading.current_thread().name)


print('start----------->%s' % (threading.Thread().name))
t1 = threading.Thread(target=thread_run, args=(['u1', 'u2', 'u3', 'u4'],))
t2 = threading.Thread(target=thread_run, args=(['u1', 'u2', 'u3', 'u4'],))

t1.start()
t2.start()
t1.join()
t2.join()
print('end----------->%s' % (threading.Thread().name))


# 2.use class to extends threading.Thread
class myThread(threading.Thread):
    def __init__(self, name, urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print 'Current %s is running...' % threading.current_thread().name
        for url in self.urls:
            print '%s-------> %s' % (threading.current_thread().name, url)
            time.sleep(random.random())
        print 'Run function finish %s' % threading.current_thread().name


t1 = myThread(name='Thread_1', urls=['url_1', 'url_2', 'url_3', 'url_4', 'url_5'])
t2 = myThread(name='Thread_2', urls=['url_1', 'url_2', 'url_3', 'url_4', 'url_5'])
t1.start()
t2.start()
t1.join()
t2.join()
print '%s ended.' % threading.current_thread().name

# Use RLock
num = 9
lock = threading.RLock()


class lockThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while num > 1:
            # lock.acquire()
            num = num - 1
            print 'This num ------>%s------>%s' % (num, threading.current_thread().name)
            time.sleep(1)
            # lock.release()


threading1 = lockThread("lockThread1")
threading2 = lockThread("lockThread2")
threading1.start()
threading2.start()
threading1.join()
threading2.join()

print '----------------------------------------------------Line---------------------------------------------------------------------------'
from gevent import monkey

monkey.patch_all()
import gevent
import urllib2


def init_start(url):
    try:
        response = urllib2.urlopen(url)
        data = response.read()
        print 'The response data len %s and url is %s' % (len(data), url)
    except Exception, e:
        print e
    return 'url---->%s----->finish'%(url)


urls = ["https://www.baidu.com", "http://blog.csdn.net/baidu_31093133/article/details/51860637",
        "https://www.baidu.com"]
# init coroutines tasks
gevents = [gevent.spawn(init_start, url) for url in urls]
# start and run coroutines tasks. default is just one thread.
print 'The task len is %s------->process id id %s' % (len(gevents),os.getpid())
gevent.joinall(gevents)
print '----------------------------------------------------Line---------------------------------------------------------------------------'
# Use gevent poll to run tasks in muit thread.协程Pool对协程的并发做出了控制,只有前两个任务执行结束才会执行第三个任务
from gevent.pool import Pool
pool=Pool(2)
results=pool.map(init_start,urls)
print results

