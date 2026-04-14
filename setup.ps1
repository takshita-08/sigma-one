Write-Host "Starting project setup..."

# -----------------------------
# 1. Check Python installation
# -----------------------------
try {
    python --version | Out-Null
    Write-Host "Python is installed"
} catch {
    Write-Host "Python not found. Please install Python and re-run."
    exit 1
}

# -----------------------------
# 2. Create virtual environment
# -----------------------------
Write-Host "Creating virtual environment..."
python -m venv venv

# -----------------------------
# 3. Activate virtual environment
# -----------------------------
Write-Host "Activating virtual environment..."

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.\venv\Scripts\Activate.ps1

# -----------------------------
# 4. Upgrade pip
# -----------------------------
Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

# -----------------------------
# 5. Install dependencies
# -----------------------------
if (Test-Path "requirements.txt") {
    Write-Host "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
}
else {
    Write-Host "Installing default dependencies..."
    pip install pytest playwright pytest-playwright
}

# -----------------------------
# 6. Install Playwright browsers
# -----------------------------
Write-Host "Installing Playwright browsers..."
python -m playwright install

# -----------------------------
# 7. Verify installation
# -----------------------------
Write-Host "Verifying setup..."

python --version
pip --version
pytest --version
python -m playwright --version

Write-Host "Setup completed successfully!"

# -----------------------------
# 8. Run tests (optional)
# -----------------------------
if (Test-Path "tests") {
    Write-Host "Running tests..."
    pytest
}
else {
    Write-Host "No tests folder found. Skipping test run."
}

Write-Host "You're ready to go!"
Write-Host "Activate later using: .\venv\Scripts\Activate.ps1"