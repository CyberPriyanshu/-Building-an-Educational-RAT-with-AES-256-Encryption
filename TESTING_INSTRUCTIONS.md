# 🧪 RAT Tool Testing Guide - Step by Step

## 📋 How to Test All 9 Features

This guide shows you exactly how to test each of the 9 advanced RAT features and what results to expect.

---

## 🚀 QUICK START

### Step 1: Launch the RAT Tool
```powershell
cd "d:\Cyber Security\Remote Access Trojan"
py rat_tool.py
```

### Step 2: Accept Terms & Conditions
- Read the terms dialog
- Click "YES" to accept

### Step 3: Wait for Auto-Connection
- Server starts automatically (2-3 seconds)
- Status will show "Server: ● Running" (green)
- Click "Connect to Server" button
- Status will show "Client: ● Connected" (green)

### Step 4: You're Ready!
- Click any numbered button (1️⃣ to 9️⃣) to test individual features
- Or click "🧪 Run All Tests" to test everything automatically

---

## 🧪 TESTING EACH FEATURE (Step-by-Step)

### ✅ Test 1: PING TEST

**Button:** `6️⃣ Ping Test` (green button)

**What it does:** Tests encrypted connection between client and server

**How to test:**
1. Click "6️⃣ Ping Test" button
2. Wait 1-2 seconds

**Expected Result:**
```
════════════════════════════════════════════════════════════════════════════
🏓 TEST 1/9: PING TEST - Testing encrypted connection
════════════════════════════════════════════════════════════════════════════
[+] ✅ Response: pong
[+] RESULT: Ping test PASSED - Connection working with encryption!
════════════════════════════════════════════════════════════════════════════
```

**What success looks like:**
- Message says "pong"
- Shows "✅ PASSED"
- Confirms encryption is working

---

### ✅ Test 2: SYSTEM INFORMATION

**Button:** `1️⃣ System Info` (blue button)

**What it does:** Retrieves detailed system information from target

**How to test:**
1. Click "1️⃣ System Info" button
2. Wait 2-3 seconds

**Expected Result:**
```
════════════════════════════════════════════════════════════════════════════
📊 TEST 2/9: SYSTEM INFORMATION - Gathering target system details
════════════════════════════════════════════════════════════════════════════
[+] ✅ System Information Retrieved:
────────────────────────────────────────────────────────────────────────────
  • platform: Windows
  • platform_release: 11
  • platform_version: 10.0.22631
  • architecture: AMD64
  • hostname: Priyanshu
  • processor: Intel64 Family 6 Model 142 Stepping 12, GenuineIntel
  • python_version: 3.12.4
────────────────────────────────────────────────────────────────────────────
[+] RESULT: System info test PASSED - All details retrieved!
════════════════════════════════════════════════════════════════════════════
```

**What success looks like:**
- Shows your Windows version
- Shows your hostname
- Shows processor details
- All 7 fields displayed
- Shows "✅ PASSED"

---

### ✅ Test 3: SCREENSHOT CAPTURE

**Button:** `2️⃣ Screenshot` (blue button)

**What it does:** Captures the current screen and displays it

**How to test:**
1. Click "2️⃣ Screenshot" button
2. Wait 3-5 seconds (processing image)

**Expected Result:**
```
════════════════════════════════════════════════════════════════════════════
📸 TEST 3/9: SCREENSHOT CAPTURE - Capturing target screen
════════════════════════════════════════════════════════════════════════════
[+] ✅ Screenshot captured successfully!
[+] Image size: 150000+ bytes
[+] RESULT: Screenshot test PASSED - Image displayed in new window!
════════════════════════════════════════════════════════════════════════════
```

**What success looks like:**
- Console shows "✅ PASSED"
- **NEW WINDOW OPENS** showing your screenshot
- Image displays your current desktop
- Window title says "Screenshot Capture - Test 3"

---

### ✅ Test 4: REMOTE SHELL

**Button:** `3️⃣ Remote Shell` (blue button)

**What it does:** Executes commands on the target system

**How to test:**
1. Click "3️⃣ Remote Shell" button
2. A dialog box appears asking for command
3. Type: `echo Hello RAT Test`
4. Click OK

