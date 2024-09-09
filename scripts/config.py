from platform import system, machine, python_version


operating_system = None
cpu_architecture = None
python_vers = None
username = None


VERSION: str = '0.0.1'

OPERATIONS: dict = {
    ":[save-exit]": 1, 
}

AUTOCOMPLETE_PYTHON = [
    "if", "else", "for", "while", "def", "class", "return", "import",
    "print", "input", "open", "close", "read", "write", "append", "len", "range",
    "list", "tuple", "set", "dict", "bool", "int", "float", "str", "None", "type",
    "isinstance", "getattr", "setattr", "hasattr", "delattr", "dir", "id", "hex",
    "oct", "bin", "chr", "ord", "eval",
    "abs", "sum", "min", "max", "pow", "round", "complex", "divmod", "round",
    "zip", "map", "filter", "reduce", "all", "any", "sorted", "reversed", "enumerate",
    "format", "f-string", "lambda", "pass", "continue", "break", "raise", "try",
    "except", "finally", "else", "finally", "raise"
]

def get_system_info(): 
    try:
        operating_system = system()
        cpu_architecture = machine()
        python_vers = python_version()
        return (operating_system, cpu_architecture, python_vers)
    except:
        print("An error occurred while retrieving system information.")


def show_system_info():
    print("----- PC info -----")
    print(f"Operating System: {operating_system}")
    print(f"CPU Architecture: {cpu_architecture}")
    print(f"Python Version: {python_vers}")
    print(f"Username: {username.nodename}")
    print("-------------------")
