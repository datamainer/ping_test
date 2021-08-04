import re
import subprocess
from time import sleep


def output_log():
    sorted_ms = []
    while sorted_ms == []:
        subprocess.run(['./ping_in_terminal.sh'])

        log_ping = open('log.txt', 'r')
        log = log_ping.read()
        log_ping.close()

        pattern_ms = r'(time=(.+))'

        result_ms = re.findall(pattern_ms, log)

        for ms in result_ms:
            sorted_ms.append(ms[1])

        if sorted_ms == []:
            sleep(10)

    str_value_ms = ' \n📡 >> '.join(sorted_ms)
    return str_value_ms


