
from platform import system, machine, python_version, uname


operating_system = None
cpu_architecture = None
python_vers = None
username = None
        
def get_system_info(): 
    try:
        operating_system = system()
        cpu_architecture = machine()
        python_vers = python_version()
        username = uname()
        return (operating_system, cpu_architecture, python_version)
    except:
        print("An error occurred while retrieving system information.")


def show_system_info():
    print("----- PC info -----")
    print(f"Operating System: {operating_system}")
    print(f"CPU Architecture: {cpu_architecture}")
    print(f"Python Version: {python_vers}")
    print(f"Username: {username.nodename}")
    print("-------------------")
