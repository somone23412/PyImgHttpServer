import os
import time
import datetime
import argparse
import otherapp as oa


def protect_start(process_num=10):
    while(True):
        time.sleep(2)

        r = os.popen('pgrep ' + oa.other_app_conf['appName'])
        pgrep_res = r.read()
        r.close()
        pids = pgrep_res.split("\n")
        if (len(pids) - 1) < process_num:
            record_file = 'crash_log.txt'

            nvidia_smi = os.popen('nvidia-smi')
            nvidia_smi_info = nvidia_smi.read()
            nvidia_smi.close()

            record = open(record_file, 'a')
            record.write('%s %s\n' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), nvidia_smi_info))
            record.close()

            oa.shutdown()
            oa.start(windowless=True)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Protect process')
    parser.add_argument('--process_num', type=int, default=10, metavar='N',
                        help='number of process in running (default:10)')
    args = parser.parse_args()
    time.sleep(2)
    protect_start(args.process_num)
    oa.shutdown()

