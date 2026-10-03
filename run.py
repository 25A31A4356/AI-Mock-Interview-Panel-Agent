import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        sys.stdout.write(f"[{time.strftime('%H:%M:%S')}] {format % args}\n")
        sys.stdout.flush()

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def open_browser():
    time.sleep(0.8)
    url = f"http://127.0.0.1:{PORT}"
    print(f"[*] Auto-launching browser: {url}")
    webbrowser.open(url)

def main():
    os.chdir(DIRECTORY)
    server_address = ("127.0.0.1", PORT)
    
    try:
        with ReusableTCPServer(server_address, QuietHandler) as httpd:
            print("=" * 64)
            print("  AI Mock Interview Panel Agent")
            print("  Enterprise HRTech Simulation Studio")
            print(f"  AI Interview Simulator active at http://127.0.0.1:{PORT}")
            print(f"  Serving Directory: {DIRECTORY}")
            print("  Press Ctrl+C to terminate.")
            print("=" * 64)
            
            threading.Thread(target=open_browser, daemon=True).start()
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Server shutdown gracefully.")
    except Exception as e:
        print(f"[!] Server error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
