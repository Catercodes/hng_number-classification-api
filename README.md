# Number Classification API

## 📌 Overview
This is a simple API that classifies numbers based on their mathematical properties. It determines whether a number is **Prime, Perfect, Armstrong, or Odd/Even** and also provides a fun fact about the number using the [Numbers API](http://numbersapi.com/).

## 🚀 Features
- Classifies numbers as **Prime, Perfect, Armstrong, and Odd/Even**
- Calculates the **sum of its digits**
- Fetches a **fun fact** about the number
- Handles **CORS (Cross-Origin Resource Sharing)**
- Returns responses in **JSON format**

## 📡 API Endpoint
### **GET** `/api/classify-number?number=<your_number>`

### Example Request:
```
GET https://your-app.onrender.com/api/classify-number?number=371
```

### Example Response:
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (Invalid Input):
```json
{
    "number": "abc",
    "error": true
}
```

## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### **2️⃣ Create & Activate a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run Locally**
```sh
python app.py
```
Test in your browser:
```
http://127.0.0.1:5000/api/classify-number?number=371
```

## 🌍 Deployment
### **Deploying on Render**
1. **Push to GitHub**:
   ```sh
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```
2. **Deploy to Render**:
   - Go to [Render](https://dashboard.render.com/)
   - Click **New Web Service**
   - Connect your GitHub repository
   - Set Build Command: `pip install -r requirements.txt`
   - Set Start Command: `gunicorn app:app`
   - Click **Deploy**

## 📜 License
This project is licensed under the MIT License.

---

🚀 **Enjoy using the API!** Let me know if you have any questions! 😊


