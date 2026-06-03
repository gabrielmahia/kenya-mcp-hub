#!/usr/bin/env python3
"""
kenya-mcp-hub — CLI registry for East Africa MCP servers
Usage: kenya-mcp-hub list | kenya-mcp-hub install <server>
"""
import sys, subprocess

REGISTRY = {
    "mpesa":    {"package": "mpesa-mcp",          "cmd": "mpesa-mcp",          "desc": "M-PESA Daraja API"},
    "water":    {"package": "wapimaji-mcp",        "cmd": "wapimaji-mcp",       "desc": "Kenya water data"},
    "health":   {"package": "swahili-health-mcp",  "cmd": "swahili-health-mcp", "desc": "Kenya DHIS2 health data"},
    "legal":    {"package": "kenya-legal-rag",     "cmd": "kenya-legal-rag",    "desc": "Kenya legal documents RAG"},
}

def list_servers():
    print("\n🔌 Kenya MCP Hub — Available Servers\n")
    print(f"{'Name':<12} {'Package':<25} {'Description'}")
    print("-" * 60)
    for name, info in REGISTRY.items():
        print(f"{name:<12} {info['package']:<25} {info['desc']}")
    print("\nInstall: pip install <package>")
    print("Claude:  claude mcp add <name> -- <cmd>\n")

def install_server(name):
    if name not in REGISTRY:
        print(f"Unknown server: {name}. Run 'kenya-mcp-hub list' to see available servers.")
        sys.exit(1)
    pkg = REGISTRY[name]["package"]
    print(f"Installing {pkg}...")
    subprocess.run([sys.executable, "-m", "pip", "install", pkg])
    print(f"\nAdd to Claude: claude mcp add {name} -- {REGISTRY[name]['cmd']}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "list": list_servers()
    elif sys.argv[1] == "install" and len(sys.argv) > 2: install_server(sys.argv[2])
    else: print("Usage: kenya-mcp-hub list | kenya-mcp-hub install <server>")
