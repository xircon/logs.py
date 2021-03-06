from os.path import expanduser

"""
This script prints out some errors from log files (Xorg.0.log, Xorg.1.log, pacman.log and journalctl.txt
It is intended for Linux OS (Arch based: Manjaro) For other Linux versions comment out function: read_pacman()
Before you run the script, in terminal from your home run: journalctl -b > journalctl.txt to pipe binary log to txt file
(journalctl -b > /path/to/your/home/journalctl.txt)
"""

home = expanduser("~")


def read_xorg0():
    """from Xorg.0.log print lines that contain words: failed, error, (WW)"""
    try:
        with open('/var/log/Xorg.0.log', 'r') as f:
            print('==============')
            print('| Xorg.0.log |')
            print('==============')
            for line in f:
                if 'failed' in line or 'error' in line or '(WW)' in line:
                    print(line, end='')
        print()
    except:
        print('Missing file: Xorg.0.log')


def read_xorg1():
    """from Xorg.1.log print lines that contain words: failed, error, (WW)"""
    try:
        with open('/var/log/Xorg.1.log', 'r') as f:
            print('==============')
            print('| Xorg.1.log |')
            print('==============')
            for line in f:
                if 'failed' in line or 'error' in line or '(WW)' in line:
                    print(line, end='')
        print()
    except:
        print('Missing file: Xorg.1.log')


def read_pacman():
    """from pacman.log print lines that contain words: pacsave, pacnew, pacorig, warning"""
    try:
        with open('/var/log/pacman.log', 'r') as f:
            print('==============')
            print('| pacman.log |')
            print('==============')
            for line in f:
                if 'pacsave' in line or 'pacnew' in line or 'pacorig' in line or 'warning' in line:
                    print(line, end='')
        print()
    except:
        print('Missing file: pacman.log   This is not Arch based distribution?')


def read_journalctl():
    """from journalctl.txt print lines that contain: emergency, alert, critical & failed; 0: emerg, 1: alert 2: crit"""
    try:
        with open(home + '/journalctl.txt', 'r') as f:
            print('==============')
            print('| journalctl |')
            print('==============')
            key_word = ['emergency', 'Emergency', 'EMERGENCY', 'alert', 'Alert', 'ALERT', 'critical', 'Critical',
                        'CRITICAL', 'failed']
            for line in f:
                for word in key_word:
                    if word in line:
                        print(line, end='')
    except:
        print('Missing file: journalctl.txt    Did you run (terminal): journalctl > journalctl.txt ?')

read_xorg0()
read_xorg1()
read_pacman()
read_journalctl()
