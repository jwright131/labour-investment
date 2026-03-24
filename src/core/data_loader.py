import pandas as pd
import streamlit as st

from core.config import EMPLOYEE_FILE, INVESTMENT_FILE, VACANCY_FILE, WAGE_FILE


def check_file(path):
    if not path.exists():
        st.error(f"Missing file: {path}")
        st.stop()
    return path


def check_required_files():
    check_file(EMPLOYEE_FILE)
    check_file(VACANCY_FILE)
    check_file(INVESTMENT_FILE)
    check_file(WAGE_FILE)


@st.cache_data
def load_employee_data():
    df = pd.read_csv(EMPLOYEE_FILE)
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    df["Employee Count"] = df["Employee Count"].astype(str).str.replace(",", "", regex=False)
    df["Employee Count"] = pd.to_numeric(df["Employee Count"], errors="coerce")
    df["Province"] = df["Province"].astype(str).str.strip()
    df["Categories"] = df["Categories"].astype(str).str.strip()
    return df.dropna(subset=["Year", "Employee Count", "Province", "Categories"])


@st.cache_data
def load_wage_data():
    df = pd.read_csv(WAGE_FILE)
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    df["Wage"] = pd.to_numeric(df["Wage"], errors="coerce")
    df["Province"] = df["Province"].astype(str).str.strip()
    df["Category"] = df["Category"].astype(str).str.strip()
    return df.dropna(subset=["Year", "Wage", "Province", "Category"])


@st.cache_data
def load_investment_data():
    df = pd.read_csv(INVESTMENT_FILE)
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    df["Investment Value"] = df["Investment Value"].astype(str).str.replace(",", "", regex=False)
    df["Investment Value"] = pd.to_numeric(df["Investment Value"], errors="coerce")
    df["Province"] = df["Province"].astype(str).str.strip()
    df["Category"] = df["Category"].astype(str).str.strip()
    return df.dropna(subset=["Year", "Investment Value", "Province", "Category"])


@st.cache_data
def load_vacancy_data():
    df = pd.read_csv(VACANCY_FILE)
    df["Values"] = df["Values"].astype(str).str.replace(",", "", regex=False)
    df["Values"] = pd.to_numeric(df["Values"], errors="coerce")
    df["MonthDate"] = pd.to_datetime(df["Date"], format="%y-%b", errors="coerce")
    df["Year"] = df["MonthDate"].dt.year.astype("Int64")

    if "North American Industry Classification System (NAICS) 4" in df.columns:
        df["NAICS"] = df["North American Industry Classification System (NAICS) 4"].astype(str).str.strip()
    else:
        df["NAICS"] = "All"

    if "Statistics" in df.columns:
        df["Statistics"] = df["Statistics"].astype(str).str.strip()
    else:
        df["Statistics"] = "All"

    return df.dropna(subset=["MonthDate", "Year", "Values", "NAICS", "Statistics"])
