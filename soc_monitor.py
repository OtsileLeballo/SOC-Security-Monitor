# ============================================
# SOC SECURITY MONITOR - BBD BURSARY PROJECT
# Created by: Otsile Leballo
# Purpose: Demonstrate SOC monitoring skills
# ============================================

import socket
import platform
from datetime import datetime
import json

def main():
    print("\n" + "="*60)
    print("        SOC SECURITY MONITORING TOOL")
    print("="*60)
    print("For BBD Bursary Application - Cybersecurity Focus")
    print("="*60 + "\n")
    
    # 1. SYSTEM INFORMATION
    print("[1] 📊 SYSTEM INFORMATION")
    print("-" * 40)
    print(f"• Hostname: {socket.gethostname()}")
    print(f"• Operating System: {platform.system()} {platform.release()}")
    print(f"• Python Version: {platform.python_version()}")
    print(f"• Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 2. PORT SECURITY CHECK
    print("\n[2] 🔍 PORT SECURITY ASSESSMENT")
    print("-" * 40)
    print("Checking common ports on localhost...")
    
    ports_to_check = [
        (21, "FTP"),
        (22, "SSH"),
        (23, "Telnet"),
        (25, "SMTP"),
        (53, "DNS"),
        (80, "HTTP"),
        (443, "HTTPS"),
        (3389, "RDP")
    ]
    
    open_ports = []
    
    for port, service in ports_to_check:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            result = sock.connect_ex(('127.0.0.1', port))
            sock.close()
            
            if result == 0:
                status = "🔴 OPEN"
                open_ports.append({"port": port, "service": service})
            else:
                status = "🟢 CLOSED"
            
            print(f"   Port {port:4d} ({service:6s}): {status}")
        except:
            print(f"   Port {port:4d} ({service:6s}): ⚠️  ERROR")
    
    # 3. SECURITY REPORT
    print("\n[3] 📋 GENERATING SECURITY REPORT")
    print("-" * 40)
    
    report_data = {
        "project": "SOC Security Monitor",
        "student": "Otsile Leballo",
        "purpose": "BBD Bursary Application - Cybersecurity Demonstration",
        "scan_date": datetime.now().isoformat(),
        "system_info": {
            "hostname": socket.gethostname(),
            "platform": f"{platform.system()} {platform.version()}",
            "python_version": platform.python_version()
        },
        "port_scan_results": {
            "total_checked": len(ports_to_check),
            "open_ports": open_ports,
            "security_notes": [
                "Port 22 (SSH) should be closed if not needed",
                "Port 3389 (RDP) is a common attack target",
                "Regular port audits improve security posture"
            ]
        },
        "soc_recommendations": [
            "Implement regular vulnerability scanning",
            "Monitor for unauthorized open ports",
            "Maintain firewall rules for unused services",
            "Document all security configurations",
            "Follow principle of least privilege"
        ]
    }
    
    # Display report summary
    print(f"   • Open ports found: {len(open_ports)}")
    if open_ports:
        print("   • Details:")
        for port_info in open_ports:
            print(f"     - Port {port_info['port']} ({port_info['service']})")
    
    # 4. SOC WORKFLOW DEMONSTRATION
    print("\n[4] 🔄 SOC ANALYST WORKFLOW")
    print("-" * 40)
    workflow = [
        ("1. MONITOR", "Continuous security monitoring"),
        ("2. DETECT", "Identify potential threats"),
        ("3. ANALYZE", "Investigate security events"),
        ("4. RESPOND", "Contain and eradicate threats"),
        ("5. REPORT", "Document and improve processes")
    ]
    
    for step, description in workflow:
        print(f"   {step}: {description}")
    
    # 5. FINAL SUMMARY
    print("\n" + "="*60)
    print("                    SCAN COMPLETE")
    print("="*60)
    print(f"✅ Project: SOC Security Monitoring Tool")
    print(f"✅ Created: For BBD Bursary Application")
    print(f"✅ Purpose: Demonstrate cybersecurity skills")
    print(f"✅ Status: Tool executed successfully")
    
    print("\n📚 This project demonstrates:")
    print("   • Understanding of network security concepts")
    print("   • Python programming for security tools")
    print("   • SOC monitoring workflows")
    print("   • Security reporting and documentation")
    
    print("\n" + "="*60)
    print("           END OF REPORT")
    print("="*60)
    
    return report_data

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n⚠️  Error occurred: {e}")
        print("The tool still demonstrates security concepts for learning purposes.")
