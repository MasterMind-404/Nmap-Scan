import subprocess
import sys

def scan_network(target, port_range, os_detection, version_detection):
    nmap_command = f"nmap -oN output.txt {target} -p {port_range}"
    if os_detection:
        nmap_command += " -O"
    if version_detection:
        nmap_command += " -sV"

    try:
        output = subprocess.check_output(nmap_command, shell=True)
    except KeyboardInterrupt:
        print("\nScan interrupted by user. Exiting...")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

    with open("output.txt", "r") as f:
        output = f.read()

    print(output)

if __name__ == "__main__":
    target = "192.168.1.1"  # Replace with your target IP
    port_range = "1-1000"  # Replace with your port range
    os_detection = True  # Set to True for OS detection
    version_detection = True  # Set to True for version detection

    scan_network(target, port_range, os_detection, version_detection)
