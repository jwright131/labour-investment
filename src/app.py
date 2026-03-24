import streamlit as st

from components.credits import render_credits_button
from components.charts import create_employee_chart, create_vacancy_chart, create_wage_chart
from components.filters import (
    render_employee_filters,
    render_investment_filters,
    render_vacancy_filters,
    render_wage_filters,
)
from components.insights import render_dashboard_insights
from components.map_utils import render_investment_map
from components.ui_sections import render_how_to_use, render_page_header
from core.config import APP_ICON, APP_LAYOUT, APP_TITLE
from core.constants import PIE_COLORS, VACANCY_STAT_LABEL
from core.data_loader import (
    check_required_files,
    load_employee_data,
    load_investment_data,
    load_vacancy_data,
    load_wage_data,
)
from core.utils import filter_in

st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout=APP_LAYOUT)

check_required_files()

employee_df = load_employee_data()
wage_df = load_wage_data()
investment_df = load_investment_data()
vacancy_df = load_vacancy_data()

render_page_header()
render_how_to_use()

insights_placeholder = st.container()

# 1. Employee
st.subheader("1. Employee Count by Province")
emp_filters = render_employee_filters(employee_df)
emp_filtered = filter_in(employee_df.copy(), "Year", emp_filters["years"])
emp_filtered = filter_in(emp_filtered, "Province", emp_filters["provinces"])
emp_filtered = filter_in(emp_filtered, "Categories", emp_filters["categories"])

if emp_filtered.empty:
    st.warning("No employee data for the selected filters.")
else:
    st.plotly_chart(create_employee_chart(emp_filtered), use_container_width=True)

st.divider()

# 2. Wage
st.subheader("2. Average Wage by Province")
wage_filters = render_wage_filters(wage_df)
wage_filtered = filter_in(wage_df.copy(), "Year", wage_filters["years"])
wage_filtered = filter_in(wage_filtered, "Province", wage_filters["provinces"])
wage_filtered = filter_in(wage_filtered, "Category", wage_filters["categories"])

if wage_filtered.empty:
    st.warning("No wage data for the selected filters.")
else:
    st.plotly_chart(create_wage_chart(wage_filtered), use_container_width=True)

st.divider()

# 3. Vacancy
st.subheader("3. Job Vacancies by Month")
vacancy_filters = render_vacancy_filters(vacancy_df)
vacancy_filtered = filter_in(vacancy_df.copy(), "Year", vacancy_filters["years"])
vacancy_filtered = vacancy_filtered[vacancy_filtered["Statistics"] == VACANCY_STAT_LABEL]
vacancy_filtered = filter_in(vacancy_filtered, "NAICS", vacancy_filters["naics"])

if vacancy_filtered.empty:
    st.warning("No vacancy data for the selected filters.")
else:
    st.plotly_chart(create_vacancy_chart(vacancy_filtered), use_container_width=True)

st.divider()

# 4. Investment Map
st.subheader("4. Investment Map by Province")
investment_filters = render_investment_filters(investment_df)
map_filtered = filter_in(investment_df.copy(), "Year", investment_filters["years"])
map_filtered = filter_in(map_filtered, "Province", investment_filters["provinces"])
map_filtered = filter_in(map_filtered, "Category", investment_filters["categories"])

if map_filtered.empty:
    st.warning("No investment data for the selected filters.")
else:
    render_investment_map(
        map_filtered,
        investment_filters["zoom_target"],
        investment_filters["categories"],
    )

    st.markdown("##### Province pie marker legend")
    legend_cols = st.columns(min(len(investment_filters["categories"]), 4) or 1)
    for i, category in enumerate(investment_filters["categories"]):
        with legend_cols[i % len(legend_cols)]:
            st.markdown(
                f"<div style='display:flex;align-items:center;gap:8px;'><span style='display:inline-block;width:14px;height:14px;background:{PIE_COLORS[i % len(PIE_COLORS)]};border-radius:2px;'></span>{category}</div>",
                unsafe_allow_html=True,
            )

with insights_placeholder:
    render_dashboard_insights(
        emp_filtered=emp_filtered,
        wage_filtered=wage_filtered,
        vacancy_filtered=vacancy_filtered,
        map_filtered=map_filtered,
        emp_filters=emp_filters,
        wage_filters=wage_filters,
        vacancy_filters=vacancy_filters,
        investment_filters=investment_filters,
    )
render_credits_button()