# 🛡️ Smart Self-Healing Material for Defence Gear

An AI-powered web application that predicts the healing efficiency of self-healing materials used in defence gear based on environmental and material conditions. The system leverages Machine Learning to estimate healing performance and provides a graphical simulation of the crack healing process over time.

---

# 📖 Project Overview

Self-healing materials are an emerging technology designed to automatically repair minor damage, improving the durability and lifespan of defence equipment. This project demonstrates how Machine Learning can be used to predict the healing efficiency of different materials based on operating conditions such as temperature, pressure, crack size, and material type.

The application features an interactive web interface built with **Gradio**, allowing users to test different scenarios and visualize the healing process.

---

# 🎯 Objectives

- Predict the healing efficiency of self-healing materials using Machine Learning.
- Analyze the impact of temperature, pressure, crack size, and material type.
- Classify crack severity into Low, Medium, and High.
- Detect burn conditions based on material temperature limits.
- Simulate the crack healing process through graphical visualization.
- Provide an easy-to-use web interface for experimentation.

---

# ✨ Features

- 🤖 AI-based healing efficiency prediction
- 🌡️ Temperature and burn condition analysis
- 📏 Crack severity classification
- 🛡️ Material-specific validation rules
- 📊 Healing process visualization
- 📈 Time-based crack reduction graph
- 💻 Interactive Gradio web interface

---

# 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Random Forest Regressor
- Joblib
- Gradio

---

# 📂 Project Structure

```
Smart-Self-Healing-Material-Defence-Gear/

│── app.py
│── healing_data_600_realistic.csv
│── requirements.txt
│── README.md
│── LICENSE
│── .gitignore
```

---

# ⚙️ Machine Learning Workflow

1. Load the dataset.
2. Split the data into training and testing sets.
3. Train a Random Forest Regressor model.
4. Evaluate model performance using R² Score and Mean Absolute Error (MAE).
5. Predict healing efficiency based on user inputs.
6. Generate a crack healing simulation graph.
7. Display results through the Gradio interface.

---

# 🧪 Input Parameters

- Temperature (°C)
- Pressure (atm)
- Crack Size (mm)
- Material Type

### Supported Materials

- Epoxy
- Nylon
- Elastomer
- Ceramic
- Carbon Fiber

---

# 📊 Output

The application displays:

- Material Information
- Crack Severity
- Burn Status
- Predicted Healing Efficiency
- Estimated Healing Time
- Crack Healing Simulation Graph

---

# 📈 Machine Learning Model

**Algorithm Used**

- Random Forest Regressor

### Model Performance

| Metric | Value |
|---------|-------|
| Dataset Size | 600 Records |
| R² Score | 0.94 |
| Mean Absolute Error (MAE) | 2.68 |

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/asreethamekala/Smart-Self-Healing-Material-Defence-Gear.git
```

## Navigate to the Project Folder

```bash
cd Smart-Self-Healing-Material-Defence-Gear
```

## Install Required Libraries

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

The application will launch locally using Gradio.

---

# 📸 Application Screenshots

> Screenshots of the application interface, prediction results, and healing simulation graph will be added soon.

---

# 🔮 Future Enhancements

- Deep Learning-based prediction models
- Real-time IoT sensor integration
- Cloud database support
- Mobile application
- Advanced material analysis
- Real-time defence equipment monitoring dashboard
- Model optimization using ensemble techniques

---

# 👩‍💻 Author

**Mekala Asreetha**

B.Tech – Artificial Intelligence and Machine Learning

Aspiring Data Analyst | Machine Learning Enthusiast

GitHub: https://github.com/asreethamekala

---

# 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ If you found this project useful, consider giving it a Star!
