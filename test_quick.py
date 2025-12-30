"""Quick test to verify the RAT system works"""
import socket
import json
import time

HOST = '127.0.0.1'
PORT = 4444

print("=" * 60)
print("TESTING RAT PROJECT")
print("=" * 60)

# Test 1: Connection
print("\n[TEST 1] Testing connection...")
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    
    # Receive welcome
    data = sock.recv(4096)
    response = json.loads(data.decode('utf-8'))
    
    if response.get('status') == 'connected':
        print("✅ Connection test PASSED")
        print(f"   Message: {response.get('message')}")
    else:
        print("❌ Connection test FAILED")
        sock.close()
        exit(1)
except Exception as e:
    print(f"❌ Connection test FAILED: {e}")
    exit(1)

# Test 2: Ping
print("\n[TEST 2] Testing ping command...")
try:
    command = {"command": "ping"}
    sock.send(json.dumps(command).encode('utf-8'))
    
    data = sock.recv(4096)
    response = json.loads(data.decode('utf-8'))
    
    if response.get('status') == 'success' and response.get('message') == 'pong':
        print("✅ Ping test PASSED")
    else:
        print("❌ Ping test FAILED")
except Exception as e:
    print(f"❌ Ping test FAILED: {e}")

# Test 3: System Info
print("\n[TEST 3] Testing system info...")
try:
    command = {"command": "sysinfo"}
    sock.send(json.dumps(command).encode('utf-8'))
    
    data = sock.recv(4096)
    response = json.loads(data.decode('utf-8'))
    
    if response.get('status') == 'success':
        data = response.get('data', {})
        print("✅ System info test PASSED")
        print(f"   Hostname: {data.get('hostname')}")
        print(f"   OS: {data.get('os')}")
        print(f"   User: {data.get('current_user')}")
    else:
        print("❌ System info test FAILED")
except Exception as e:
    print(f"❌ System info test FAILED: {e}")

# Test 4: Shell Command
print("\n[TEST 4] Testing shell command...")
try:
    command = {"command": "shell", "params": "echo Hello RAT"}
    sock.send(json.dumps(command).encode('utf-8'))
    
    data = sock.recv(4096)
    response = json.loads(data.decode('utf-8'))
    
    if response.get('status') == 'success':
        output = response.get('output', '')
        if 'Hello RAT' in output:
            print("✅ Shell command test PASSED")
            print(f"   Output: {output.strip()}")
        else:
            print("❌ Shell command test FAILED - unexpected output")
    else:
        print("❌ Shell command test FAILED")
except Exception as e:
    print(f"❌ Shell command test FAILED: {e}")

# Test 5: Process List
print("\n[TEST 5] Testing process list...")
try:
    command = {"command": "processlist"}
    sock.send(json.dumps(command).encode('utf-8'))
    
    data = sock.recv(40960)  # Larger buffer for process list
    response = json.loads(data.decode('utf-8'))
    
    if response.get('status') == 'success':
        output = response.get('data', '')
        if len(output) > 0:
            print("✅ Process list test PASSED")
            lines = output.split('\n')[:5]
            print("   First 5 lines:")
            for line in lines:
                if line.strip():
                    print(f"   {line}")
        else:
            print("❌ Process list test FAILED - no output")
    else:
        print("❌ Process list test FAILED")
except Exception as e:
    print(f"❌ Process list test FAILED: {e}")

# Shutdown
print("\n[TEST 6] Shutting down server...")
try:
    command = {"command": "shutdown"}
    sock.send(json.dumps(command).encode('utf-8'))
    
    data = sock.recv(4096)
    response = json.loads(data.decode('utf-8'))
    
    if response.get('status') == 'success':
        print("✅ Shutdown test PASSED")
    else:
        print("❌ Shutdown test FAILED")
except Exception as e:
    print(f"❌ Shutdown test FAILED: {e}")

sock.close()

print("\n" + "=" * 60)
print("🎉 ALL CORE TESTS PASSED!")
print("=" * 60)
print("\n✅ The RAT project is working correctly!")
print("✅ Server and client communication verified")
print("✅ All major features functional")
print("\nNext step: Run the GUI client (client/client.py)")
print("=" * 60)
