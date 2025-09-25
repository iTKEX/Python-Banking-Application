# 🏦 Python Bank Application

**Python Bank Application** is a _lightweight_, _menu-driven_ banking application for the **terminal**. It stores data in **CSV** files and
models core retail-banking flows:

- Account creation & authentication
- Checking and Savings accounts
- Deposits & withdrawals (with overdraft handling)
- Peer-to-peer transfers
- Transaction history logging

---

## 📁 Project Structure

```
Python Bank Application/
├── assets/
│ └── bank.csv
│ └── history.csv
├── banking.py
└── README.md
```

---

## ⚙️ Installation & Setup

1. Make sure you have **Python 3.10+** installed.

2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/python-bank-app.git
   cd python-bank-app
   ```

3. Run the application:
   ```bash
   python3 banking.py
   ```

---

## ✨ Features

- Persistent data storage in CSV files (no external DB required).
- Checking and Savings account support.
- Deposits, withdrawals, internal and external transfers.
- Overdraft handling: $35 fee applied, account disabled after 2 overdrafts.
- Transaction history logs with details.
- Menu-driven text interface.

---

## 🛠️ Technologies Used

- **Python 3.12**
- **CSV module**
- **Datetime module**
- **Terminal I/O**

---

## 📊 Application Functionality

| Feature                     | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| **Sign Up / Sign In**        | Create a new customer account or log into an existing one.                  |
| **Checking & Savings**       | Support for both account types, user chooses at setup.                      |
| **Deposit**                  | Add money to chosen account, logs transaction.                              |
| **Withdraw**                 | Withdraw money (max $100 per transaction). Overdraft fees apply if balance ≤ 0. |
| **Internal Transfer**        | Transfer money between own Checking and Savings accounts.                   |
| **External Transfer**        | Send money to another customer’s account (savings/checking).                |
| **Transaction Logs**         | Print full history or details of a single transaction.                      |
| **Overdraft Handling**       | $35 fee per overdraft, account deactivated after 2 overdrafts.              |

---

## 🚀 Challenges & Key Takeaways

- **User Experience** → Menu-driven design balanced simplicity with enough features. 
- **Data Persistence** → Managing flat CSVs required clean read/write handling.  
- **Error Handling** → Input validation was critical to avoid crashes and invalid data.  
- **Takeaway** → Breaking code into modular classes (`Customer`, `Bank`, `History`, `Transactions`) kept things organized.  

---

## 🧊 IceBox Features

- **🔐 Password Encryption** → Replace plain-text storage with hashing.  
- **🎨 Colorful CLI** → Use libraries for a better terminal UI.  

---

## 📚 References & Data Sources

#### Saudi Digital Academy: [SDA Website](https://www.google.com)

#### General Assembly: [GA Website](https://generalassemb.ly/)
