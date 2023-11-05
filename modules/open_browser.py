import subprocess
import socket
import webbrowser


# Get the IP address of the host
def get_host_ip():
    try:
        # Create a socket and connect to a remote host (e.g., Google's public DNS server)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        host_ip = s.getsockname()[0]
        s.close()
        return host_ip
    except Exception as e:
        print(f"Error getting host IP: {e}")
        return None


def open_browser():
    # Get the host IP and port
    host_ip = get_host_ip()
    port = 8888

    if host_ip:
        # Print the host IP and port
        print(f"Host IP: {host_ip}")
        print(f"Port: {port}")

        # Open a web browser with the specified IP and port
        url = f"http://{host_ip}:{port}"
        webbrowser.open(url)
    else:
        print("Failed to get host IP.")

    # You can use the subprocess module to run a command here if needed.


if __name__ == '__main__':
    print("modules/open_browser.py executed as main")