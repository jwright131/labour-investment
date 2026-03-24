import streamlit as st

from core.utils import format_list_for_text


def render_dashboard_insights(
    emp_filtered,
    wage_filtered,
    vacancy_filtered,
    map_filtered,
    emp_filters,
    wage_filters,
    vacancy_filters,
    investment_filters,
):
    with st.expander("Dashboard Insights", expanded=True):
        st.markdown("### Detailed Summary Based on Current Filters")

        st.markdown("#### Active Filter Snapshot")
        st.markdown(
            f"""
**Employee filters**
- Years: {format_list_for_text(emp_filters['years'])}
- Provinces: {format_list_for_text(emp_filters['provinces'])}
- Categories: {format_list_for_text(emp_filters['categories'])}

**Wage filters**
- Years: {format_list_for_text(wage_filters['years'])}
- Provinces: {format_list_for_text(wage_filters['provinces'])}
- Categories: {format_list_for_text(wage_filters['categories'])}

**Vacancy filters**
- Years: {format_list_for_text(vacancy_filters['years'])}
- Industries: {format_list_for_text(vacancy_filters['naics'])}

**Investment filters**
- Years: {format_list_for_text(investment_filters['years'])}
- Provinces: {format_list_for_text(investment_filters['provinces'])}
- Categories: {format_list_for_text(investment_filters['categories'])}
- Map focus: {investment_filters['zoom_target']}
"""
        )

        st.markdown("---")
        st.markdown("#### Labour Market Insights")

        emp_totals = None
        wage_totals = None
        vacancy_naics_totals = None
        investment_totals = None

        if emp_filtered.empty:
            st.markdown("**Employee Count:** No employee data matches the current employee filters.")
        else:
            emp_totals = emp_filtered.groupby("Province", as_index=False)["Employee Count"].sum().sort_values("Employee Count", ascending=False)
            emp_cat_totals = emp_filtered.groupby("Categories", as_index=False)["Employee Count"].sum().sort_values("Employee Count", ascending=False)
            top_emp = emp_totals.iloc[0]
            bottom_emp = emp_totals.iloc[-1]
            top_emp_cat = emp_cat_totals.iloc[0]
            total_emp = emp_filtered["Employee Count"].sum()
            st.markdown(
                f"**Employee Count:** The current employee selection contains **{total_emp:,.0f}** total employees. "
                f"**{top_emp['Province']}** has the highest count at **{top_emp['Employee Count']:,.0f}**, while "
                f"**{bottom_emp['Province']}** has the lowest at **{bottom_emp['Employee Count']:,.0f}**. "
                f"The largest employee category is **{top_emp_cat['Categories']}** with **{top_emp_cat['Employee Count']:,.0f}** employees."
            )

        if wage_filtered.empty:
            st.markdown("**Wages:** No wage data matches the current wage filters.")
        else:
            wage_totals = wage_filtered.groupby("Province", as_index=False)["Wage"].mean().sort_values("Wage", ascending=False)
            wage_cat_totals = wage_filtered.groupby("Category", as_index=False)["Wage"].mean().sort_values("Wage", ascending=False)
            top_wage = wage_totals.iloc[0]
            bottom_wage = wage_totals.iloc[-1]
            top_wage_cat = wage_cat_totals.iloc[0]
            avg_wage_all = wage_filtered["Wage"].mean()
            wage_gap = top_wage["Wage"] - bottom_wage["Wage"]
            st.markdown(
                f"**Wages:** The overall average wage in the filtered data is **{avg_wage_all:,.2f}**. "
                f"**{top_wage['Province']}** has the highest average wage at **{top_wage['Wage']:,.2f}**, while "
                f"**{bottom_wage['Province']}** has the lowest at **{bottom_wage['Wage']:,.2f}**. "
                f"The gap between them is **{wage_gap:,.2f}**. The highest-paying category is **{top_wage_cat['Category']}** at **{top_wage_cat['Wage']:,.2f}**."
            )

        if vacancy_filtered.empty:
            st.markdown("**Job Vacancies:** No vacancy data matches the current vacancy filters.")
        else:
            vacancy_monthly = vacancy_filtered.groupby("MonthDate", as_index=False)["Values"].sum().sort_values("MonthDate")
            vacancy_naics_totals = vacancy_filtered.groupby("NAICS", as_index=False)["Values"].sum().sort_values("Values", ascending=False)
            top_vacancy_naics = vacancy_naics_totals.iloc[0]
            total_vacancies = vacancy_filtered["Values"].sum()
            avg_monthly_vacancies = vacancy_monthly["Values"].mean()

            if len(vacancy_monthly) >= 2:
                first_val = vacancy_monthly.iloc[0]["Values"]
                last_val = vacancy_monthly.iloc[-1]["Values"]
                first_month = vacancy_monthly.iloc[0]["MonthDate"].strftime("%b %Y")
                last_month = vacancy_monthly.iloc[-1]["MonthDate"].strftime("%b %Y")
                change = last_val - first_val
                if last_val > first_val:
                    detail_text = "This suggests hiring demand strengthened over the selected period."
                    trend_text = "an upward trend"
                elif last_val < first_val:
                    detail_text = "This suggests hiring demand softened over the selected period."
                    trend_text = "a downward trend"
                else:
                    detail_text = "This suggests hiring demand remained fairly steady over the selected period."
                    trend_text = "a stable trend"

                st.markdown(
                    f"**Job Vacancies:** The filtered vacancy data contains **{total_vacancies:,.0f}** total vacancies, with an average of **{avg_monthly_vacancies:,.0f}** per month. "
                    f"The trend is **{trend_text}** from **{first_month}** to **{last_month}**, changing from **{first_val:,.0f}** to **{last_val:,.0f}** for a net change of **{change:,.0f}**. "
                    f"The industry with the highest total vacancies is **{top_vacancy_naics['NAICS']}** with **{top_vacancy_naics['Values']:,.0f}** vacancies. {detail_text}"
                )
            else:
                st.markdown(
                    f"**Job Vacancies:** The filtered vacancy data contains **{total_vacancies:,.0f}** total vacancies. "
                    f"The highest-vacancy industry is **{top_vacancy_naics['NAICS']}** with **{top_vacancy_naics['Values']:,.0f}** vacancies."
                )

        if map_filtered.empty:
            st.markdown("**Investment:** No investment data matches the current investment filters.")
        else:
            investment_totals = map_filtered.groupby("Province", as_index=False)["Investment Value"].sum().sort_values("Investment Value", ascending=False)
            investment_cat_totals = map_filtered.groupby("Category", as_index=False)["Investment Value"].sum().sort_values("Investment Value", ascending=False)
            top_inv = investment_totals.iloc[0]
            bottom_inv = investment_totals.iloc[-1]
            top_inv_cat = investment_cat_totals.iloc[0]
            total_investment = map_filtered["Investment Value"].sum()
            st.markdown(
                f"**Investment:** The filtered investment data totals **{total_investment:,.0f}**. "
                f"**{top_inv['Province']}** has the highest total at **{top_inv['Investment Value']:,.0f}**, while "
                f"**{bottom_inv['Province']}** has the lowest at **{bottom_inv['Investment Value']:,.0f}**. "
                f"The largest investment category is **{top_inv_cat['Category']}**, totaling **{top_inv_cat['Investment Value']:,.0f}**."
            )

        st.markdown("---")
        st.markdown("#### Overall Interpretation")

        overall_notes = []
        if emp_totals is not None:
            overall_notes.append(f"employee activity is strongest in **{emp_totals.iloc[0]['Province']}**")
        if wage_totals is not None:
            overall_notes.append(f"the highest wages appear in **{wage_totals.iloc[0]['Province']}**")
        if vacancy_naics_totals is not None:
            overall_notes.append(f"the most job-vacancy pressure appears in **{vacancy_naics_totals.iloc[0]['NAICS']}**")
        if investment_totals is not None:
            overall_notes.append(f"investment is most concentrated in **{investment_totals.iloc[0]['Province']}**")

        if overall_notes:
            st.markdown(
                "Based on the current filters, " + ", ".join(overall_notes) +
                ". Together, these results help compare where labour supply, wage pressure, hiring demand, and investment activity are strongest."
            )
        else:
            st.markdown("There is not enough filtered data across the current selections to build an overall dashboard interpretation.")