**Expected Result:**
```
════════════════════════════════════════════════════════════════════════════
🖥️ TEST 4/9: REMOTE SHELL - Executing command on target
════════════════════════════════════════════════════════════════════════════
[*] Executing: echo Hello RAT Test
[+] ✅ Command executed successfully!
────────────────────────────────────────────────────────────────────────────
OUTPUT:
Hello RAT Test
────────────────────────────────────────────────────────────────────────────
[+] RESULT: Remote shell test PASSED - Command executed!
════════════════════════════════════════════════════════════════════════════
```

**Other commands to try:**
- `whoami` - Shows current user
- `hostname` - Shows computer name
- `dir` - Lists files in current directory
- `systeminfo` - Full system information

**What success looks like:**
- Your command output is displayed
- Shows "✅ PASSED"
- Output matches what you'd see in cmd.exe

---

### ✅ Test 5: FILE BROWSER

**Button:** `4️⃣ File Browser` (blue button)

**What it does:** Lists files and folders in a directory

**How to test:**
1. Click "4️⃣ File Browser" button
2. Dialog appears asking for path
3. Type: `.` (current directory) or `C:\`
4. Click OK

**Expected Result:**
```
════════════════════════════════════════════════════════════════════════════
📁 TEST 5/9: FILE BROWSER - Listing directory contents
════════════════════════════════════════════════════════════════════════════
[*] Listing: .
[+] ✅ Found 18 items:
────────────────────────────────────────────────────────────────────────────
  • client
  • server
  • README.md
  • rat_tool.py
  • test_enhanced.py
  • requirements.txt
  ... (more files)
────────────────────────────────────────────────────────────────────────────
[+] RESULT: File browser test PASSED - Directory listed!
════════════════════════════════════════════════════════════════════════════
```

**What success looks like:**
- Shows list of files/folders
- Number of items displayed
- Shows "✅ PASSED"

---

### ✅ Test 6: PROCESS LIST

**Button:** `5️⃣ Process List` (blue button)

**What it does:** Lists all running processes on the system

**How to test:**
1. Click "5️⃣ Process List" button
2. Wait 2-3 seconds (processing)

**Expected Result:**
```
════════════════════════════════════════════════════════════════════════════
⚙️ TEST 6/9: PROCESS LIST - Enumerating running processes
════════════════════════════════════════════════════════════════════════════
[+] ✅ Retrieved 317 processes:
────────────────────────────────────────────────────────────────────────────
  • PID:      0 | Name: System Idle Process
  • PID:      4 | Name: System
  • PID:    124 | Name: Registry
  • PID:    456 | Name: smss.exe
  • PID:    780 | Name: csrss.exe
  • PID:    912 | Name: wininit.exe
  ... (more processes)
  ... and 302 more processes
────────────────────────────────────────────────────────────────────────────
[+] RESULT: Process list test PASSED - All processes enumerated!
════════════════════════════════════════════════════════════════════════════
```

**What success looks like:**
- Shows 200-400 processes (varies by system)
- Each process shows PID and Name
- Shows first 15 processes
- Shows "✅ PASSED"

---

### ✅ Test 7: KEYLOGGER SIMULATION

**Button:** `7️⃣ Keylogger (Sim)` (purple button)

**What it does:** Demonstrates keylogger concept (SIMULATED - not real)

**How to test:**
1. Click "7️⃣ Keylogger (Sim)" button
2. Wait 1-2 seconds

**Expected Result:**
```
════════════════════════════════════════════════════════════════════════════
⌨️ TEST 7/9: KEYLOGGER SIMULATION - Educational demonstration
════════════════════════════════════════════════════════════════════════════
[+] ✅ Keylogger Status:
────────────────────────────────────────────────────────────────────────────
  • Active: True
  • Buffer Size: 1 keystrokes
  • Sample Data: This is simulated educational data. Real keyloggers are ILLEGAL without authorization!
  • Warning: EDUCATIONAL SIMULATION ONLY
────────────────────────────────────────────────────────────────────────────
⚠️  NOTE: This is SIMULATED data for educational purposes!
    Real keyloggers are ILLEGAL without authorization!
