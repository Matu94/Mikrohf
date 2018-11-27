#!/usr/bin/env python3
'''Records measurments to a given file. Usage example:

$ ./record_measurments.py out.txt'''
import sys
from rplidar import RPLidar
import numpy as np


PORT_NAME = '/dev/ttyUSB0'
scan_list = []

def run(path):
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    data = []
    outfile = open('mikro10.csv', 'w')
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for scan in lidar.iter_scans():
            line = '\t'.join(str(v) for v in scan)
            outfile.write(line + '\n')
            ##data.append(np.array(scan))
            ##outfile.write(data + '\n')
    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()
    outfile.close()

if __name__ == '__main__':
    run(sys.argv[0])

