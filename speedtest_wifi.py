import sys
import speedtest
import numpy as np
import matplotlib.pyplot as plt
import time
import csv
import datetime

def get_speed_test():
    severs = []
    stest = speedtest.Speedtest()
    stest.get_servers(severs)
    return stest

def command_line_runner():
    stest = get_speed_test()
    down_result = stest.download() / 1024 /1024
    up_result = stest.upload() / 1024 / 1024
    result = [down_result, up_result]

    return down_result, up_result


def main():
    t = [0]
    arrDown = [0]
    arrUp = [0]

    count_t = 0;
    
    with open('./log.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        dt_now = datetime.datetime.now()
        writer.writerow([str(dt_now)])
        print(dt_now)
        f.close()

    while True:
        start = time.time()

        plt.xlabel('t [s]')
        plt.ylabel('Speed [Mbps]')
        plt.grid(color='r', linestyle='dotted', linewidth=1)
        plt.plot(t, arrDown,marker="+", label='Downloads [Mbps]')
        plt.plot(t, arrUp,marker=".", label = 'Uploads [Mbps]')
        plt.legend()
        plt.draw()
        plt.pause(1)
        plt.clf()

        down, up = command_line_runner()

        if len(t) >= 10:
            del t[0]
            del arrDown[0]
            del arrUp[0]

        elapsed_time = time.time() - start

        with open('./log.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([str(down), str(up), str(elapsed_time)])
            f.close()

        print('Downloads:' + str(down) + ' Mbps\n' )
        print('Uploads:' + str(up) + ' Mbps\n' )
        print('計測時間:' + str(elapsed_time) + ' Second\n')
        print('ーーーーーーーーーーーーーーー\n')

        
        count_t += elapsed_time
        t.append(count_t)
        arrDown.append(down)
        arrUp.append(up)

main()