[+] RESULT: Keylogger test PASSED - Simulation working!
════════════════════════════════════════════════════════════════════════════
```

**What success looks like:**
- Shows "Active: True"
- Sample data is fake/educational
- Warning messages displayed
- Shows "✅ PASSED"
- **IMPORTANT:** This is NOT capturing real keystrokes

---

### ✅ Test 8: WEBCAM CAPTURE

**Button:** `8️⃣ Webcam Capture` (purple button)

**What it does:** Captures image from your webcam

**How to test:**
1. Click "8️⃣ Webcam Capture" button
2. Wait 2-4 seconds (camera initialization)

**Expected Result (if webcam exists):**
```
════════════════════════════════════════════════════════════════════════════
📷 TEST 8/9: WEBCAM CAPTURE - Accessing target camera
════════════════════════════════════════════════════════════════════════════
[+] ✅ Webcam captured successfully!
[+] Image size: 30808 bytes
[+] RESULT: Webcam test PASSED - Camera image displayed!
════════════════════════════════════════════════════════════════════════════
```

**Expected Result (if no webcam):**
```
════════════════════════════════════════════════════════════════════════════
📷 TEST 8/9: WEBCAM CAPTURE - Accessing target camera
════════════════════════════════════════════════════════════════════════════
[-] ⚠️  Webcam: Failed to capture webcam
    (This is expected if no webcam is available)
════════════════════════════════════════════════════════════════════════════
```

**What success looks like:**
- If webcam exists: **NEW WINDOW OPENS** with your camera image
- Window title says "Webcam Capture - Test 8"
- Shows your face or room
- If no webcam: Shows warning (this is OK)

---

### ✅ Test 9: PERSISTENCE INFORMATION

**Button:** `9️⃣ Persistence Info` (purple button)

**What it does:** Shows educational information about persistence techniques

**How to test:**
1. Click "9️⃣ Persistence Info" button
2. Wait 1-2 seconds

**Expected Result:**
```
════════════════════════════════════════════════════════════════════════════
🔒 TEST 9/9: PERSISTENCE INFORMATION - Educational techniques
════════════════════════════════════════════════════════════════════════════
[+] ✅ Persistence Techniques (Educational):
────────────────────────────────────────────────────────────────────────────

📋 Registry Persistence:
  • HKCU\Software\Microsoft\Windows\CurrentVersion\Run
  • HKLM\Software\Microsoft\Windows\CurrentVersion\Run
  • HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce

📁 Startup Folder:
  • %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
  • %PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\Startup

⏰ Scheduled Tasks:
  • Task Scheduler - User logon trigger
  • Task Scheduler - System startup trigger

⚙️ Windows Services:
  • Windows Service installation
  • Service with auto-start configuration

