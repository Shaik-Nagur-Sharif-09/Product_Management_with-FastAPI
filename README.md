# Product Management System with FastAPI
**Course Project / Assignment Submission**

### 📋 PROJECT OVERVIEW
This is a basic backend application built using **FastAPI** framework to manage product inventories. It contains proper endpoints to implement complete **CRUD (Create, Read, Update, Delete)** functions.

Instead of heavy database structures, this uses a simple custom logic inside `database.py` that handles application variables in a Python List of Dictionaries format to replicate memory mock functionalities.

---

### 💻 SYSTEM REQUIREMENTS & SETUP

**1. Clone the Project Repository:**
```bash
git clone https://github.com
cd Product_Management_with-FastAPI
```

**2. Package Configurations:**
Make sure you have python environment set up. Run the following command via terminal to fetch necessary library wrappers:
```bash
pip install fastapi uvicorn
```

**3. Execution Command:**
Execute the Uvicorn server block to trigger local deployment channel:
```bash
uvicorn app:app --reload
```

---

### 🛣️ API ENDPOINTS (ROUTING DESCRIPTIONS)

Open local instance dashboard via browser: **`http://127.0.0`**

* **`GET /`** -> Simple application heartbeat status parameter check text.
* **`GET /products`** -> Fetches full backend dataset list directly.
* **`GET /products/{name}`** -> Dynamic matching array block parameters check (Case-Insensitive).
* **`POST /products`** -> Adds structured parameters array values inside runtime instance array.
* **`PUT /products/{name}/stock`** -> Performs quick numeric balance parameter update operation checks.
* **`DELETE /products/{name}`** -> Removes target objects indexes using `.pop()` loop references.

---

### 📦 SAMPLE INITIAL DATA SET
The module auto-seeds the local instance with the following default data matrices:
1. **Galaxy S24** | Brand: Samsung | Stock: 15 units | Price: 79999.00 INR
2. **MacBook Air** | Brand: Apple | Stock: 8 units | Price: 92000.00 INR

*NOTE: Since storage structure relies completely on operational local lists execution memory frames, data modifications will fully wipe out and revert to initialization default schema states upon any server crash or manual terminal reset triggers.*
