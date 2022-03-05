import platform
import os
import sys

print("===================[Process IDs]======================")
print("Process id: ", os.getpid())
print("Parent Process id: ", os.getppid())
print("===================[Platform Info]======================")
print("Machine network name: ", platform.node())
print("Python version: ", platform.python_version())
print('System: ', platform.system())
print("Machine Type:", platform.machine())
print("Processor type: ", platform.processor())
print("OS release: ", platform.release())
print("===================[System Info]======================")
print("Python module lookup path: ", sys.path)
print("Command to run python: ", sys.argv)
print("USERNAME environment var: ", os.environ["USERNAME"])


