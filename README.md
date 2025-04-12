# 📘 Assignment 2 - Network Creation Project

This project includes Jupyter Notebook analysis and Python scripts for creating and working with a network from given data sources.

---

## 🚀 Getting Started

Follow the steps below to set up and run the project on your local machine.

---

### 🧱 Set Up Virtual Environment

Create a virtual environment (only needs to be done once):

```bash
python -m venv env
```

#### ✅ Activate the Environment

- **Windows:**
  ```bash
  .\env\Scripts\activate
  ```

- **Mac/Linux:**
  ```bash
  source env/bin/activate
  ```

---

### 📥 Install Required Packages

After activating the environment, install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🧪 Run the Notebook

### 🔹 Option 1: Launch Jupyter Notebook

```bash
jupyter notebook
```

Then open the notebook file:

```
assignment2.ipynb
```

### 🔹 Option 2: Open in VS Code

1. Open the project folder in **Visual Studio Code**
2. Open `assignment2.ipynb`
3. Run cells individually or click **"Run All"**

---

## 📁 Project Structure

```
Project/
├── env/                               # Virtual environment (excluded from version control)
├── assignment2.ipynb                  # Main Jupyter notebook
├── Data for network creation (1).xlsx # Original Excel data
├── Data for network creation - Sheet1 (1).csv # Converted CSV data
├── graph.py                           # Script for graph-related operations
├── combine.py                         # Script for data combining/cleaning
├── requirements.txt                   # List of Python dependencies
└── README.md                          # Project instructions (this file)
```

> ⚠️ Make sure the `env/` folder is included in `.gitignore` to avoid pushing it to GitHub.

---

## ✅ Notes

- You can generate or update `requirements.txt` using:
  ```bash
  pip freeze > requirements.txt
  ```

- If you're using VS Code, ensure the Python interpreter is set to your virtual environment.
