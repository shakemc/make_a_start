import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("")


with col2:
    st.title("Stanislav Radyk")
    content = """Highly motivated and dedicated professional with a deep passion for cloud computing, 
    Amazon WebServices (AWS), and networking.Committed to enhancing business agility and efficiency through the 
    effective utilization of cloud technologies. A detail-oriented troubleshooter with a proven ability to identify 
    and resolve issues. A pro active team player with strong leadership capabilities, driven by purpose,punctuality, 
    and sociability. Takes ownership of work and maintains stability in challenging situations. Committed to 
    continuous improvement, constantly enhancing skills, and acquiring new knowledge to stay at the forefront of 
    industry trends """
    st.write(content)
