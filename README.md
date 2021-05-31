# Live Coder Python Module (WIP)

A basic wrapper for [snoop](https://github.com/alexmojaki/snoop).

To be used with a new Live Coder VSCode extension.

## Usage

Start by adding snoop to one of your methods.

```python
from live_coder import snoop

@snoop
def my_first_method():
  pass
```

Whenever your code is ran its snoop logs will be written to `.live_coder`.

These logs are then parsed to show live values for the code.
