# 🛡️ Smart Self-Healing Material for Defence Gear

An AI-powered web application that predicts the healing efficiency of self-healing materials used in defence gear based on operating conditions such as temperature, pressure, crack size, and material type. The system uses a Machine Learning model to estimate healing performance and visually simulates the crack healing process over time.

---

# 📖 Project Overview

Self-healing materials have the potential to improve the durability and reliability of military protective equipment by automatically repairing minor damage. This project demonstrates how Artificial Intelligence can be used to predict the healing efficiency of different self-healing materials under varying environmental conditions.

The application allows users to select a material, enter operating parameters, and receive an instant prediction of healing efficiency along with a graphical visualization of crack reduction over time.

---

# 🎯 Objectives

- Predict the healing efficiency of self-healing materials using Machine Learning.
- Analyze the effect of temperature, pressure, crack size, and material type.
- Classify crack severity based on crack size.
- Detect burn conditions based on material temperature limits.
- Simulate the crack healing process using graphical visualization.
- Provide an easy-to-use web interface for testing different scenarios.

---

# ✨ Features

- 🤖 Machine Learning-based healing prediction
- 🌡️ Temperature and burn condition analysis
- 📏 Crack severity classification (Low, Medium, High)
- 🛡️ Material-specific validation rules
- 📊 Healing process visualization
- 📈 Time-based crack reduction graph
- 💻 Interactive web interface built using Gradio

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

├── app.py
├── healing_data_600_realistic.csv
├── healing_model.pkl
├── requirements.txt
├── README.md
├── Images/
├── Documentation/
└── Dataset/
```

---

# ⚙️ Machine Learning Workflow

1. Load the healing dataset.
2. Split the dataset into training and testing sets.
3. Train a Random Forest Regressor model.
4. Evaluate model performance using R² Score and Mean Absolute Error (MAE).
5. Save the trained model.
6. Accept user inputs through the Gradio interface.
7. Predict healing efficiency.
8. Generate a healing simulation graph.
9. Display prediction results to the user.

---

# 🧪 Input Parameters

- Temperature (°C)
- Pressure (atm)
- Crack Size (mm)
- Material Type

Supported Materials:

- Epoxy
- Nylon
- Elastomer
- Ceramic
- Carbon Fiber

---

# 📊 Output

The application provides:

- Material information
- Crack severity
- Burn status
- Predicted healing efficiency
- Estimated healing time
- Crack healing simulation graph

---

# 📈 Machine Learning Model

**Algorithm Used:** Random Forest Regressor

**Evaluation Metrics:**

- R² Score
- Mean Absolute Error (MAE)

The trained model is saved using Joblib and reused during prediction.

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/asreethamekala/Smart-Self-Healing-Material-Defence-Gear.git
```

Move into the project folder

```bash
cd Smart-Self-Healing-Material-Defence-Gear
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

---

# 📸 Screenshots

Screenshots of the application interface and prediction results will be added here.

---

# 🔮 Future Enhancements

- Deep Learning-based prediction models
- IoT sensor integration for real-time monitoring
- Cloud database support
- Mobile application integration
- Advanced material analysis
- Real-time defence equipment monitoring dashboard

---

# 👩‍💻 Author

**Mekala Asreetha**

B.Tech (Artificial Intelligence and Machine Learning)

Aspiring Data Analyst | Machine Learning Enthusiast

---

# 📄 License

This project is licensed under the MIT License.
