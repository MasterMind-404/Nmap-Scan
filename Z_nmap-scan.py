
import os
import subprocess
import argparse
import ipaddress

def scan_network(target, port_range, os_detection, version_detection):
    """
    Scan the network using Nmap
    """
    nmap_command = ["nmap"]

    # Add target IP or network
    nmap_command.append(target)

    # Add port range
    if port_range:
        nmap_command.append("-p")
        nmap_command.append(port_range)

    # Add OS detection
    if os_detection:
        nmap_command.append("-O")

    # Add version detection
    if version_detection:
        nmap_command.append("-sV")

    # Run Nmap command
    output = subprocess.check_output(nmap_command)
    print(output.decode("utf-8"))

def validate_ip_address(target):
    """
    Validate the target IP address or network
    """
    try:
        ipaddress.ip_network(target, strict=False)
        return True
    except ValueError:
        return False

def main():
    parser = argparse.ArgumentParser(description="Nmap Scanner")
    parser.add_argument("target", help="Target IP address or network")
    parser.add_argument("-p", "--port_range", help="Port range to scan (e.g. 1-100)")
    parser.add_argument("-O", "--os_detection", action="store_true", help="Enable OS detection")
    parser.add_argument("-sV", "--version_detection", action="store_true", help="Enable version detection")
    args = parser.parse_args()

    if not validate_ip_address(args.target):
        print("Invalid target IP address or network")
        return

    scan_network(args.target, args.port_range, args.os_detection, args.version_detection)

if __name__ == "__main__":
    main()
