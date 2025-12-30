# 🧪 Complete Testing Guide

This guide provides **step-by-step testing instructions** for your RAT project.

---

## ⚠️ Before Testing

### Prerequisites Check
```powershell
# 1. Check Python version (3.8+)
python --version

# 2. Install required packages
pip install pillow pycryptodome

# 3. Verify installation
python -c "from PIL import ImageGrab; print('Pillow OK')"
python -c "from Crypto.Cipher import AES; print('Crypto OK')"
```

### Safety Checklist
- ✅ Only testing on your own computer (localhost)
- ✅ No external network connections
- ✅ Antivirus temporarily disabled (optional, if it blocks)
- ✅ Firewall allows localhost connections

---

## 🚀 Test Scenario 1: Basic Connection

**Goal**: Verify client can connect to server

### Steps:

#### 1. Start the Server (Terminal 1)
```powershell
cd "d:\Cyber Security\Remote Access Trojan\server"
python server.py
```

**Expected Output:**
```
==================================================
 RAT SERVER - EDUCATIONAL PROJECT
 Localhost Only - Safe for Testing
==================================================

[*] RAT Server v1.0 - Educational Project
[*] Localhost only (127.0.0.1)
[*] Starting server on 127.0.0.1:4444
[+] Server listening on 127.0.0.1:4444
[*] Waiting for client connection...
```

#### 2. Start the Client (Terminal 2 - New Window)
```powershell
# Open NEW PowerShell window
cd "d:\Cyber Security\Remote Access Trojan\client"
python client.py
```

**Expected Result:**
- GUI window opens
- Shows "RAT Control Panel v1.0"
- Status shows "● Disconnected" (red)

#### 3. Connect
- Click the **"Connect"** button in the GUI
- Wait 1-2 seconds

**Expected Results:**

**Server Terminal:**
```
[+] Client connected from ('127.0.0.1', <port>)
[*] Ready to receive commands...
```

**Client GUI:**
```
[+] Connected successfully!
[+] RAT Server Ready
```
- Status changes to **"● Connected"** (green)
- Connect button becomes disabled

#### ✅ Success Criteria
- Server shows "Client connected"
- Client shows "Connected successfully"
- Status indicator is green
- No error messages

---

## 🧪 Test Scenario 2: Ping Command

**Goal**: Test basic command execution

### Steps:

1. In the Client GUI, click **"🏓 Ping"**

**Expected Output (Client Console):**
```
[*] Sending ping...
[+] Response: pong
```

**Expected Output (Server Terminal):**
```
[*] Received command: ping
```

#### ✅ Success Criteria
- Client receives "pong" response
- No errors displayed

---

## 🧪 Test Scenario 3: System Information

**Goal**: Retrieve victim machine information

### Steps:

1. Click **"📊 System Info"** in Client GUI

**Expected Output (Client Console):**
```
[*] Requesting system information...
[+] System Information:
==================================================
  hostname: YOUR-COMPUTER-NAME
  os: Windows
  os_version: 10.0.19045
  os_release: 10
  architecture: AMD64
  processor: Intel64 Family 6 Model 142 Stepping 12, GenuineIntel
  python_version: 3.11.5
  current_user: YourUsername
  current_directory: d:\Cyber Security\Remote Access Trojan\server
==================================================
```

#### ✅ Success Criteria
- All system fields are populated
- Information matches your actual system
- No errors

---

## 🧪 Test Scenario 4: Screenshot Capture

**Goal**: Capture and transfer screenshot

### Steps:

1. Open some windows on your desktop (Notepad, browser, etc.)
2. Click **"📸 Screenshot"** in Client GUI
3. Wait 2-5 seconds

**Expected Output (Client Console):**
```
[*] Requesting screenshot...
[+] Screenshot received (123456 bytes)
[+] Screenshot saved as: screenshot_12345.png
```

**Expected Result:**
- New window pops up showing your desktop screenshot
- File `screenshot_12345.png` created in client folder
- Image shows what was on your screen

#### ✅ Success Criteria
- Screenshot window appears
- Image is clear and shows your desktop
- File saved successfully
- No corruption

---

## 🧪 Test Scenario 5: Remote Shell

**Goal**: Execute commands remotely

### Steps:

1. Click **"🖥️ Remote Shell"** in Client GUI
2. Dialog box appears: "Enter command to execute"
3. Type: `whoami`
4. Click OK

**Expected Output (Client Console):**
```
[*] Executing: whoami
[+] Command output:
desktop-abc\yourusername
```

### More Commands to Test:

