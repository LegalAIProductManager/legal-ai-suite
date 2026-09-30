"""
Enterprise Legal & Governance Operations Suite
Author: Michael Torre
Description: A unified multi-module Streamlit command center for enterprise legal intake, 
             legal tech vendor evaluation (Harvey vs. Legora), and high-volume PE entity governance.
"""

import streamlit as st
import time
import pandas as pd

# --- Page Configuration ---
st.set_page_config(
    page_title="Enterprise Legal & Governance Suite",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom Styling for Enterprise Look ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton button { width: 100%; border-radius: 6px; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

# --- Global Sidebar Navigation ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/law.png", width=60)
    st.title("Governance Suite")
    st.markdown("---")
    
    selected_module = st.radio(
        "Select Operations Module",
        [
            "⚡ 1. Commercial AI Intake & Risk",
            "📊 2. Vendor Fit (Harvey vs. Legora)",
            "🏢 3. Entity Lifecycle & M&A Governance"
        ]
    )
    st.markdown("---")
    st.info("System Status: 🟢 All Connectors Online (Slack, Outlook, Calendar, DB)")


# ==========================================
# MODULE 1: COMMERCIAL AI INTAKE & RISK
# ==========================================
if selected_module == "⚡ 1. Commercial AI Intake & Risk":
    st.title("⚡ Multi-Channel Legal AI Command Center")
    st.markdown("Automate routine commercial agreement intake, contextualize across enterprise tools, and enforce risk guardrails.")
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📁 Web Drop Zone", "💬 Slack / Teams Simulator", "✉️ Outlook & Calendar Context"])

    with tab1:
        st.subheader("Direct Document Intake")
        uploaded_file = st.file_uploader("Upload Counterparty Agreement (PDF or Word)", type=["pdf", "docx", "txt"])
        counterparty_name = st.text_input("Counterparty Name", placeholder="e.g., Apex Infrastructure Corp")

    with tab2:
        st.subheader("Chat Channel Ingestion")
        st.info("Simulating inbound request from internal business ops/sales via Slack.")
        slack_input = st.text_area("Paste chat snippet or request", placeholder="Hey @legal, need a rapid review on this vendor MSA. Payment terms are net-60.")

    with tab3:
        st.subheader("Aggregated Workspace Context")
        col_a, col_b = st.columns(2)
        with col_a:
            st.text_input("Linked Outlook Thread", value="re: Master Services Agreement markup v3.docx")
        with col_b:
            st.text_input("Upcoming Calendar Event", value="Vendor Closing Sync - Oct 18")

    st.markdown("###")
    if st.button("🚀 Run Contextual AI Risk Review", type="primary"):
        with st.spinner("Aggregating workspace context and evaluating playbooks..."):
            time.sleep(1.5)
            
        st.success("Review Complete!")
        st.markdown("---")
        st.subheader("📊 Risk Assessment & Routing Result")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label="Overall Risk Tier", value="RED 🔴", delta="Requires GC Escalation")
        with c2:
            st.metric(label="Context Source", value="Slack + Outlook", delta="Matched 3 threads")
        with c3:
            st.metric(label="Processing Time", value="1.2 seconds", delta="Optimized")

        with st.expander("🔍 View Detailed Clause Breakdown & Fallbacks", expanded=True):
            st.markdown("**1. Confidentiality Term:** Flagged as *Perpetual* (High Risk).")
            st.info("**Recommended Fallback:** *'The obligations of confidentiality shall survive for a period of three (3) years following termination.'*")
            st.markdown("**2. Governing Law:** References unspecified foreign jurisdiction.")
            st.warning("**Recommended Fallback:** *'This Agreement shall be governed by the laws of the State of New York.'*")


# ==========================================
# MODULE 2: VENDOR FIT (HARVEY vs. LEGORA)
# ==========================================
elif selected_module == "📊 2. Vendor Fit (Harvey vs. Legora)":
    st.title("📊 Vendor Fit: AI Platform Evaluation & Bake-Off")
    st.markdown("Multi-department scorecard, public market capabilities analysis, and POC testing results for enterprise AI deployment.")
    st.markdown("---")

    col_h, col_l = st.columns(2)
    with col_h:
        st.markdown("### 🏛️ Harvey AI")
        st.caption("US BigLaw Market Leader / OpenAI GPT-4 Architecture")
        st.markdown("- **Strengths:** Heavy-hitter brand, deep US litigation precedent integration, secure agentic workspaces.")
        st.markdown("- **Considerations:** Premium pricing tier ($1,200–$2,000+/seat/mo), enterprise-only gate.")
    with col_l:
        st.markdown("### 🇪🇺 Legora")
        st.caption("European/Cross-Border Leader / Native aOS Architecture")
        st.markdown("- **Strengths:** Tabular review grids for M&A due diligence, multilingual cross-border capabilities, strong GDPR compliance.")
        st.markdown("- **Considerations:** 10-seat minimum, structured around structured grid interactions.")

    st.markdown("---")
    st.subheader("⚙️ Multi-Department Weighted Scoring Methodology")
    st.markdown("Adjust department weights to reflect enterprise priorities:")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        w_it = st.slider("IT (%)", 0, 50, 20)
    with col2:
        w_sec = st.slider("InfoSec (%)", 0, 50, 30)
    with col3:
        w_comp = st.slider("Compliance (%)", 0, 50, 20)
    with col4:
        w_legal = st.slider("Legal (%)", 0, 50, 20)
    with col5:
        w_tax = st.slider("Tax & Finance (%)", 0, 50, 10)

    total_weight = w_it + w_sec + w_comp + w_legal + w_tax
    if total_weight != 100:
        st.warning(f"⚠️ Current total weight is {total_weight}%. Recommended total is 100%.")

    st.markdown("###")
    st.subheader("📈 POC Model Testing & Feature Ranking Results")
    
    poc_data = pd.DataFrame({
        "Evaluation Dimension": [
            "Data Security & Sovereignty", 
            "Tabular M&A Review & Grid Speed", 
            "Contract Redlining & Word Add-in", 
            "Cross-Border Multi-Jurisdiction", 
            "API / Enterprise Connector Flexibility"
        ],
        "Harvey Score (1-10)": [9.1, 7.8, 9.4, 7.5, 8.2],
        "Legora Score (1-10)": [8.9, 9.6, 8.5, 9.2, 8.7]
    })
    st.dataframe(poc_data, use_container_width=True)


# ==========================================
# MODULE 3: ENTITY LIFECYCLE & M&A GOVERNANCE
# ==========================================
elif selected_module == "🏢 3. Entity Lifecycle & M&A Governance":
    st.title("🏢 Entity Lifecycle & M&A Governance Engine")
    st.markdown("High-volume PE entity onboarding, global core data management, and departmental sign-off gates.")
    st.markdown("---")

    tab_create, tab_tracker = st.tabs(["➕ Single & Bulk Entity Intake", "📋 Cross-Departmental Approval Tracker"])

    with tab_create:
        st.subheader("Global Core Entity Information")
        st.markdown("Enter core corporate metadata required before routing to departments:")

        col_e1, col_e2, col_e3 = st.columns(3)
        with col_e1:
            ent_name = st.text_input("Legal Entity Name", placeholder="e.g., DataCenter Holdings Sub LLC")
            ent_jurisdiction = st.selectbox("Jurisdiction / State", ["Delaware (US)", "Maryland (US)", "Luxembourg", "Cayman Islands", "United Kingdom"])
        with col_e2:
            ent_type = st.selectbox("Entity Structure", ["Limited Liability Company (LLC)", "Corporation (Inc.)", "Limited Partnership (LP)", "Branch Office"])
            ent_tax_id = st.text_input("Tax ID / EIN", placeholder="XX-XXXXXXX")
        with col_e3:
            ent_business = st.text_input("Primary Business Line", placeholder="e.g., Infrastructure Operations")
            ent_contact = st.text_input("Primary Business Contact", placeholder="Name / Email")

        st.markdown("---")
        st.subheader("📥 Bulk Entity CSV / Template Upload")
        st.file_uploader("Upload 20-point entity spreadsheet template", type=["csv", "xlsx"])

        if st.button("🚀 Submit Entity for Departmental Routing", type="primary"):
            st.success("Entity record created and locked in staging! Triggering automated cross-functional workflows...")

    with tab_tracker:
        st.subheader("Active Entity Governance & Regional Sign-Off Gates")
        st.markdown("Entities cannot be finalized or pushed to the centralized agent database until all departmental gate questions are satisfied.")

        entity_records = pd.DataFrame({
            "Entity Name": ["Project Atlas Sub A LLC", "NorthStar Data Europa BV", "Cascade PropHoldings LLC"],
            "Jurisdiction": ["Delaware (US)", "Netherlands", "Nevada (US)"],
            "Legal Gate": ["🟢 Approved", "🟢 Approved", "🟡 Pending Review"],
            "Tax Sign-Off": ["🟢 Approved", "🔴 Pending Filing", "🔴 Pending Review"],
            "Treasury / Finance": ["🟢 Approved", "🟢 Approved", "🟡 Pending Bank Setup"],
            "Overall Status": ["Ready for Centralization", "Blocked (Tax)", "In Staging"]
        })
        st.dataframe(entity_records, use_container_width=True)

        st.markdown("###")
        st.subheader("🔍 Departmental Questionnaire Gate: NorthStar Data Europa BV")
        st.info("Tax Department Action Required: Confirm foreign disregarded entity election form status.")
        
        tax_q1 = st.radio("Has the Form 8832 (or regional equivalent) been verified by external counsel?", ["Select...", "Yes - Filed & Confirmed", "No - Pending Review", "Not Applicable"])
        tax_note = st.text_area("Tax Department Review Notes", placeholder="Enter compliance comments or conditions...")
        
        if st.button("💾 Submit Departmental Sign-Off"):
            st.success("Tax sign-off recorded. Status updated in audit trail.")
