# AlbCrypt - PoC Ransomware in Python
AlbCrypt is an open-source, python ransomware Proof-of-Concept. This project is young and incomplete so there may be bugs and errors.
Minor tests have been conducted to ensure there are no syntax errors and the script runs.

**WARNING! If run, this project can encrypt files. Make sure you run it in a safe environment (e.g. virtual machine).**

## Usage

Clone repository `git clone https://github.com/zagnox/AlbCrypt.git`

Run script and specify target folder `python3 main.py -p <target path>`

Run again to decrypt files with decrypt option `python3 main.py decrypt -p <target path>`