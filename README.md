# Socket Basics Custom Rules Test

Test repository for validating custom opengrep/semgrep rules with [Socket Basics](https://github.com/SocketDev/socket-basics).

## Structure

```
.github/workflows/socket.yml   # GHA workflow with custom rules enabled
.socket/rules/org-rules.yml    # Custom SAST rules
src/app.py                     # Sample code that triggers the rules
```

## Custom Rules

| Rule ID              | Pattern                              | What it catches              |
|----------------------|--------------------------------------|------------------------------|
| `org.no-eval`        | `eval(...)`                          | Arbitrary code execution     |
| `org.no-exec`        | `exec(...)`                          | Arbitrary code execution     |
| `org.no-shell-true`  | `subprocess.call(..., shell=True)`   | Command injection            |
| `org.no-pickle-load` | `pickle.loads(...)`                  | Unsafe deserialization       |

## Local Validation

```bash
# Validate rule syntax
semgrep --validate --config .socket/rules/

# Run rules against source
semgrep --config .socket/rules/ src/
```
