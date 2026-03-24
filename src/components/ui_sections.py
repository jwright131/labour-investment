import streamlit as st

from core.config import APP_CAPTION, APP_TITLE


def render_page_header():
    st.title(APP_TITLE)
    st.caption(APP_CAPTION)



def render_how_to_use():
    with st.expander("How to Use This Dashboard", expanded=False):
        st.markdown(
            """
### Overview
This dashboard allows you to explore labour market trends across employment, wages, job vacancies, and investment.

### Using Filters
- Each visualization has its own **filter panel**.
- Click on the filter section to expand it.
- You can select **multiple years, provinces, and categories**.
- By default, one category is selected, but all options are available.

### Charts
- **Bar charts** compare provinces across different categories.
- **Line chart** shows how job vacancies change over time.
- **Map** displays investment levels across Canada.

### Map Interaction
- Each province shows a **pie chart marker** representing category breakdowns.
- You can **zoom and pan** the map freely.
- Use the **Zoom to province** dropdown to quickly focus on a specific region.
- Click on markers to see detailed breakdowns.

### Tips
- Select multiple categories to compare industries.
- Narrow to a single province for deeper analysis.
- Combine filters to explore specific trends.
"""
        )
