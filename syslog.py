#!/usr/bin/env python3

import re
import sys

with open(sys.argv[1]) as logs:
    pattern = r"^([a-zA-Z0-9: ]+) rsyslogd: ([0-9]+)"
    for log in logs.readlines():
#        print("L: ",log)
        res = re.search(pattern, log.strip())
        #print("Res: ",res);
        if res is not None:
            print("Time: {}".format(res.group(1)));
            print("ID changed to {}".format(res.group(2)))
