#!/usr/bin/env python



import time

MACHINE_NAME = 'Extrusora 150-1'
WORK_ORDER   = '' 
STATUS       = 'STOPED' 



while True:
    time.sleep(5)
    print ( MACHINE_NAME, "WorkOrder:",WORK_ORDER, 'Status:', STATUS  )

