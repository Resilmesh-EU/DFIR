#!/bin/bash
# Setup script for Docker Compose configuration
# Automatically configures network mode based on CAI_MODEL

set -e

echo "🔧 DFIR Report - Docker Setup"
echo "=============================="

# Load .env if exists
if [ -f .env ]; then
    echo "📄 Loading .env file..."
    export $(cat .env | grep -v '^#' | xargs)
fi

CAI_MODEL=${CAI_MODEL:-alias1}
echo "🤖 CAI_MODEL: $CAI_MODEL"

# Create docker-compose.override.yml if using Ollama
if [ "$CAI_MODEL" = "ollama" ]; then
    echo "✅ Configuring for Ollama..."
    cat > docker-compose.override.yml << EOF
version: '3.8'
services:
  cai-framework:
    network_mode: "container:ollama-server"
EOF
    echo "✅ Created docker-compose.override.yml with Ollama network configuration"
else
    echo "✅ Using external API configuration"
    # Remove override if exists
    if [ -f docker-compose.override.yml ]; then
        rm docker-compose.override.yml
        echo "🗑️  Removed docker-compose.override.yml (not needed for external API)"
    fi
fi

echo ""
echo "🚀 Ready to start!"
echo "   Run: docker-compose up -d"
echo ""


