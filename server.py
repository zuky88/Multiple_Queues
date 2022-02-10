#!/usr/bin/env python3

import threading
import queue
import datetime

class QUE():
    def __init__(self, q:queue.Queue) -> None:
        self.q = q
    def Put(self, msg):
        self.q.put(msg)
    def Get(self):
        return self.q.get()
    def TaskDone(self):
        self.q.task_done()

qA = QUE(queue.Queue())
qB = QUE(queue.Queue())

def thread_start():
    t = threading.Thread(target = serverMain, args = (qA,qB,))
    t.setDaemon(True)
    t.start()


def serverMain(qA:QUE, qB:QUE):
    msg = [0,0]
    while True:
        msg[0] = qA.Get()
        msg[1] = qB.Get()
        now = datetime.datetime.now()
        print('[server]get:{0}, {1}'.format(msg, now))
        qA.TaskDone()
        qB.TaskDone()


def msg_send_A(msg):
    qA.Put(msg)

def msg_send_B(msg):
    qB.Put(msg)
