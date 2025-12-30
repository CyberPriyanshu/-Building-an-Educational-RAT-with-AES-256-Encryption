# 🚀 Quick Start Guide - Enhanced RAT v2.0

## ⚡ 3-Minute Setup

### Step 1: Install Dependencies (1 minute)
```powershell
cd "d:\Cyber Security\Remote Access Trojan"
py -m pip install -r requirements.txt
```

**Installs:**
- pillow (screenshots)
- pycryptodome (AES-256 encryption)
- opencv-python (webcam capture)

---

### Step 2: Start Server (30 seconds)
```powershell
# In Terminal 1
py server/server.py
```

**You'll see:**
```
============================================================
  ENHANCED RAT SERVER v2.0 - Educational Project
  ⚠️  LOCALHOST ONLY - SAFE FOR LEARNING ⚠️
============================================================
[*] Process: svchost.exe (simulated)
[*] Encryption: AES-256 Enabled
[+] Server listening on 127.0.0.1:4444
[*] Waiting for client connection...
```

---

### Step 3: Launch Client (30 seconds)
```powershell
# In Terminal 2
py client/client.py
```

**Actions:**
1. Read and accept Terms & Conditions
2. Click "Connect" button
3. Status shows: "● Connected" (green)

---

### Step 4: Test Features (1 minute)

**Try these buttons:**

1. **🏓 Ping** - Test encrypted connection
   - Response: "pong"

2. **📊 System Info** - Get target details
   - Shows: OS, hostname, platform, etc.

3. **📸 Screenshot** - Capture screen
   - Opens image in new window

4. **🔐 Encryption Test** - Verify AES-256
   - Shows: Encryption status and test result

5. **📷 Webcam Capture** - Camera access
   - Captures and displays webcam image

6. **👻 Stealth Info** - Educational info
   - Shows: Stealth techniques and detection methods

---

## 🧪 Run Automated Tests

### Basic Test (6 features)
```powershell
py test_quick.py
```

### Advanced Test (9 features)
```powershell
py test_enhanced.py
```

**Expected:** ✅ 100% pass rate

---

## 📚 Documentation Files

Quick reference to all docs:

| File | Purpose |
|------|---------|
| `README.md` | Main documentation |
| `HOW_IT_WORKS.md` | Technical details |
| `TESTING_GUIDE.md` | Test instructions |
| `ENHANCED_TEST_RESULTS.md` | Test results |
| `COMPLETION_SUMMARY.md` | Project summary |
| `INTERVIEW_GUIDE.md` | Presentation guide |
| `QUICK_START.md` | This file |

---

## 🎯 Feature Reference

### Core Features (Blue Buttons)
- 📊 System Info
- 📸 Screenshot  
- 🖥️ Remote Shell
- 📁 File Browser
- ⚙️ Process List
- 📥 Download File
- 📤 Upload File

### Special Features (Red/Green)
- 🔴 Kill Process (dangerous)
- 🏓 Ping (test)

### Advanced Features (Purple)
- ⌨️ Keylogger (simulated)
- 📷 Webcam Capture
- 🔒 Persistence Info

### Info Features (Gray)
- 👻 Stealth Info
- 🔐 Encryption Test
- ℹ️ About RAT

---

## 🔧 Troubleshooting

### Server won't start
```powershell
# Check if port 4444 is in use
netstat -ano | findstr :4444

# Kill process using port
taskkill /PID <PID> /F
```

### Client can't connect
1. Make sure server is running first
2. Check status shows "Waiting for client..."
3. Verify IP is 127.0.0.1 (localhost)

### Webcam not working
```powershell
# Check if opencv is installed
py -m pip show opencv-python

# Reinstall if needed
py -m pip install opencv-python --upgrade
```

### Tests failing
1. Stop any running server/client
2. Start fresh server
3. Run test script
4. Server should restart for each test run

---

## 💡 Quick Commands Cheat Sheet

```powershell
# Start server
py server/server.py

# Start client
py client/client.py

# Run basic tests
py test_quick.py

# Run advanced tests  
py test_enhanced.py

# Install dependencies
py -m pip install -r requirements.txt

# Check Python version
py --version

# List installed packages
py -m pip list
```

---

## 🎤 Demo in 60 Seconds

For quick demonstrations:

1. **Start server** (Terminal 1)
2. **Launch client** (Terminal 2)
3. **Accept terms** and **Connect**
4. **Click "System Info"** - Show data retrieval
5. **Click "Encryption Test"** - Prove AES-256 working
6. **Click "Webcam Capture"** - Show multimedia
7. **Click "Stealth Info"** - Show security knowledge

**Total time:** ~60 seconds  
**Demonstrates:** Encryption, GUI, features, ethics

---

## 📊 System Requirements

**Minimum:**
- Python 3.8+
- Windows 7+
- 100 MB disk space
- Internet (for initial setup only)

**Recommended:**
- Python 3.12.4
- Windows 10/11
- Webcam (for webcam features)
- 2 GB RAM

**Tested On:**
- Python 3.12.4
- Windows 11
- 8 GB RAM
- Webcam available

---

## ⚠️ Safety Reminders

Before you start:

✅ **This is educational only**  
✅ **Runs on localhost (127.0.0.1) only**  
✅ **No external network access**  
✅ **Terms & conditions required**  
✅ **No malicious capabilities**  

❌ **Don't modify host IP**  
❌ **Don't remove safety checks**  
❌ **Don't use unauthorized**  
❌ **Don't share for malicious use**  

---

## 🎉 You're Ready!

Project is complete and tested. Use for:
- Portfolio demonstrations
- Job interviews
- Educational purposes
- Security research
- Learning cybersecurity

**100% tested and working!** ✅

---

## 📞 Need Help?

1. Check documentation files
2. Review test results
3. Read HOW_IT_WORKS.md
4. Check INTERVIEW_GUIDE.md

---

⚡ **Start now:** `py server/server.py` in one terminal, `py client/client.py` in another!
