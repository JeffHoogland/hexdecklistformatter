#!/bin/bash
rm -f ui_*.py
rm -f ui_*.pyc
pyside-uic formatter.ui > ui_Formatter.py
