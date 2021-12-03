# Task1 for LeverX courses

## About The Script

Given 2 files:
* students.json
* rooms.json

This script loads this 2 files with join them in one structure, where every room contains information about students in this room.
Output format can be:
* JSON 
* XML

## Installation
1. Clone the repo
    ```sh
    git clone https://github.com/yuramorozov01/leverx_task1.git
    cd leverx_task1/
    ```
2. Create virtual environment
    ```sh
    python3 -m venv venv
    ```
3. Activate virtual environment
    ```sh
    source venv/bin/activate
    ```
4. Install dependencies
    ```sh
    pip3 install -r requirements.txt
    ```

## Exectuting
1. Run script (format argument is case insensitive):
    * JSON output format 
    ```sh
    python3 convert.py path/to/students.json path/to/rooms.json JSON path/to/save.json
    ```
    * XML output format
    ```sh
    python3 convert.py path/to/students.xml path/to/rooms.xml XML path/to/save.xml
    ```
