"""Sample application with intentional security issues for testing custom SAST rules."""

import pickle
import subprocess


def run_user_query(user_input: str) -> str:
    """Executes user-provided expression. Triggers: org.no-eval"""
    result = eval(user_input)
    return str(result)


def run_dynamic_code(code_string: str) -> None:
    """Executes dynamically generated code. Triggers: org.no-exec"""
    exec(code_string)


def run_shell_command(cmd: str) -> int:
    """Runs a shell command from user input. Triggers: org.no-shell-true"""
    return subprocess.call(cmd, shell=True)


def load_cached_object(data: bytes) -> object:
    """Deserializes untrusted data. Triggers: org.no-pickle-load"""
    return pickle.loads(data)


if __name__ == "__main__":
    print(run_user_query("2 + 2"))
    run_dynamic_code("print('hello')")
    run_shell_command("echo test")
    load_cached_object(pickle.dumps({"key": "value"}))
