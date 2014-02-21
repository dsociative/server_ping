# -*- coding: utf8 -*-
import socket
import argparse
import timeit

from socket_server.util.sender import Sender


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int, default=10555)
parser.add_argument('-H', '--hostname', type=str, default='')


def send():
    args = parser.parse_args()
    sender = Sender(args.hostname, args.port)
    sender.connect()
    sender.send({'command': 'server.stats'})
    sender.recv()


def measure():
    try:
        return timeit.timeit(
            "send()",
            setup="from server_ping.ping import send",
            number=1
        )
    except socket.error:
        return -1


def main():
    print measure()
