# SOC-Security-Monitor
I've developed a Python-based SOC Security Monitoring Tool that performs system security checks and demonstrates understanding of SOC workflows


# 🔒 SOC Security Monitoring Tool

A Python-based security monitoring tool, demonstrating cybersecurity and SOC analyst skills.

## 🎯 Project Purpose
This project was created to showcase:
- Understanding of Security Operations Center (SOC) workflows
- Practical Python programming for security tools
- Network security monitoring concepts
- Professional documentation and reporting

## 🚀 Live Demo
The code runs successfully on OneCompiler: [View Live Run](https://onecompiler.com/python)

## 📋 Features
- **System Information Gathering** - Hostname, OS, scan time
- **Port Security Assessment** - Checks common ports on localhost
- **Security Reporting** - Generates structured security report
- **SOC Workflow Demonstration** - Shows standard SOC analyst procedures

## 🛠️ Technologies Used
- Python 3.x (Standard Library Only)
- Socket programming for network checks
- JSON for report generation
- Platform module for system information

## 📊 Sample Output
============================================================
SOC SECURITY MONITORING TOOL
============================================================

[1] 📊 SYSTEM INFORMATION

• Hostname: test-system
• Operating System: Linux
• Scan Time: 2024-03-20 14:30:00

[2] 🔍 PORT SECURITY ASSESSMENT

Port 80 (HTTP ): 🟢 CLOSED
Port 443 (HTTPS ): 🟢 CLOSED
Port 22 (SSH ): 🟢 CLOSED

[3] 📋 GENERATING SECURITY REPORT

• Open ports found: 0

... (Full output in screenshots)


## 🎓 Learning Outcomes
Through this project, I demonstrated:
1. **Security Monitoring** - Understanding of port scanning for security assessment
2. **Python Development** - Creating practical security tools
3. **SOC Concepts** - Knowledge of Security Operations Center workflows
4. **Documentation** - Professional reporting and project documentation
5. **Ethical Security** - Responsible scanning of only localhost systems


## 🔧 How to Run
```bash
# Method 1: OneCompiler (Recommended)
1. Visit https://onecompiler.com/python
2. Paste the code
3. Click "Run"

# Method 2: Local Python
python soc_monitor.py
