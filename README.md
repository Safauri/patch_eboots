# GTA V EBOOT Patcher

## Overview
A simple script for patching EBOOT files in ELF format by replacing predefined values.

## Requirements
- Python 3.x (no external dependencies)

## Usage
1. Drag and drop an ELF file onto the script.
2. The script scans for predefined values and applies replacements.
3. Patched results are displayed in the terminal.

### Converting to an Executable
To package the script as a `.exe` for easier use:
```bash
pyinstaller --onefile main.py
```
