#!/usr/bin/env python3
from datetime import datetime as dt

now = dt.now()

print('Starting X Color eta {}'.format(now))
from Color_Detector_Main import banners, banner

try:
    banners(banner)
    from Color_Detector import get_colors, get_image, RGB2HEX
except KeyboardInterrupt as Ke:
    print('\n Error the program was interrupted')
    
    def close():
        import sys
        waiter = 'Shutting down ' + '#' * 20 + '\n'
        for s in waiter:
            sys.stdout.write(s)
            sys.stdout.flush()
            import time
            time.sleep(0.2)
    print('please wait')
    close()
    print('Died {}'.format(now))
