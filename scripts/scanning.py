import os

def scan_target(target):
    print(f"Scanning {target} for open ports...")
    os.system(f"nmap {target}")

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    scan_target(target_ip)
