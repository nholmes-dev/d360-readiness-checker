import socket
import urllib.request
from datetime import datetime


def check_dns(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return True, ip_address
    except socket.gaierror:
        return False, None


def check_https(url):
    try:
        response = urllib.request.urlopen(url, timeout=10)
        return True, response.status
    except Exception as error:
        return False, str(error)


def run_checks(hostname, url):
    print("D360 Environment Readiness Checker")
    print("----------------------------------")
    print(f"Check time: {datetime.now()}")
    print()

    dns_ok, ip_address = check_dns(hostname)

    if dns_ok:
        print(f"[PASS] DNS resolved: {hostname} -> {ip_address}")
    else:
        print(f"[FAIL] DNS could not resolve: {hostname}")

    https_ok, result = check_https(url)

    if https_ok:
        print(f"[PASS] HTTPS response received: HTTP {result}")
    else:
        print(f"[FAIL] HTTPS check failed: {result}")


if __name__ == "__main__":
    hostname = "example.com"
    url = "https://example.com"

    run_checks(hostname, url)
