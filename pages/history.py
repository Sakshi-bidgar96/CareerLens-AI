import streamlit as st, json, pandas as pd
from database.db import get_history

def render():
    st.markdown('<div class="eyebrow">SAVED ANALYSES</div><h1>History</h1><p class="muted">Your recent analyses for this account.</p>',unsafe_allow_html=True)
    rows=get_history(st.session_state.user_id)
    if not rows: st.info("अजून saved analysis नाही."); return
    for row in rows:
        with st.expander(f"{row['filename']} · {row['created_at']}"):
            skills=json.loads(row["skills_json"]); results=json.loads(row["results_json"])
            st.write("Detected skills:",", ".join(skills) or "None detected")
            st.dataframe(pd.DataFrame([{"Role":r["title"],"Match":r["score"],"Category":r["category"]} for r in results]),use_container_width=True,hide_index=True)
