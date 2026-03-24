import plotly.express as px


def create_employee_chart(emp_filtered):
    grouped = emp_filtered.groupby(["Province", "Categories"], as_index=False)["Employee Count"].sum()
    fig = px.bar(grouped, x="Province", y="Employee Count", color="Categories", title="Employee Count by Province")
    fig.update_layout(xaxis_title="Province", yaxis_title="Employee Count", legend_title="Category")
    return fig



def create_wage_chart(wage_filtered):
    grouped = wage_filtered.groupby(["Province", "Category"], as_index=False)["Wage"].mean()
    fig = px.bar(grouped, x="Province", y="Wage", color="Category", title="Average Wage by Province")
    fig.update_layout(barmode="group", xaxis_title="Province", yaxis_title="Average Wage", legend_title="Category")
    return fig



def create_vacancy_chart(vacancy_filtered):
    grouped = vacancy_filtered.groupby(["MonthDate", "NAICS"], as_index=False)["Values"].sum()
    fig = px.line(grouped, x="MonthDate", y="Values", color="NAICS", markers=True, title="Job Vacancies by Month")
    fig.update_layout(xaxis_title="Month", yaxis_title="Vacancies", legend_title="Industry")
    return fig
