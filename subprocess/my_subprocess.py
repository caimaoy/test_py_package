# -*- coding: utf-8 -*-

import subprocess

def call(args, wait = True):
    p = subprocess.Popen(args,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         )
    if wait:
        retCode = p.wait()
        stdout = p.stdout.read()
        stderr = p.stderr.read()

        print retCode
        print stdout

    return

if __name__ == "__main__":
    args = "cmd /C cmd"
    call(args)

