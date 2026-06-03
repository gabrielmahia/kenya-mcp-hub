# 🔌 Kenya MCP Hub

**The unified registry and developer gateway for East Africa's Model Context Protocol (MCP) servers.**

Every AI agent protocol server built for East Africa, in one place. Connect any LLM (Claude, GPT-4, Gemini) to Kenya's digital infrastructure in minutes.

## Available MCP Servers

| Server | Domain | PyPI | Description |
|--------|--------|------|-------------|
| [mpesa-mcp](https://github.com/gabrielmahia/mpesa-mcp) | 💰 FinTech | `pip install mpesa-mcp` | M-PESA Daraja API as MCP tools |
| [wapimaji-mcp](https://github.com/gabrielmahia/wapimaji-mcp) | 💧 Water | `pip install wapimaji-mcp` | Kenya water infrastructure data |
| [swahili-health-mcp](https://github.com/gabrielmahia/swahili-health-mcp) | 🏥 Health | `pip install swahili-health-mcp` | Kenya DHIS2 health data |
| [kenya-legal-rag](https://github.com/gabrielmahia/kenya-legal-rag) | ⚖️ Legal | `pip install kenya-legal-rag` | Kenya legal documents RAG |

## Quickstart

```bash
# Install any server
pip install mpesa-mcp

# Add to Claude Code
claude mcp add mpesa -- mpesa-mcp
claude mcp add water -- wapimaji-mcp
claude mcp add health -- swahili-health-mcp

# Or add all at once
claude mcp add mpesa -- mpesa-mcp && claude mcp add water -- wapimaji-mcp
```

## For Developers: Add Your Server

This hub welcomes East African MCP servers. Open a PR with:
1. Server name and PyPI package name
2. Domain and description
3. Example tool calls

## Strategic Context

Gabriel Mahia is the first documented engineer to implement all three major AI agent protocols (MCP, A2A, Google ADK) for East Africa. This hub aggregates that infrastructure for the broader developer community.

See: [mpesa-mcp PyPI](https://pypi.org/project/mpesa-mcp/) | [gabrielmahia GitHub](https://github.com/gabrielmahia)

---

*gabrielmahia.ai | MIT License | East Africa AI Infrastructure*
