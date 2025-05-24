# 🔄 Real-time Data Transformation with PySpark Structured Streaming

This project demonstrates how to simulate and process real-time data streams using **PySpark Structured Streaming** in a beginner-friendly environment.

---

## 📌 What It Does
- Simulates a real-time data stream using the built-in `rate` source
- Joins the streaming data with a static DataFrame (user data)
- Performs transformations and aggregations in real time
- Outputs the results (e.g. average age per country) to the console

---

## 🚀 Technologies Used
- Python 3.10+
- Apache Spark 3.4.1
- PySpark
- Google Colab (optional, for testing)

---

## 📂 Files
- `structured_streaming.py` - Main script
- `sample_streaming_data.txt` - 50 records for simulation
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore rules

---

## 📊 Sample Output
```
+--------+------------------+
|country |avg_age           |
+--------+------------------+
|USA     |31.0              |
|Canada  |27.0              |
|UK      |40.0              |
+--------+------------------+
```

---

## ✨ How to Run
1. Ensure Java and Spark are installed
2. Optional: start a socket listener
   ```bash
   ncat -lk 9999
   ```
3. Run the script:
   ```bash
   python structured_streaming.py
   ```

---

## 🌟 Author
Created by Pavlik as part of a hands-on learning journey into data streaming and PySpark fundamentals.
