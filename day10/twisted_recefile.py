#!/usr/bin/env python
# -*- coding:utf-8 -*-
# This is the Twisted Get Poetry Now! client, version 3.0.

# NOTE: This should not be used as the basis for production code.

import optparse

from twisted.internet.protocol import Protocol, ClientFactory


def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

This is the Get Poetry Now! client, Twisted version 3.0
Run it like this:

  python get-poetry-1.py port1 port2 port3 ...
"""

    parser = optparse.OptionParser(usage)
    _, addresses = parser.parse_args()
    print('==addr:',_,addresses)
    if not addresses:
        print parser.format_help()
        parser.exit()

    def parse_address(addr):
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)
        if not port.isdigit():
            parser.error('Ports must be integers.')
        return host, int(port)
    #return  parse_address(addresses)
    return map(parse_address, addresses)

class PoetryProtocol(Protocol):

    poem = ''
    def dataReceived(self, data):
        self.poem += data
        #self.factory = PoetryClientFactory
        print('[%s] recv:[%s]' %(self.transport.getPeer(),len(self.poem)))
    def connectionLost(self, reason):
        self.poemReceived(self.poem)

    def poemReceived(self, poem):
        self.factory.poem_finished(poem)


class PoetryClientFactory(ClientFactory):
    protocol = PoetryProtocol #handle method
    def __init__(self, callback):
        self.callback = callback
    def poem_finished(self, poem):
        self.callback(poem)
        #self.get_poem(poem)


def get_poetry(host, port, callback):
    """
    Download a poem from the given host and port and invoke
      callback(poem)
    when the poem is complete.
    """
    from twisted.internet import reactor
    factory = PoetryClientFactory(callback)
    reactor.connectTCP(host, port, factory)


def poetry_main():
    addresses = parse_args() #((172.0.0.1,9000),(...))
    from twisted.internet import reactor
    poems = []

    def got_poem(poem):
        poems.append(poem)
        if len(poems) == len(addresses):
            reactor.stop()

    for address in addresses:
        host, port = address
        get_poetry(host, port, got_poem)
    reactor.run()

    print("main loop done...")
    #for poem in poems:
    #    Eprint poem

if __name__ == '__main__':
    poetry_main()