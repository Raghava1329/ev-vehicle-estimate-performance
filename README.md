# Intelligent Electric Vehicle Analytics using AWS and Machine Learning 🚗⚡

## Project Overview

This project aims to analyze electric vehicle performance and safety using machine learning, addressing the rising concerns over battery-related fire incidents in electric scooters. The solution leverages AWS infrastructure to create a secure, scalable, and cloud-based analytics pipeline.

## 👨‍💻 Team Members – Code Freaks
- Malla Madhavi Sri Lakshmi  
- Rayi Navya  
- Mycharla Deepak  
- Dasireddy Chaitanya  
- Devupalli Pardava Krishnam Naidu  
- Avula Ragavendra  

---

## 🔍 Problem Statement

Increasing fire incidents in electric scooters have raised safety concerns. The project investigates key performance metrics—like battery capacity, range, motor type, etc.—and develops predictive models to assess safety and reliability of electric vehicles.

---

## 🧠 ML Pipeline

### 🔹 Feature Engineering
- Selected Features:
  - Motor Type (kW)
  - Battery Capacity (kWh)
  - Battery Power (W)
  - Range
  - Acceleration
  - Load Capacity
  - Satisfaction Rate

- Transformation & Encoding applied to:
  - Range buckets
  - Categorical to numerical conversion (where necessary)

- Final Dataset: `team-14.csv`

### 🔹 Model Development
- **Linear Regression**
- **Decision Tree Regressor**
- **Random Forest Regressor**

### 📊 Evaluation
- Compared models based on prediction accuracy.
- Random Forest Regressor yielded the most accurate results.

---

## ☁️ AWS Infrastructure

### 🔸 VPC Setup
- Public Subnets configured under VPC `team-14`
- Routing via `team-14-rtb-public`
- Internet Gateway for external access

### 🔸 Services Used
- **EC2**: For computing and notebook hosting  
- **S3**: For dataset and model storage  
- **IAM**: Managed access policies  
- **VPC**: Isolated cloud network  
- **ALB**: Load balancing (future scope)  

---

## 🔬 Results & Insights

- AI-powered analytics helped identify key contributors to EV fire risks.
- Recommendations:
  - Use of higher-quality materials
  - More rigorous quality control in manufacturing

---

## 📁 Files

- `data`: Synthetic dataset generated using feature engineering
- `notebook.ipynb`: Jupyter Notebook with model training and evaluation
- `README.md`: Project documentation

---

## 📚 References

- [India Today – Ola Electric Fire Incident](https://www.indiatoday.in/india/story/ola-electric-scooter-recall-fire-incident-battery-system-1941302-2022-04-24)  
- [Cartoq – Fire Incident in Bhopal](https://www.cartoq.com/ola-s1-pro-fire-in-bhopal/)  
- [Moneycontrol – EV Safety Concerns](https://www.moneycontrol.com/news/)  
- [Outlook India – Business Reports on EVs](https://www.outlookindia.com/)

---

## 🚀 Tech Stack
- **Python**, **Pandas**, **Scikit-learn**
- **AWS**: EC2, S3, VPC, IAM
- **Jupyter Notebook**, **CSV**, **Matplotlib**

---

## 📝 Conclusion

The project successfully demonstrates how ML and cloud computing can be combined to derive actionable insights into electric vehicle safety. It lays the foundation for future developments in real-time monitoring and predictive maintenance in the EV industry.

