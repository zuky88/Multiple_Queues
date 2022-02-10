#!/usr/bin/env python3

import threading
import datetime
import time
import server

def clientMain():
    msg = 0
    while True:
        now = datetime.datetime.now()
        print('[clientB]send:{0}, {1}'.format(msg, now))
        server.msg_send_A(msg)
        msg += 2
        time.sleep(0.1)

def thread_start():
    t = threading.Thread(target = clientMain,args=())
    t.setDaemon(True)
    t.start()
