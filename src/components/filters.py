import streamlit as st

from core.utils import default_one, sorted_int_list, sorted_text_list


def render_employee_filters(employee_df):
    years = sorted_int_list(employee_df["Year"])
    provinces = sorted_text_list(employee_df["Province"])
    categories = sorted_text_list(employee_df["Categories"])

    with st.expander("Employee filters", expanded=False):
        selected_years = st.multiselect("Year", years, default=default_one(years[-1:]), key="emp_years")
        selected_provinces = st.multiselect("Province", provinces, default=provinces, key="emp_provinces")
        selected_categories = st.multiselect("Category", categories, default=default_one(categories), key="emp_categories")

    return {
        "years": selected_years,
        "provinces": selected_provinces,
        "categories": selected_categories,
    }



def render_wage_filters(wage_df):
    years = sorted_int_list(wage_df["Year"])
    provinces = sorted_text_list(wage_df["Province"])
    categories = sorted_text_list(wage_df["Category"])

    with st.expander("Wage filters", expanded=False):
        selected_years = st.multiselect("Year", years, default=default_one(years[-1:]), key="wage_years")
        selected_provinces = st.multiselect("Province", provinces, default=provinces, key="wage_provinces")
        selected_categories = st.multiselect("Category", categories, default=default_one(categories), key="wage_categories")

    return {
        "years": selected_years,
        "provinces": selected_provinces,
        "categories": selected_categories,
    }



def render_vacancy_filters(vacancy_df):
    years = sorted_int_list(vacancy_df["Year"])
    naics = sorted_text_list(vacancy_df["NAICS"])

    with st.expander("Job vacancy filters", expanded=False):
        selected_years = st.multiselect("Year", years, default=default_one(years[-1:]), key="vacancy_years")
        selected_naics = st.multiselect("Industry / NAICS", naics, default=default_one(naics), key="vacancy_naics")

    return {
        "years": selected_years,
        "naics": selected_naics,
    }



def render_investment_filters(investment_df):
    years = sorted_int_list(investment_df["Year"])
    provinces = sorted_text_list(investment_df["Province"])
    categories = sorted_text_list(investment_df["Category"])

    with st.expander("Investment map filters", expanded=False):
        selected_years = st.multiselect("Year", years, default=default_one(years[-1:]), key="investment_years")
        selected_provinces = st.multiselect("Province", provinces, default=provinces, key="investment_provinces")
        selected_categories = st.multiselect("Category", categories, default=default_one(categories), key="investment_categories")
        zoom_target = st.selectbox("Zoom to province", ["Canada"] + provinces, index=0, key="map_zoom_target")

    return {
        "years": selected_years,
        "provinces": selected_provinces,
        "categories": selected_categories,
        "zoom_target": zoom_target,
    }
