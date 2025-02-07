# Virtual Environment Setup Guide

## Introduction
This guide provides step-by-step instructions to install and use `virtualenv` for managing isolated Python environments.

## 1. Install `virtualenv`
Run the following command to install `virtualenv` globally:
```bash
pip install virtualenv
```

Ensure `pip` is installed and updated:
```bash
python -m ensurepip --default-pip
python -m pip install --upgrade pip
```

## 2. Create a Virtual Environment
Navigate to your project directory and create a virtual environment:
```bash
python -m venv venv  # Creates a virtual environment named 'venv'
```

## 3. Activate the Virtual Environment
### 🔹 On Windows (CMD or PowerShell):
```cmd
venv\Scripts\activate
```

### 🔹 On macOS/Linux:
```bash
source venv/bin/activate
```

## 4. Install Dependencies in Virtual Environment
After activation, install dependencies inside the environment:
```bash
pip install -r requirements.txt  # Install from a requirements file (if available)
```

## 5. Deactivate the Virtual Environment
To exit the virtual environment, simply run:
```bash
deactivate
```

## 6. Delete a Virtual Environment (If Needed)
If you need to remove a virtual environment, delete its folder:
```bash
rm -rf venv  # Linux/macOS
rd /s /q venv  # Windows
```

## 7. Verify Virtual Environment is Activated
Check if the virtual environment is active:
```bash
which python  # Linux/macOS
where python   # Windows
```
The output should point to the `venv` folder.

---
### 🎯 Now, you're ready to work in a clean Python environment! 🚀

