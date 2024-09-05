import platform
import subprocess

def ping(host):
    # Check the operating system to use the appropriate ping command
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Ping command with 4 packets
    command = ['ping', param, '4', host]

    # Run the ping command and check the result
    try:
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        print(output.stdout)
        print(f"\nPing to {host} successful!")
    except subprocess.CalledProcessError:
        print(f"\nUnable to ping to {host}.")

def main():
    host = input("IP or domain:  ")
    ping(host)

if __name__ == "__main__":
    main()