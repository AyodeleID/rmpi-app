# ----------------- RMPI Streamlit App -----------------
import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# -----------------
# Page Config (MUST be first and only once)
# -----------------
st.set_page_config(
    page_title="Global Real-Time Migration Pressure Index (RMPI)",
    layout="wide"
)

# -----------------
# Load dataset
# -----------------
@st.cache_data
def load_data():
    file_path = "data/processed/master_rmpi_with_mpi.csv"  # relative path for GitHub/Streamlit
    df = pd.read_csv(file_path)
    # expected columns: country_name, year, migration_pressure_index
    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    df = df.dropna(subset=["year", "migration_pressure_index"]).copy()
    df["year"] = df["year"].astype(int)
    df = df.sort_values(["country_name", "year"])
    return df

df = load_data()

# -----------------
# App Title & Tabs
# -----------------
st.title("Global Real-Time Migration Pressure Index (RMPI)")

# Short note about MPI composition
st.markdown("""
**About the RMPI:**  
The Migration Pressure Index (MPI) is constructed using a machine learning model  
(Random Forest and Exponential Smoothing) trained on multiple global drivers,  
including **conflict and violence, climate shocks, socioeconomic factors, and political stability**.  
The index provides a standardized score (**0–1**) capturing migration and displacement pressures.  
""")

tabs = st.tabs([
    "Global Overview",
    "Country Detail",
    "Comparison",
    "Emigration vs Immigration",
    "Forecasts"
])

# -----------------
# Tab 1: Global Overview
# -----------------
with tabs[0]:
    st.header("Global Overview")
    st.caption("World map of Migration Pressure Index (MPI) by year.")

    year_selected = st.slider(
        "Select year",
        int(df["year"].min()),
        int(df["year"].max()),
        int(df["year"].min()),
        key="glob_year"
    )

    df_year = df[df["year"] == year_selected]

    if not df_year.empty:
        fig_map = px.choropleth(
            df_year,
            locations="country_name",
            locationmode="country names",
            color="migration_pressure_index",
            color_continuous_scale="Reds",
            title=f"Global Migration Pressure Index in {year_selected}",
        )
        fig_map.update_layout(
            margin=dict(l=0, r=0, t=40, b=0),
            height=600,
            geo=dict(projection_type="natural earth")
        )
        st.plotly_chart(fig_map, use_container_width=True)
    else:
        st.info("No data for the selected year.")

    st.write("Sample MPI data for this year")
    df_display = df_year.copy()
    df_display["year"] = df_display["year"].astype(str)
    col_tbl, _ = st.columns([1, 2])
    with col_tbl:
        st.dataframe(df_display, use_container_width=True)

# -----------------
# Tab 2: Country Detail
# -----------------
with tabs[1]:
    st.header("Country Detail")

    country_list = sorted(df["country_name"].dropna().unique().tolist())
    country_selected = st.selectbox("Select a country", country_list, key="detail_country")

    df_country = df[df["country_name"] == country_selected].sort_values("year")

    if df_country.empty:
        st.info("No data for this country yet.")
    else:
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            fig, ax = plt.subplots(figsize=(6.0, 3.0), dpi=150)
            ax.plot(
                df_country["year"].values,
                df_country["migration_pressure_index"].values,
                marker="o", linewidth=2
            )
            ax.set_title(f"Migration Pressure Trend - {country_selected}", fontsize=14)
            ax.set_xlabel("Year", fontsize=11)
            ax.set_ylabel("MPI", fontsize=11)
            ax.set_xticks(df_country["year"].tolist())
            ax.grid(True, alpha=0.25, linestyle="--")
            plt.tight_layout()
            st.pyplot(fig)

# -----------------
# Tab 3: Comparison (placeholder)
# -----------------
with tabs[2]:
    st.header("Comparison")
    st.caption("Compare MPI across multiple countries (coming next).")

# -----------------
# Tab 4: Emigration vs Immigration (placeholder)
# -----------------
with tabs[3]:
    st.header("Emigration vs Immigration")
    st.caption("EPI/IAI views (coming next).")

# -----------------
# Tab 5: Forecasts
# -----------------
with tabs[4]:
    st.header("Forecasts")

    country_for_fc = st.selectbox("Select country for forecast", country_list, key="fc_country")
    df_fc = df[df["country_name"] == country_for_fc].sort_values("year")

    if df_fc.empty or df_fc["year"].nunique() < 2:
        st.info("Need at least 2 historical points to forecast.")
    else:
        horizon = st.slider("Forecast horizon (years ahead)", 1, 10, 5, key="fc_h")

        y = df_fc.set_index("year")["migration_pressure_index"].astype(float)
        model = ExponentialSmoothing(y, trend="add", seasonal=None)
        fit = model.fit()

        last_year = int(y.index.max())
        fc_years = list(range(last_year + 1, last_year + horizon + 1))
        forecast_values = fit.forecast(horizon)

        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            fig, ax = plt.subplots(figsize=(6.0, 3.0), dpi=150)
            ax.plot(y.index.values, y.values, label="Historical MPI", marker="o", linewidth=2)
            ax.plot(fc_years, forecast_values.values, label="Forecast MPI", marker="x", linestyle="--", linewidth=2)
            ax.set_title(f"Migration Pressure Index Forecast ({country_for_fc})", fontsize=14)
            ax.set_xlabel("Year", fontsize=11)
            ax.set_ylabel("MPI", fontsize=11)
            ax.set_xticks(list(y.index.values) + fc_years)
            ax.grid(True, alpha=0.25, linestyle="--")
            ax.legend()
            plt.tight_layout()
            st.pyplot(fig)

        forecast_df = pd.DataFrame({"year": fc_years, "predicted_mpi": forecast_values.values})
        forecast_df_display = forecast_df.copy()
        forecast_df_display["year"] = forecast_df_display["year"].astype(str)
        st.write("Forecast values:")
        col_tbl_fc, _ = st.columns([1, 2])
        with col_tbl_fc:
            st.dataframe(forecast_df_display, use_container_width=True)

# -----------------
# Footer / Developer Credit
# -----------------
st.markdown("""
---
**Developer:**  
*Ayodele Idowu*  
Economist | Data Scientist
""")
