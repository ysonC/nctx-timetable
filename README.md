# README for Bus Departure Tracker Project

## Overview

This project is designed to provide real-time bus departure information from a specific bus stop, utilizing Nottingham City Transport's website. It features a Python script that fetches and displays bus departure times, a batch file to run the script, and a VBScript for silent execution.

## Files Description

- main.py: The main Python script that scrapes bus departure times using BeautifulSoup and requests.
- run.bat: A batch file that activates the Python environment and runs main.py.
- run.vbs: A VBScript that executes run.bat silently to avoid opening the Command Prompt window.

## Requirements

Python 3.x
requests and beautifulsoup4 libraries
A Windows environment for the batch and VBScript files

## Setup

Ensure Python and necessary libraries are installed.
Update main.py with the correct URL for your bus stop.
Adjust paths in run.bat and run.vbs to match your environment.
Usage
Double-click the shortcut created for run.vbs to fetch and display the bus departure times silently without opening a Command Prompt window.

## Customization

- Modify main.py to track different bus stops or additional information.
- Update the VBScript and batch file for different execution environments or parameters.

## Note

This project is designed for educational purposes and personal use. Ensure compliance with Nottingham City Transport's website terms of use when scraping data.
