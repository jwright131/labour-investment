import streamlit as st

# -----------------------------
# Credits Dialog
# -----------------------------

@st.dialog("Credits")
def show_credits_dialog():
    st.markdown("## Credits")
    st.caption("Labour Visualizations Dashboard")

    st.divider()

    st.markdown("**Project Lead**  \nJosh Wright")
    st.markdown("**Developer**  \nJosh Wright")
    st.markdown("**Designer**  \nJosh Wright")
    st.markdown("**Data Preparation**  \nJosh Wright")
    st.markdown("**Visualization Build**  \nJosh Wright")
    st.markdown("**Testing and Review**  \nJosh Wright")

    st.divider()
    st.caption("© 2026 Josh Wright")
# -----------------------------
# Floating Button Renderer
# -----------------------------
def render_credits_button():
    st.markdown(
        """
        <style>
        div[data-testid="stButton"][data-key="credits_button"] {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 9999;
        }

        div[data-testid="stButton"][data-key="credits_button"] > button {
            border-radius: 999px;
            padding: 0.45rem 0.9rem;
            font-size: 0.85rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.18);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button("Credits", key="credits_button"):
        show_credits_dialog()