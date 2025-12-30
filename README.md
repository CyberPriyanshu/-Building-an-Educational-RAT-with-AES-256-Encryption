# 🔐 Enhanced Remote Access Trojan (RAT) - Educational Project v2.0

> **⚠️ IMPORTANT DISCLAIMER**  
> This project is **STRICTLY FOR EDUCATIONAL PURPOSES** only. Designed for:
> - Portfolio demonstrations
> - Security research and learning
> - Job interview presentations
> - Understanding RAT mechanics for defensive security
> 
> **HARDCODED TO LOCALHOST (127.0.0.1) ONLY**  
> No unauthorized use permitted. Creator not liable for misuse.

---

## 🎯 Project Overview

A **professionally crafted Remote Access Trojan** demonstrating advanced cybersecurity concepts:
- **AES-256 encrypted C2 communication**
- **Keylogger simulation** (educational only)
- **Webcam capture** capabilities
- **Persistence mechanisms** (informational)
- **Stealth techniques** and detection methods
- **Full remote system control**

Perfect for demonstrating security knowledge in interviews and portfolio presentations.

---

## ✨ Features

### 🔒 Core RAT Capabilities
1. **System Information** - OS, hostname, architecture, processor
2. **Screenshot Capture** - Full-screen capture with save
3. **Remote Shell** - Execute commands remotely
4. **File Browser** - Navigate file system
5. **Process Manager** - List and kill processes
6. **File Transfer** - Upload/download files
7. **Ping/Connectivity** - Test connection

### 🚀 Enhanced Features (v2.0)
8. **AES-256 Encryption** - Military-grade encrypted C2 
9. **Keylogger Simulation** - Educational demo (not real)
10. **Webcam Capture** - Real-time camera access
11. **Persistence Info** - Registry, startup, tasks (educational)
12. **Stealth Analysis** - Techniques and detection
13. **Professional GUI** - Dark theme, color-coded
14. **Terms & Conditions** - Built-in ethical guidelines

---

## 🔧 Installation

```powershell
# Install dependencies
py -m pip install -r requirements.txt

# Dependencies: pillow, pycryptodome, opencv-python
```

---

## 🚀 Usage

### Start Server
```powershell
py server/server.py
```

### Launch Client
```powershell
py client/client.py
```

### Run Tests
```powershell
py test_enhanced.py  # Test all 9 advanced features
```

---

## 📊 Test Results

**✅ ALL 9 ENHANCED FEATURES: PASSED (100%)**

| Feature | Status |
|---------|--------|
| Encrypted Connection | ✅ AES-256-CBC |
| Keylogger Simulation | ✅ Educational |
| Webcam Capture | ✅ 30KB+ captured |
| Persistence Info | ✅ 9 techniques |
| Stealth Info | ✅ 5 techniques |
| Process List | ✅ 317 processes |
| Remote Shell | ✅ Working |
| System Info | ✅ Complete |
| Encrypted Ping | ✅ Verified |

See [ENHANCED_TEST_RESULTS.md](ENHANCED_TEST_RESULTS.md) for details.

---

## 🎓 Educational Value

### For Interviews
"I developed an educational RAT demonstrating:
- Secure C2 channels using AES-256 encryption
- Common malware techniques (stealth, persistence)
- Responsible tool development (localhost-only)
- Full-stack implementation (server, GUI, tests)
- Both offensive and defensive security perspectives"

### Skills Demonstrated
- Network programming (encrypted TCP sockets)
- Cryptography (AES-256-CBC implementation)
- GUI development (Tkinter, 650+ lines)
- System APIs (process, file management)
- Multimedia (screenshots, webcam)
- Testing (automated suites, 100% pass)
- Security awareness (detection methods)

---

## 🔒 Security Features

### Encryption
- **Algorithm:** AES-256-CBC
- **Key:** SHA-256 derived
- **IV:** Random 16-byte per message
- **Verified:** End-to-end working

### Safety
- ✅ Hardcoded localhost only
- ✅ Terms dialog on startup
- ✅ Educational warnings
- ✅ No real persistence
- ✅ Simulated keylogger only

---

## 🛡️ Detection & Defense

### Detection Methods Taught
1. Network traffic analysis
2. Process behavior monitoring
3. Antivirus signatures
4. Heuristic analysis
5. Behavioral detection
6. Memory forensics

### How to Defend
- Monitor network connections
- Use endpoint detection (EDR)
- Application whitelisting
- Regular security audits

---

## 📚 Documentation

- [HOW_IT_WORKS.md](HOW_IT_WORKS.md) - Technical architecture
- [TESTING_GUIDE.md](TESTING_GUIDE.md) - Testing instructions
- [ENHANCED_TEST_RESULTS.md](ENHANCED_TEST_RESULTS.md) - Advanced results
- [PROJECT_STATUS.md](PROJECT_STATUS.md) - Development status

---

## ⚖️ Legal & Ethical Notice

### ✅ ALLOWED
- Personal education
- Portfolio demos
- Interview presentations
- Own system testing

### ❌ PROHIBITED
- Unauthorized access
- Network use without permission
- Malicious purposes
- Removing safety restrictions

**USE AT YOUR OWN RISK - YOU ARE RESPONSIBLE**

---

## 🏆 Achievements

- ✅ 14 features implemented
- ✅ AES-256 encryption working
- ✅ 100% test pass rate (9/9)
- ✅ Professional GUI (15 buttons)
- ✅ 5 documentation files
- ✅ 2 automated test suites
- ✅ Portfolio-ready

**Version:** 2.0 Enhanced  
**Status:** ✅ Complete & Tested  
**Purpose:** Educational Portfolio

⚠️ **LOCALHOST ONLY • ETHICAL USE ONLY**
