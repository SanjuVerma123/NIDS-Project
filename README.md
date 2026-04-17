# 🔒 Network Intrusion Detection System (NIDS)

## 📌 Problem Statement
The goal of this project is to **detect malicious network traffic (intrusions/attacks) using Machine Learning**.

### 🎯 Business Impact
- Prevent cyber attacks  
- Reduce financial loss  
- Improve system security  

---

## 📂 Dataset
We use the **NSL-KDD dataset**, an improved version of the KDD’99 dataset, widely used for intrusion detection research.

Files:
- `KDDTrain+.txt` → Training data  
- `KDDTest+.txt` → Testing data  

---

## ⚙️ Tech Stack
- **Python** (NumPy, Pandas, Matplotlib, Seaborn)  
- **Scikit-learn** (preprocessing, evaluation)  
- **Imbalanced-learn (SMOTE)** for handling class imbalance  
- **XGBoost** for classification  
- **Streamlit** for deployment  

---

## 🚀 Project Workflow
1. **Data Cleaning**  
   - Handle nulls, duplicates, outliers  
   - Convert labels into binary (Normal vs Attack)  

2. **Exploratory Data Analysis (EDA)**  
   - Histograms, count plots by protocol, service, guest login  
   - Visualize attack distribution  

3. **Encoding & Preprocessing**  
   - Label encoding for categorical features  
   - SMOTE for balancing classes  
   - StandardScaler for normalization  

4. **Model Training**  
   - XGBoost classifier (`eval_metric='logloss'`)  
   - Train/test split (80/20)  

5. **Evaluation**  
   - Accuracy, Precision, Recall, F1-score  
   - ROC Curve & AUC  
   - Feature importance visualization  

6. **Deployment**  
   - Streamlit app with interactive UI  
   - Single prediction & batch prediction (CSV upload)  
   - Feature importance chart  

---

## 📊 Results
- Accuracy: ~99.96%  
- ROC AUC: 1.0  
- Top features: `src_bytes`, `protocol_type`, etc.  

---

## 🖥️ Streamlit App
### Run Locally
```bash
streamlit run app.py
