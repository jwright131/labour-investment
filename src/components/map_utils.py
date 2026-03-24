import math

import folium
from streamlit_folium import st_folium

from core.constants import PIE_COLORS, PROVINCE_COORDS


def build_pie_svg(labels, values, size=70):
    total = sum(values)
    if total <= 0:
        return f'''
        <svg width="{size}" height="{size}" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="45" fill="#d9d9d9" stroke="#222" stroke-width="2"/>
        </svg>
        '''

    cx, cy, r = 50, 50, 45
    start_angle = -90
    paths = []

    for i, value in enumerate(values):
        frac = value / total
        sweep = frac * 360
        end_angle = start_angle + sweep

        x1 = cx + r * math.cos(math.radians(start_angle))
        y1 = cy + r * math.sin(math.radians(start_angle))
        x2 = cx + r * math.cos(math.radians(end_angle))
        y2 = cy + r * math.sin(math.radians(end_angle))

        large_arc = 1 if sweep > 180 else 0
        color = PIE_COLORS[i % len(PIE_COLORS)]

        if frac >= 0.9999:
            path = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" />'
        else:
            path = (
                f'<path d="M {cx},{cy} '
                f'L {x1:.4f},{y1:.4f} '
                f'A {r},{r} 0 {large_arc},1 {x2:.4f},{y2:.4f} Z" '
                f'fill="{color}" />'
            )
        paths.append(path)
        start_angle = end_angle

    return f'''
    <svg width="{size}" height="{size}" viewBox="0 0 100 100">
        {''.join(paths)}
        <circle cx="50" cy="50" r="45" fill="none" stroke="#222" stroke-width="2"/>
    </svg>
    '''



def add_pie_marker(fmap, province, grouped_df):
    coords = PROVINCE_COORDS.get(province)
    if not coords or grouped_df.empty:
        return

    labels = grouped_df["Category"].tolist()
    values = grouped_df["Investment Value"].tolist()
    svg = build_pie_svg(labels, values, size=72)

    legend_html = "".join(
        f"<div style='margin-bottom:4px;'><span style='display:inline-block;width:10px;height:10px;background:{PIE_COLORS[i % len(PIE_COLORS)]};margin-right:6px;'></span>{label}: {value:,.0f}</div>"
        for i, (label, value) in enumerate(zip(labels, values))
    )

    popup_html = f'''
    <div style="width:220px;">
        <h4 style="margin:0 0 8px 0;">{province}</h4>
        {legend_html}
    </div>
    '''

    folium.Marker(
        location=[coords["lat"], coords["lon"]],
        icon=folium.DivIcon(
            html=f'''
            <div style="width:72px;height:72px;display:flex;align-items:center;justify-content:center;">
                {svg}
            </div>
            '''
        ),
        popup=folium.Popup(popup_html, max_width=260),
        tooltip=province,
    ).add_to(fmap)



def render_investment_map(map_filtered, zoom_target, investment_selected_categories):
    center = PROVINCE_COORDS.get(zoom_target, PROVINCE_COORDS["Canada"])
    fmap = folium.Map(
        location=[56.1304, -106.3468],  # Canada center
        zoom_start=3,
        min_zoom=3,
        max_zoom=8,
        tiles="CartoDB positron"
    )

    grouped_for_pies = map_filtered.groupby(["Province", "Category"], as_index=False)["Investment Value"].sum()

    for province in sorted(grouped_for_pies["Province"].unique().tolist()):
        province_df = grouped_for_pies[grouped_for_pies["Province"] == province].copy()
        add_pie_marker(fmap, province, province_df)

    st_folium(fmap, width=None, height=650, returned_objects=[])
    return grouped_for_pies
