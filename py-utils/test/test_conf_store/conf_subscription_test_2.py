# class Singleton:
#     __instance = None
#
#     @staticmethod
#     def getInstance():
#         """ Static access method. """
#         if Singleton.__instance == None:
#             Singleton()
#         return Singleton.__instance
#
#     def __init__(self):
#         """ Virtually private constructor. """
#         if Singleton.__instance != None:
#             raise Exception("This class is a singleton!")
#         else:
#             Singleton.__instance = self
#
#
# # s = Singleton()
# # print(s)
#
# s = Singleton.getInstance()
# print(s)
#
# s = Singleton.getInstance()
# print(s)

# from cortx.utils.process import SimpleProcess
#
# handler = SimpleProcess("ps -ef | grep zookeeper.properties | grep -v grep | wc -l")
# stdout, stderr, retcode = handler.run()

import subprocess

# ps = subprocess.run(['ps', '-ef'], check=True, capture_output=True)
# ps = subprocess.Popen(('ps', '-ef'), stdout=subprocess.PIPE)
# output = subprocess.check_output(('grep', 'zookeeper.properties'), stdin=ps.stdout)
# print(output)

# cmd = "ps -ef|grep 'zookeeper.properties|grep'"
# cmd_to_execute = "ps -ef | grep 'zookeeper.properties' | grep -v grep | wc -l"

# from cortx.utils.process import SimpleProcess
#
# cmd = "pip3 freeze"
# cmd_proc = SimpleProcess(cmd)
# stdout, stderr, retcode = cmd_proc.run()
# result = stdout.decode("utf-8") if retcode == 0 else stderr.decode("utf-8")

from subprocess import Popen, PIPE
cmd = "ps -ef | grep zookeeper.properties | grep -v grep | wc -l"
# list_cmds = [x.split() for x in cmd.split(' | ')]

list_cmds = [x.split() for x in cmd.split(' | ')]
try:
    list_cmds = [x.split() for x in cmd.split(' | ')]
    for i in range(len(list_cmds)):
        if i == 0:
            ps = Popen(list_cmds[0], stdout=PIPE)
        else:
            ps = Popen(list_cmds[i], stdin=ps.stdout, stdout=PIPE, stderr=PIPE)
    output = ps.communicate()
    print(output)
# self._output = output[0]
# self._err = output[1]
# self._returncode = ps.returncode
except Exception as err:
    print(err)
# self._err = "SubProcess Error: " + str(err)
# self._output = ""
# self._returncode = -1
# print(output1.stdout.read(), output1.stderr.read(), output1.returncode)

# from cortx.utils.process import SimpleProcess
# cmd = "ls -l | wc -l"
# import shlex
# li = shlex.split(cmd)
# print(li)
# TO DO: Use paramiko for ssh.
# cmd_proc = SimpleProcess(cmd)
# run_result = cmd_proc.run()
# print(run_result)
