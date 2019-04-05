#import os
#os.system('ls sdhndfxymjnxfs.NOEXISTE')
#os.system('echo $?')  # mostra 0 en lloc d'un altre nombre com hauria de mostrar al fallar la comanda 'ls' anterior.
import os

def run_easy(cmd):
    """ runs a command and returns the standard output and the standard error """
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    try:
        out = stdout.decode('utf8')
        err = stderr.decode('utf8')
    except UnicodeDecodeError as e:
        logging.warning("run_easy(cmd:%s): it wasn't possible to decode as UTF8 on command output"%cmd)
        out = stdout.decode("utf8", "replace")
        err = stderr.decode("utf8", "replace")
    finally:
        process.stdout.close()
        process.stderr.close()
    logging.info("testutils.run_easy()")
    logging.info("\tcmd:%s"%cmd)
    logging.info("\tstdout:%s"%shorten_message(out, 150))
    logging.info("\tstderr:%s"%err)
    return out, err

def run_background(cmd):
    """ runs a command in backgroundi
        No output is generated. In case of error it silently fails
    """
    logging.info("utiltests.run_background(cmd: %s)"%cmd)
    pid = os.fork()
    if pid == 0:
        run_easy(cmd)
    logging.info("utiltests.run_background(cmd: %s) launched"%cmd)

def command_runs_without_error(cmd):
    """ runs the command and returns True if there's no error in its execution """
    _, err = run_easy(cmd)
    return len(err) == 0

##
