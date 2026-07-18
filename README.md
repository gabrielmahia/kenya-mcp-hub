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

This hub provides discovery and documentation for AI agent protocol implementations for East Africa — MCP, A2A, and Google ADK. This hub aggregates that infrastructure for the broader developer community.

See: [mpesa-mcp PyPI](https://pypi.org/project/mpesa-mcp/) | [gabrielmahia GitHub](https://github.com/gabrielmahia)

---

*gabrielmahia.ai | MIT License | East Africa AI Infrastructure*

<!-- interconnect:v1 -->
## Part of the East Africa coordination stack

- **Install & run:** `pip install reli-cli && reli list` — 33 MCP servers on the [official MCP Registry](https://registry.modelcontextprotocol.io) under `io.github.gabrielmahia`
- **Evaluate any model on Swahili agent tasks:** [kipimo](https://github.com/gabrielmahia/kipimo) · [dataset](https://huggingface.co/datasets/gmahia/kipimo) · [leaderboard](https://huggingface.co/spaces/gmahia/kipimo-leaderboard)
- **Coordinate across servers:** [africa-coord-bus](https://pypi.org/project/africa-coord-bus/) — offline-first event bus with a built-in Kenya routing table
- **Datasets:** [huggingface.co/gmahia](https://huggingface.co/gmahia) · **Docs hub:** [nairobi-stack](https://github.com/gabrielmahia/nairobi-stack)

Model-agnostic by design: closed APIs, open-weight models, and small distilled models are all first-class citizens.
<!-- /interconnect:v1 -->
