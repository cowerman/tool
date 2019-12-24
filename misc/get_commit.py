#!/usr/bin/env python3

import os
import sys
import subprocess


def dump_commit(commit, i):

    cmd = 'wget {}.patch -O 00{}.patch'.format(commit, i)
    res = subprocess.call(cmd, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, close_fds=True)
    print("Get {} > 00{}.patch".format(commit, i))
    

def main(args):

    arg_len = len(args)
    if arg_len != 1:
        # get only one commit with parameter
        dump_commit(args[1], 1)
        return

    with open('commits', 'rt') as commits:
        commit_lines = commits.readlines()
        i = 0
        for commit_line in commit_lines:
            i += 1
            commit = commit_line.strip()
            dump_commit(commit, i)


if __name__ == '__main__':
    ARGS = sys.argv
    main(ARGS)

