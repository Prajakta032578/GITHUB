# GitHub Copilot – System Uptime Script

## Objective

The objective of this assignment was to use GitHub Copilot on GitHub.com to generate a Python script that prints the system uptime, improve the generated code, and document the experience.

## Copilot Suggestion

GitHub Copilot suggested a Python script that used the `os.popen()` function to execute the `uptime` command and display the output.

## Modifications Made

I modified the generated script to improve its security, reliability, and readability by:

* Replacing `os.popen()` with `subprocess.run()`.
* Creating a separate `get_system_uptime()` function.
* Adding exception handling using `try` and `except`.
* Adding support for both Windows and Linux/macOS.
* Improving the overall structure using a `main()` function.

These changes make the script more secure and easier to maintain.

## Testing

The script was tested by running it from the terminal using Python. It successfully displayed the system uptime on the operating system.

## How to Run

1. Clone or download the repository.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command:

```bash
python copilot_test.py
```

## Repository Contents

* `copilot_test.py` – Python script to display system uptime.
* `README.md` – Documentation of the Copilot-generated code, modifications, testing, and execution steps.
