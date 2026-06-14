FROM python:3.12-slim
LABEL org.opencontainers.image.source="https://github.com/gabrielmahia/kenya-mcp-hub"
RUN pip install --no-cache-dir kenya-mcp-hub
CMD ["kenya-mcp-hub"]
