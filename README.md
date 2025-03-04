# 🏀 NBA 2K25 Player Dataset - Web Scraping Project
---

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green)
![MIT License](https://img.shields.io/badge/License-MIT-green)
![Kaggle Views](https://img.shields.io/badge/Kaggle_Views-2900%2B-blue)
![Kaggle Downloads](https://img.shields.io/badge/Kaggle_Downloads-508-orange)

## 📌 Project Overview

This project focuses on **scraping high-quality and structured NBA player attributes** from the **NBA 2K25** game, sourced from the [NBA 2K Ratings Website](https://www.2kratings.com/). The dataset provides **clean, noise-free**, and **well-structured data** for analysis, modeling, and research purposes.

> 📢 The dataset has gained **2,900+ views and 508 downloads on Kaggle**!  

🔗 **Dataset Link:** [NBA 2K25 Player Complete Dataset](https://www.kaggle.com/datasets/reinerjasin/nba-2k25-player-complete-dataset)

---

## 📊 Dataset Features

The dataset includes:
- ✅ **Player Information**: Name, Team, Position, Height, Weight
- ✅ **Player Ratings**: Shooting, Dribbling, Defense, Speed, Strength
- ✅ **Player Badges**: One-hot encoded for easy use in models
- ✅ **Clean and Structured Format**: Ready for machine learning and analytics

**Example JSON Output:**
```json
{
  "Name": "LeBron James",
  "Overall": 97,
  "Position": "SF",
  "Shooting": 85,
  "Defense": 88,
  "Badges": ["Slasher", "Playmaker"]
}
```

---

## ⚙️ Tech Stack

- **Web Scraping:** Selenium, BeautifulSoup
- **Data Processing:** Pandas, NumPy
- **Automation:** Chromedriver
- **Storage Format:** CSV, JSON

---

## 🚀 Installation & Usage

### **🔹 Prerequisites**
Make sure you have:
- Python **3.x** installed  
- ChromeDriver **matching your Chrome version**  
- Required Python libraries installed  

### **🔹 Setup Instructions**
1️⃣ **Clone the repository**
```bash
git clone https://github.com/ReinerJasin/nba-2k25-player-dataset.git
cd nba-2k25-player-dataset
```
2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```
3️⃣ **Run the scraper**
```bash
python scraper.py
```
4️⃣ **Access the dataset**
- The scraped dataset will be stored in the `data/` folder as a CSV file.  
- Alternatively, you can download the latest dataset from [Kaggle](https://www.kaggle.com/datasets/reinerjasin/nba-2k25-player-complete-dataset).

---

## 🛠️ Challenges & Solutions

### ❌ **Challenge: Data Retrieval Failures**
- Some requests to the website failed, even with correct URLs.

### ✅ **Solution:**
- Implemented a **validation system** that detects missing data and **automatically retries** scraping.
- Built-in **error handling** prevents script crashes.

---

## 🔍 Use Cases & Applications

📌 **How can you use this dataset?**
- 🏀 **Player Performance Analysis** (Predicting in-game player potential)
- 📊 **Data Visualization** (Comparing players over different seasons)
- 🧠 **Machine Learning Models** (Predicting NBA 2K player rating changes)
- 🤖 **AI Sports Analytics** (Training AI for basketball insights)

---

## 🎯 Future Improvements
- 📈 **Scraping historical NBA 2K ratings** to analyze rating trends.
- 🔄 **Automated dataset updates** for fresh player ratings.
- 🏆 **Expanding data sources** to include real-life NBA stats.

---

## 🤝 Contributions

Contributions are welcome! To contribute:
1. **Fork the repository**  
2. **Create a new branch**  
3. **Make changes and submit a PR**  

Check out [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 📢 Acknowledgments

Special thanks to **NBA 2K Ratings Website** for providing the source data.  
If you find this project useful, don’t forget to **⭐ star the repository**! 🚀

---
