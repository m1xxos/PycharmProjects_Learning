import argparse
import socket
import itertools
import string

parser = argparse.ArgumentParser()
parser.add_argument('host', help='enter hostname')
parser.add_argument('port', help='enter port number', type=int)

args = parser.parse_args()
character_set = string.ascii_lowercase + string.digits


def generate_password():
    for length in range(1, len(character_set) + 1):
        for product in itertools.product(character_set, repeat=length):
            yield ''.join(product)


with socket.socket() as client:
    client.connect((args.host, args.port))
    for password in generate_password():
        client.send(password.encode())
        response = client.recv(1024).decode()

        if response == 'Connection success!':
            print(password)
            break