────────────────────────────────────────────────────────────────────────────
⚠️  EDUCATIONAL INFORMATION ONLY - NOT IMPLEMENTED
[+] RESULT: Persistence test PASSED - All techniques documented!
════════════════════════════════════════════════════════════════════════════
```

**What success looks like:**
- Shows 4 categories: Registry, Startup, Tasks, Services
- Total of 9 techniques listed
- Warning says "NOT IMPLEMENTED"
- Shows "✅ PASSED"
- **IMPORTANT:** This only shows information, doesn't create persistence

---

## 🎯 BONUS FEATURES

### 🔍 Stealth Info

**Button:** `🔍 Stealth Info` (gray button)

**What it does:** Shows stealth techniques and detection methods

**Expected Result:**
- Lists 5 stealth techniques
- Lists 6 detection methods
- Shows current status (process name, encryption, etc.)
- Educational information only

---

### 🔐 Encryption Test

**Button:** `🔐 Encryption Test` (teal button)

**What it does:** Verifies AES-256 encryption is working

**Expected Result:**
```
════════════════════════════════════════════════════════════════════════════
🔐 ENCRYPTION TEST - Verifying AES-256-CBC
════════════════════════════════════════════════════════════════════════════
🔐 Encryption Enabled: True
🔑 Algorithm: AES-256-CBC with random IV
🔒 Key Derivation: SHA-256 hash of passphrase
────────────────────────────────────────────────────────────────────────────
[+] ✅ Encryption test SUCCESSFUL!
[+] Command encrypted → Server decrypted → Response encrypted → Client decrypted
════════════════════════════════════════════════════════════════════════════
```

---

### 🧪 Run All Tests

**Button:** `🧪 Run All Tests` (orange button)

**What it does:** Runs all 9 tests automatically in sequence

**How to test:**
1. Click "🧪 Run All Tests" button
2. Click "Yes" on confirmation dialog
3. Wait 10-15 seconds for all tests to complete

**Expected Result:**
- Clears console
- Runs Test 1 through Test 9 automatically
- Each test shows "✅ PASSED"
- Screenshot and webcam windows open automatically
- Final summary shows:
  ```
  🎉 ALL 9 TESTS COMPLETED SUCCESSFULLY!
  
  📊 TEST SUMMARY:
    ✅ Test 1: Ping - PASSED
    ✅ Test 2: System Info - PASSED
    ✅ Test 3: Screenshot - PASSED
    ✅ Test 4: Remote Shell - PASSED
    ✅ Test 5: File Browser - PASSED
    ✅ Test 6: Process List - PASSED
    ✅ Test 7: Keylogger Simulation - PASSED
    ✅ Test 8: Webcam Capture - PASSED (or no webcam)
    ✅ Test 9: Persistence Info - PASSED
  
  🏆 SUCCESS RATE: 100% (9/9 tests)
  ```
- Dialog box appears: "✅ All 9 tests completed successfully!"

---

## 📊 EXPECTED SUCCESS CRITERIA

### For Each Test:

✅ **PASS Criteria:**
- Console shows "✅ PASSED" or "✅" symbol
- No error messages
- Expected data is displayed
- For screenshot/webcam: New window opens with image

❌ **FAIL Criteria:**
- Shows "❌ FAILED" or error message
- No data displayed
- Connection error
- Timeout

---

## 🐛 Troubleshooting

### Problem: Server won't start
**Solution:**
```powershell
# Check if port 4444 is in use
netstat -ano | findstr :4444

# If something is using it, restart the tool
```

### Problem: Can't connect to server
**Solution:**
- Wait 3-5 seconds after launching
- Make sure "Server: ● Running" shows green
- Click "Connect to Server" button
- If fails, restart the tool

### Problem: Webcam test fails
**Solution:**
- This is NORMAL if you don't have a webcam
- Check Device Manager for camera
- Some laptops have camera switches/privacy shutters
- Try closing other apps using camera (Zoom, Teams, etc.)

### Problem: Screenshot is black
**Solution:**
- This is normal for some applications
- Desktop should capture fine
- Try clicking on desktop before taking screenshot

---

## 🎯 SUMMARY TABLE

| # | Feature | Button | Expected Time | Window Opens? | Pass Rate |
|---|---------|--------|---------------|---------------|-----------|
| 1 | Ping | 6️⃣ Green | 1-2 sec | No | 100% |
| 2 | System Info | 1️⃣ Blue | 2-3 sec | No | 100% |
| 3 | Screenshot | 2️⃣ Blue | 3-5 sec | **YES** | 100% |
| 4 | Remote Shell | 3️⃣ Blue | 1-2 sec | No | 100% |
| 5 | File Browser | 4️⃣ Blue | 2-3 sec | No | 100% |
| 6 | Process List | 5️⃣ Blue | 2-3 sec | No | 100% |
| 7 | Keylogger | 7️⃣ Purple | 1-2 sec | No | 100% |
| 8 | Webcam | 8️⃣ Purple | 2-4 sec | **YES** (if camera exists) | 95% |
| 9 | Persistence | 9️⃣ Purple | 1-2 sec | No | 100% |

**Total Expected Pass Rate: 100% (9/9 tests)**  
*Webcam may show warning if no camera - this is acceptable*

---

## 🏆 FINAL VERIFICATION

After running all tests, you should see:

✅ **9/9 tests show "PASSED"**  
✅ **No errors in console**  
✅ **Screenshot window opened**  
✅ **Webcam window opened (or warning if no camera)**  
✅ **All data displayed correctly**  
✅ **Server status: Green**  
✅ **Client status: Green**  

**Congratulations! Your RAT Tool is working perfectly!** 🎉

---

⚠️ **REMEMBER:** FOR EDUCATIONAL USE ONLY • LOCALHOST ONLY • NO UNAUTHORIZED ACCESS