| Command | Expected Output |
|---------|----------------|
| `whoami` | Your username |
| `hostname` | Your computer name |
| `dir` | Current directory listing |
| `echo Hello RAT` | Hello RAT |
| `ipconfig` | Network configuration |

#### ✅ Success Criteria
- Command executes on server
- Output displays in client
- No errors

---

## 🧪 Test Scenario 6: File Browser

**Goal**: Browse remote filesystem

### Steps:

1. Click **"📁 File Browser"**
2. Dialog: "Enter path to list"
3. Type: `C:\`
4. Click OK

**Expected Output (Client Console):**
```
[*] Listing directory: C:\
[+] Directory: C:\
==================================================
📁 Program Files 
📁 Windows 
📁 Users 
📄 pagefile.sys (1234567 bytes)
...
==================================================
```

### More Paths to Test:
- `C:\Users`
- `C:\Windows\System32`
- `.` (current directory)

#### ✅ Success Criteria
- Directories show 📁 icon
- Files show 📄 icon with size
- Listing matches actual folder contents

---

## 🧪 Test Scenario 7: Process List

**Goal**: View running processes

### Steps:

1. Click **"⚙️ Process List"**
2. Wait 1-2 seconds

**Expected Output (Client Console):**
```
[*] Requesting process list...
[+] Process List:
==================================================
Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
System Idle Process              0 Services                   0          8 K
System                           4 Services                   0      1,234 K
python.exe                   12345 Console                    1     45,678 K
...
==================================================
```

#### ✅ Success Criteria
- List shows running processes
- python.exe appears (your server!)
- Process IDs and memory usage shown

---

## 🧪 Test Scenario 8: Kill Process

**Goal**: Terminate a process

### Steps:

1. Open **Notepad** on your computer
2. Click **"🔴 Kill Process"**
3. Dialog: "Enter process name"
4. Type: `notepad.exe`
5. Click OK
6. Confirm: Click **Yes**

**Expected Output (Client Console):**
```
[*] Killing process: notepad.exe
[+] Process notepad.exe terminated
```

**Expected Result:**
- Notepad closes immediately
- Confirmation message appears

#### ⚠️ Warning
Don't kill critical system processes! Only test with:
- notepad.exe
- calc.exe
- mspaint.exe

#### ✅ Success Criteria
- Process terminates
- No errors
- Application closes

---

## 🧪 Test Scenario 9: File Download

**Goal**: Download file from victim machine

### Steps:

#### 1. Create Test File (Server Side)
```powershell
# In server folder
echo "This is a test file" > test_download.txt
```

#### 2. Download File
1. Click **"📥 Download File"**
2. Dialog: "Enter remote file path"
3. Type: `test_download.txt`
4. Click OK
5. Save dialog appears
6. Choose location and click Save

**Expected Output (Client Console):**
```
[*] Downloading: test_download.txt
[+] File saved: C:\Users\...\test_download.txt (21 bytes)
```

**Expected Result:**
- File saves to chosen location
- Content matches original file
- File size correct

#### ✅ Success Criteria
- File downloads successfully
- Content is intact
- No corruption

---

## 🧪 Test Scenario 10: File Upload

**Goal**: Upload file to victim machine

### Steps:

#### 1. Prepare Test File (Client Side)
```powershell
# In client folder
echo "Uploaded by RAT" > test_upload.txt
```

#### 2. Upload File
1. Click **"📤 Upload File"**
2. File browser opens
3. Select `test_upload.txt`
4. Click Open
5. Dialog: "Enter remote path"
6. Type: `received_file.txt`
7. Click OK

**Expected Output (Client Console):**
```
[*] Uploading: test_upload.txt -> received_file.txt
[+] File uploaded: received_file.txt
```

#### 3. Verify Upload
```powershell
# Check server folder
cd "d:\Cyber Security\Remote Access Trojan\server"
type received_file.txt
```

**Expected Output:**
```
Uploaded by RAT
```

#### ✅ Success Criteria
- File appears in server folder
- Content matches original
- Size is correct

---

## 🧪 Test Scenario 11: Disconnection

**Goal**: Properly disconnect and cleanup

### Steps:

1. Click **"Disconnect"** in Client GUI

**Expected Output (Client Console):**
```
[*] Disconnected from server
```

**Expected Output (Server Terminal):**
```
[-] Client disconnected
[*] Cleaning up...
[*] Server stopped
```

**Expected Results:**
- Client status: "● Disconnected" (red)
- Connect button re-enabled
- Server exits gracefully

#### ✅ Success Criteria
- Clean disconnection
- No hanging connections
- Server stops properly

---

## 🧪 Test Scenario 12: Reconnection

**Goal**: Test multiple connection cycles

### Steps:

1. Restart server:
```powershell
python server.py
```

2. Click **"Connect"** in Client GUI
3. Verify connection
4. Test a command (e.g., Ping)
5. Disconnect
6. Repeat steps 2-5 three times

#### ✅ Success Criteria
- Each connection succeeds
- No memory leaks
- Commands work every time

---

## 🧪 Advanced Testing Scenarios

### Test 13: Stress Test - Multiple Commands

Execute rapidly:
1. Ping
2. System Info
3. Process List
4. Ping
5. File Browser
6. Screenshot

**Expected**: All complete successfully without crashes

### Test 14: Large File Transfer

1. Create 10MB test file:
```powershell
fsutil file createnew large_test.bin 10485760
```

2. Upload it
3. Download it back
4. Compare checksums

### Test 15: Long-Running Command

1. Remote Shell: `ping 127.0.0.1 -n 100`
2. Should complete after ~100 seconds
3. Verify output shows all pings

---

## ❌ Troubleshooting Common Issues

### Issue 1: "Connection Refused"

**Symptoms:**
```
[-] Connection error: [WinError 10061] No connection could be made...
```

**Solutions:**
- ✅ Make sure server is running FIRST
- ✅ Check port 4444 not in use: `netstat -an | findstr 4444`
- ✅ Verify host is 127.0.0.1

### Issue 2: "PIL/Pillow not installed"

**Symptoms:**
```
[-] Error: PIL/Pillow not installed
```

**Solution:**
```powershell
pip install pillow
```

### Issue 3: "Module not found"

**Symptoms:**
```
ModuleNotFoundError: No module named 'Crypto'
```

**Solution:**
```powershell
pip install pycryptodome
```

### Issue 4: Server Hangs

**Symptoms:**
- Server stops responding
- No output after command

**Solution:**
- Press `Ctrl+C` in server terminal
- Restart server
- Check for infinite loops

### Issue 5: Screenshot Window Doesn't Appear

**Symptoms:**
- "Screenshot received" but no window

**Solution:**
- Check behind other windows
- Look for `.png` file in client folder
- Open manually

---

## 📊 Testing Checklist

Print this and check off as you test:

- [ ] Basic connection works
- [ ] Ping responds
- [ ] System info displays correctly
- [ ] Screenshot captures and displays
- [ ] Remote shell executes commands
- [ ] File browser lists directories
- [ ] Process list shows running processes
- [ ] Kill process terminates application
- [ ] File download works
- [ ] File upload works
- [ ] Disconnection is clean
- [ ] Reconnection works
- [ ] No crashes or errors
- [ ] All features work as expected

---

## 🎓 Demo Script for Companies

When presenting to companies, follow this flow:

### 1. Introduction (30 seconds)
"This is a Remote Access Trojan educational project demonstrating client-server architecture, network communication, and cybersecurity concepts."

### 2. Architecture Overview (1 minute)
Show README.md architecture diagram
Explain client-server model

### 3. Live Demo (5 minutes)

**Step 1: Connection**
- Start server
- Start client
- Connect

**Step 2: System Reconnaissance**
- System Info
- Process List
- File Browser

**Step 3: Remote Control**
- Execute shell command
- Take screenshot
- Show result

**Step 4: File Operations**
- Upload demo file
- Download file back
- Verify

### 4. Code Walkthrough (3 minutes)
- Show server.py structure
- Explain command handler
- Show client GUI code

### 5. Q&A (2 minutes)
Be ready to answer:
- How does socket communication work?
- How would you add encryption?
- What security measures are included?
- How could this scale to multiple clients?

---

## 🔐 Post-Testing

### Cleanup:
1. Stop server (Ctrl+C)
2. Close client GUI
3. Delete test files
4. Clear screenshots

### Security:
1. Re-enable antivirus
2. Remove from startup (if added)
3. Delete logs (optional)

---

## 📝 Testing Log Template

Use this to track your tests:

```
Date: __________
Tester: __________

Test #1: Basic Connection
Result: ☐ Pass ☐ Fail
Notes: _________________

Test #2: Ping Command
Result: ☐ Pass ☐ Fail
Notes: _________________

...

Overall Status: ☐ All Passed ☐ Some Failed
Issues Found: _________________
```

---

## ✅ Ready to Present!

Once all tests pass:
1. ✅ Take screenshots of successful tests
2. ✅ Record a demo video (optional)
3. ✅ Prepare your talking points
4. ✅ Review HOW_IT_WORKS.md
5. ✅ Practice your demo
6. ✅ Impress the company! 🚀

---

**You're now a RAT expert! Good luck with your presentation!** 🎓
