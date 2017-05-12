#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-5-12 下午1:42
# @Author         : Tom.Lee
# @Description    : 
# @File           : bin.py
# @Product        : PyCharm

"""
setup commands:
    simple demo for python setup.

Usage:
    setupapp -l
    setupapp -h | --help
    setupapp -v | --version
    setupapp -m
    setupapp -P <port>
    setupapp -H <ip>
    setupapp [-H <ip>] [-P <port>]

Arguments:
    ip    output ip
    port  output port

Options:
    -h --help        帮助
    -v --version     版本.
    -l               列表.
    -m               say hello
"""

from docopt import docopt


class SetupApp(object):
    """
    test class
    """

    def __init__(self, **kwargs):
        self.args = kwargs

    def command(self):
        if self.args.get('-l'):
            for i, var in enumerate(range(1, 6)):
                print '\t' * i, var
        if self.args.get('-H') and self.args.get('-P'):
            print "[IP:PORT] %s:%s" % (self.args.get('<ip>'), self.args.get('<port>'))

        if self.args.get('-H'):
            print "IP : ", self.args.get('<ip>')

        if self.args.get('-P'):
            print "PORT : ", self.args.get('<port>')

        if self.args.get('-m'):
            print '** Say Hello **'

        if True not in self.args.values():
            print __doc__


def run():
    """ 入口方法 """
    args = docopt(__doc__, version='1.0.0')
    SetupApp(**args).command()
