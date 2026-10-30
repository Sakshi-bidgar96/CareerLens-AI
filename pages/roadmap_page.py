import streamlit as st
from core.roadmap import build_roadmap

def render():
    st.markdown('<div class="eyebrow">PERSONALIZED SKILL DEVELOPMENT</div><h1>Career roadmap</h1><p class="muted">A practical sequence based on the missing skills for your chosen role.</p>',unsafe_allow_html=True)
    results=st.session_state.get("job_results",[])
    if not results: st.info("Roadmap तयार करण्यासाठी आधी resume analyze करा."); return
    role=st.selectbox("Target job role",[r["title"] for r in results])
    selected=next(r for r in results if r["title"]==role)
    st.metric("Current match score",f"{selected['score']}%")
    st.write("Priority skill gaps:",", ".join(selected["missing_required"] or selected["missing_preferred"]) or "No required gaps detected")
    roadmap=build_roadmap(selected)
    for item in roadmap:
        with st.container(border=True):
            st.markdown(f"### {item['week']} · {item['focus']}")
            for task in item["tasks"]: st.checkbox(task,key=f"roadmap_{role}_{item['week']}_{task}")
    st.caption("Roadmap is a starter plan generated from detected skill gaps. Adjust it to your time, current knowledge and target job requirements.")
