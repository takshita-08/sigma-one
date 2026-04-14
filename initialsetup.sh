#!/bin/bash

set -e

echo "🚀 Starting project setup..."

# -----------------------------
# 1. Check Python installation
# -----------------------------
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 not found. Please install manually."
    exit 1
else
    echo "✅ Python3 already installed"
fi

# -----------------------------
# 2. Create virtual environment
# -----------------------------
echo "📦 Creating virtual environment..."
python3 -m venv venv

# -----------------------------
# 3. Set platform-specific paths
# -----------------------------
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    ACTIVATE_SCRIPT="venv/Scripts/activate"
    PYTHON_BIN="venv/Scripts/python.exe"
    PIP_BIN="venv/Scripts/pip.exe"
else
    ACTIVATE_SCRIPT="venv/bin/activate"
    PYTHON_BIN="venv/bin/python"
    PIP_BIN="venv/bin/pip"
fi

# -----------------------------
# 4. Activate venv (only for bash environments)
# -----------------------------
echo "🔄 Activating virtual environment..."
source "$ACTIVATE_SCRIPT"

# -----------------------------
# 5. Upgrade pip
# -----------------------------
echo "⬆️ Upgrading pip..."
"$PYTHON_BIN" -m pip install --upgrade pip

# -----------------------------
# 6. Install dependencies
# -----------------------------
if [ -f "requirements.txt" ]; then
    echo "📥 Installing dependencies..."
    "$PIP_BIN" install -r requirements.txt
else
    echo "📥 Installing default dependencies..."
    "$PIP_BIN" install pytest playwright pytest-playwright
fi

# -----------------------------
# 7. Install Playwright browsers
# -----------------------------
echo "🌐 Installing Playwright browsers..."
"$PYTHON_BIN" -m playwright install

# Linux only (safe fallback)
"$PYTHON_BIN" -m playwright install-deps || true

# -----------------------------
# 8. Verify
# -----------------------------
echo "🔍 Verifying setup..."
"$PYTHON_BIN" --version
"$PIP_BIN" --version
"$PYTHON_BIN" -m pytest --version
"$PYTHON_BIN" -m playwright --version

echo "✅ Setup completed!"