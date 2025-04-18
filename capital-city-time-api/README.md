# Flask Capital City Time API

This is a simple Flask-based API deployed on a Google Cloud Platform VM that returns the **current local time** and **UTC offset** for a specified **capital city**, with **token-based authorization**.

---

## 👤 Author
Jessica Xiong

---

## 🗂 GitHub Repo Files
- `app.py` – main Flask app file
- `README.md` – this documentation, which contains "IP Address of my working API" and " Documentation on how to call my API"

---

##  Deployed API URL

**Public IP Address:** `http://34.10.29.238:5001`



##  API Authentication
All endpoints require a Bearer token in the `Authorization` header.

**Token:**
```
supersecrettoken123
```

---

##  Supported Capital Cities
You can pass the following capital cities (case-sensitive) as query parameters:
- `Tokyo`
- `Washington`
- `London`
- `Paris`
- `Beijing`
- `Ottawa`
- `Canberra`

---

##  Public API Endpoint (Hosted on GCP)
```
http://34.10.29.238:5001/api/time?city=Tokyo
```

---

##  How to Call the API

###  Sample `curl` Request
```bash
curl -H "Authorization: Bearer supersecrettoken123" \
     "http://34.10.29.238:5001/api/time?city=Tokyo"
```

### ✅ Successful Response
```json
{
  "city": "Tokyo",
  "local_time": "2025-04-19 04:26:00",
  "utc_offset": "UTC+09:00"
}
```

### ❌ Unauthorized (Missing/Invalid Token)
```json
{
  "error": "Unauthorized – provide a valid token"
}
```

### ❌ City Not Found
```json
{
  "error": "City 'Madrid' not found in database"
}
```

---

##  How to Run the App on Your VM

1. SSH into your GCP VM
2. Activate your virtual environment:
```bash
source myenv/bin/activate
```
3. Run the app:
```bash
python3 app.py
```





