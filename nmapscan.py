import subprocess
import sys
import argparse

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
    parser = argparse.ArgumentParser(description="Nmap Scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("port_range", help="Port range to scan (e.g., 1-1000)")
    parser.add_argument("-o", "--os_detection", action="store_true", help="Enable OS detection")
    parser.add_argument("-v", "--version_detection", action="store_true", help="Enable version detection")
    args = parser.parse_args()

    scan_network(args.target, args.port_range, args.os_detection, args.version_detection)
