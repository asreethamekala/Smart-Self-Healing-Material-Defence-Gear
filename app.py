import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

import gradio as gr

# -----------------------------
# LOAD CSV DATASET
# -----------------------------
df = pd.read_csv("Dataset/healing_data_600_realistic.csv")
# VERIFY DATASET
print(df.head())
print("DATA SIZE:", len(df))

# -----------------------------
# FEATURES & TARGET
# -----------------------------
X = df.drop("healing_efficiency", axis=1)
y = df["healing_efficiency"]

# -----------------------------
# TRAIN-TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# MODEL TRAINING
# -----------------------------
model = RandomForestRegressor()
model.fit(X_train, y_train)

# -----------------------------
# MODEL EVALUATION
# -----------------------------
y_pred = model.predict(X_test)

print("\nMODEL PERFORMANCE")
print("R2 Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))

# -----------------------------
# SAVE MODEL
# -----------------------------
joblib.dump(model, "healing_model.pkl")

# -----------------------------
# MATERIAL DATABASE
# -----------------------------
materials = {
    "Epoxy": {"code": 0, "max_temp": 180},
    "Nylon": {"code": 1, "max_temp": 220},
    "Elastomer": {"code": 2, "max_temp": 150},
    "Ceramic": {"code": 3, "max_temp": 1000},
    "Carbon Fiber": {"code": 4, "max_temp": 300}
}

# -----------------------------
# MAIN FUNCTION
# -----------------------------
def smart_system(temp, pressure, crack, polymer):

    poly_info = materials[polymer]

    # Burn check
    burn = 1 if temp > poly_info["max_temp"] else 0

    # Safety check
    if temp > 350:
        return "⚠️ Extreme temperature! Material failure possible", None

    # Severity
    if crack < 1:
        severity = "LOW"
    elif crack < 2:
        severity = "MEDIUM"
    else:
        severity = "HIGH"

    # Healing time
    healing_time = round(crack * 2, 2)

    # Non-healable cases
    if polymer == "Ceramic":
        return "Ceramic → Cannot heal (brittle)", None

    if polymer == "Carbon Fiber":
        return "Carbon Fiber → Cannot heal (fiber break)", None

    if polymer == "Nylon" and burn == 1:
        return "Nylon burnt → Cannot heal", None

    # Prediction
    input_data = np.array([[temp, pressure, crack, poly_info["code"], burn]])
    healing = model.predict(input_data)[0]

    # -----------------------------
    # GRAPH
    # -----------------------------
    plt.figure()

    time = np.linspace(0, 10, 50)
    healing_factor = healing / 100

    crack_progress = crack * np.exp(-healing_factor * time)

    plt.plot(time, crack_progress, label="Crack Healing")
    plt.scatter(0, crack)

    plt.xlabel("Time (minutes)")
    plt.ylabel("Crack Size (mm)")
    plt.title("Self-Healing Process Over Time")

    plt.grid()
    plt.legend()

    graph_path = "graph.png"
    plt.savefig(graph_path)
    plt.close()

    # -----------------------------
    # OUTPUT
    # -----------------------------
    output_text = f"""
========================================
🛡️ SMART DEFENCE SYSTEM
========================================

📏 Crack Size : {crack:.2f} mm
🚨 Severity   : {severity}

🧪 Material   : {polymer}
🌡️ Temp       : {temp} °C
ضغط Pressure  : {pressure} atm
🔥 Burn       : {'YES' if burn else 'NO'}

🤖 Healing    : {healing:.2f}%
⏱️ Heal Time  : {healing_time} mins

========================================
"""

    return output_text, graph_path

# -----------------------------
# UI
# -----------------------------
interface = gr.Interface(
    fn=smart_system,
    inputs=[
        gr.Slider(20, 350, label="Temperature (°C)"),
        gr.Slider(1, 5, label="Pressure (atm)"),
        gr.Slider(0.1, 3.5, label="Crack Size (mm)"),
        gr.Dropdown(
            ["Epoxy", "Nylon", "Elastomer", "Ceramic", "Carbon Fiber"],
            label="Material"
        )
    ],
    outputs=["text", "image"],
    title="🛡️ Smart Self-Healing Defence System",
    description="AI-based healing prediction with time-based simulation"
)

interface.launch(share=False)