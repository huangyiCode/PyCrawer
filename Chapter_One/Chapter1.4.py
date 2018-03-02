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
