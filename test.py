from subprocess import Popen

proceso = Popen(['ls'])
proceso.wait()

print(proceso)