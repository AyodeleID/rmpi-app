<div align="center">

# 🌍 Real-Time Migration Pressure Index (RMPI)

### Interactive Intelligence Dashboard for Migration Dynamics

[![Python](https://img.shields.io/badge/Python-Data%20App-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Live%20Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Status](https://img.shields.io/badge/Status-Active-16a34a?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-0f766e?style=for-the-badge)](#)

<br/>

> **RMPI** transforms multi-dimensional migration drivers into a single, interpretable pressure score.  
> Built for analysts, researchers, and policymakers who need **fast**, **visual**, and **actionable** migration insights.

</div>

---

## 🧭 What is RMPI?

The **Real-Time Migration Pressure Index (RMPI)** is a Streamlit-based analytical dashboard that tracks migration pressure across countries and regions by combining:

- 📈 **Economic indicators** (livelihood stress, unemployment proxies, inflation-related pressure)
- 🌦️ **Environmental indicators** (climate shocks, environmental stress signals)
- 🧩 **Social indicators** (instability, vulnerability, social pressure metrics)

These are aggregated into a single composite score to support monitoring and decision-making.

---

## ✨ Core Experience

<table>
<tr>
<td width="50%">

### 🗺️ Spatial View
Interactive map showing RMPI intensity by country/region.

</td>
<td width="50%">

### 📉 Temporal View
Trend lines to monitor how migration pressure evolves over time.

</td>
</tr>
<tr>
<td width="50%">

### 🎛️ Scenario Controls
Dynamic filters for geography, time windows, and indicator weights.

</td>
<td width="50%">

### 📦 Exportability
Download processed data for policy notes, reports, and modeling.

</td>
</tr>
</table>

---

## ⚙️ Feature Breakdown

| Module | Function | Why It Matters |
|---|---|---|
| **Interactive Map** | Displays RMPI geographically | Rapid hotspot identification |
| **Time-Series Charts** | Shows pressure trajectories | Detects shifts and turning points |
| **Weight Sliders / Filters** | Adjusts indicator contribution | Enables scenario/sensitivity testing |
| **Regional Selector** | Focuses on specific geographies | Improves local policy relevance |
| **Data Export** | Downloadable analysis-ready files | Supports downstream research |

---

## 🧪 How to Run Locally

### 1) Install dependencies
```bash
pip install -r requirements.txt
```

### 2) Launch app
```bash
streamlit run app.py
```

### 3) Open in browser
Streamlit will provide a local URL (usually `http://localhost:8501`).

---

## 🚀 Live Access

Use the **“Open in Streamlit”** / live badge in your repository header to run the hosted version instantly.

---

## 🛠 Suggested Tech Stack (for README clarity)

```txt
Frontend/UI: Streamlit
Data Handling: pandas, numpy
Visuals: plotly / altair / matplotlib
Geo Layer: pydeck / geopandas (if used)
Deployment: Streamlit Community Cloud
```

---

## 🧱 Project Structure (recommended presentation)

```txt
📦 rmpi-dashboard
 ┣ 📄 app.py
 ┣ 📄 requirements.txt
 ┣ 📄 README.md
 ┣ 📂 data/
 ┃ ┣ 📄 raw_*.csv
 ┃ ┗ 📄 processed_*.csv
 ┣ 📂 src/
 ┃ ┣ 📄 preprocessing.py
 ┃ ┣ 📄 scoring.py
 ┃ ┗ 📄 visuals.py
 ┗ 📂 assets/
    ┗ 📄 logo / screenshots
```

---

## 📌 Use Cases

- Early-warning monitoring for migration stress zones
- Donor and NGO prioritization support
- Policy simulation through indicator reweighting
- Research communication with interactive storytelling

---

## 🔮 Next Enhancements

- Add forecast mode for short-term RMPI projection
- Add confidence bands/uncertainty intervals
- Integrate automated data refresh pipelines
- Add country profile pages with drill-down diagnostics

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👤 Author

<div align="center">

## **Ayodele Idowu**  
### Economist & Data Scientist

[![GitHub](https://img.shields.io/badge/GitHub-AyodeleID-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AyodeleID)
[![Portfolio](https://img.shields.io/badge/Portfolio-ayodeleid.com-0A66C2?style=for-the-badge&logo=google-chrome&logoColor=white)](https://ayodeleid.com)

</div>
