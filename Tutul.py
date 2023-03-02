import os, platform, time, sys
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)
xoss('\033[0;93m [>] Checking Updates......')
time.sleep(0.10)
import Op
Op.main()
xoss('')
 
