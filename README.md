# Daily Creed

A Python application that displays daily creed popups extracted from a Word document.

## Features

- Extracts creeds from a Word document
- Displays daily creed popups
- Runs as a daemon in the background

## Installation

1. Install dependencies:
   ```
   pip install python-docx schedule
   ```

2. Run the extraction script:
   ```
   python extract_creeds.py
   ```

3. Run the daemon:
   ```
   python creed_popup_daemon.py
   ```

## License

MIT