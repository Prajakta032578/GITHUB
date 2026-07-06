import platform
import subprocess


def get_system_uptime():
    """Return the system uptime."""
    try:
        system = platform.system()

        if system == "Windows":
            result = subprocess.run(
                ["net", "stats", "workstation"],
                capture_output=True,
                text=True,
                check=True
            )

            for line in result.stdout.splitlines():
                if "Statistics since" in line:
                    return line.strip()

            return "Unable to determine system uptime."

        elif system in ("Linux", "Darwin"):
            result = subprocess.run(
                ["uptime"],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()

        else:
            return f"Unsupported operating system: {system}"

    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e}"

    except Exception as e:
        return f"Unexpected error: {e}"


def main():
    print("System Uptime")
    print("-" * 30)
    print(get_system_uptime())


if __name__ == "__main__":
    main()
