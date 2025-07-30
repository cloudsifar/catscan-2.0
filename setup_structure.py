#!/usr/bin/env python3
"""
Setup script to create the CatSCAN modular directory structure
Run this from your project root directory
"""

import os
from pathlib import Path

def create_structure():
    """Create the complete directory structure for CatSCAN"""
    
    # Define the structure
    structure = {
        "src/catscan": [
            "__init__.py",
            "__main__.py",
            "main.py",
            "config.py",
            "exceptions.py"
        ],
        "src/catscan/auth": [
            "__init__.py",
            "keyring_auth.py",
            "config_auth.py",
            "validators.py"
        ],
        "src/catscan/api": [
            "__init__.py",
            "client.py",
            "terraform.py",
            "rate_limiter.py"
        ],
        "src/catscan/scanner": [
            "__init__.py",
            "workspace.py",
            "state.py",
            "resources.py"
        ],
        "src/catscan/storage": [
            "__init__.py",
            "history.py",
            "config.py"
        ],
        "src/catscan/ui": [
            "__init__.py",
            "console.py",
            "panels.py",
            "tables.py",
            "menus.py",
            "rich_ui.py",
            "curses_ui.py"
        ],
        "src/catscan/utils": [
            "__init__.py",
            "platform.py",
            "keyboard.py",
            "logging.py"
        ]
    }
    
    # Create directories and files
    for directory, files in structure.items():
        # Create directory
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {directory}")
        
        # Create files
        for file in files:
            filepath = Path(directory) / file
            if not filepath.exists():
                filepath.touch()
                
                # Add basic module docstring
                if file == "__init__.py":
                    docstring = f'"""{directory.replace("src/catscan/", "").replace("/", ".")} package"""\n'
                else:
                    module_name = file.replace(".py", "")
                    docstring = f'"""\n{module_name} module\n\nThis module contains {module_name} functionality.\n"""\n'
                
                # Write with UTF-8 encoding
                filepath.write_text(docstring, encoding='utf-8')
                print(f"  ✓ Created file: {file}")
    
    # Create root level files
    root_files = {
        "pyproject.toml": '''[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "catscan"
version = "2.0.0"
description = "Terraform Infrastructure Scanner"
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
    "requests>=2.28.0",
    "rich>=13.0.0",
    "keyring>=23.0.0",
]

[project.scripts]
catscan = "catscan.main:main"
''',
        "setup.py": '''from setuptools import setup, find_packages

setup(
    name="catscan",
    version="2.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "rich>=13.0.0",
        "keyring>=23.0.0",
    ],
    entry_points={
        "console_scripts": [
            "catscan=catscan.main:main",
        ],
    },
)
''',
        "requirements.txt": '''requests>=2.28.0
rich>=13.0.0
keyring>=23.0.0
''',
        "README.md": '''# CatSCAN - Terraform Infrastructure Scanner

CatSCAN is a secure, high-performance tool for scanning and analyzing Terraform Cloud infrastructure.

## Features

- Secure token storage with system keyring
- Parallel processing with connection pooling
- Detailed resource inventory and history
- Cross-platform support (Windows/Linux/Mac)
- Beautiful terminal UI with Rich and Curses

## Installation

```bash
pip install -e .
```

## Usage

```bash
catscan
```

## Development

```bash
# Install in development mode
pip install -e .

# Run tests
pytest

# Run with debug logging
CATSCAN_DEBUG=true catscan
```
''',
        ".gitignore": '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
ENV/
env/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# CatSCAN specific
.catscan_config.json
.catscan_history/

# OS
.DS_Store
Thumbs.db
'''
    }
    
    for filename, content in root_files.items():
        filepath = Path(filename)
        if not filepath.exists():
            # Write with UTF-8 encoding
            filepath.write_text(content, encoding='utf-8')
            print(f"✓ Created {filename}")
        else:
            print(f"⚠️  {filename} already exists, skipping")
    
    print("\n✅ Directory structure created successfully!")
    print("\nNext steps:")
    print("1. Move code sections from the monolith to their respective modules")
    print("2. Update imports throughout the codebase")
    print("3. Run 'pip install -e .' to install in development mode")
    print("4. Test with 'python -m catscan' or just 'catscan'")

if __name__ == "__main__":
    create_structure()