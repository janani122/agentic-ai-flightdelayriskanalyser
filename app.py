from workflow_graph import graph
import streamlit as st

st.set_page_config(page_title="AI Airport Control Tower")

st.title("✈️ AI Airport Control Tower")

flight = st.text_input("Flight Number")
departure = st.text_input("Departure Airport")

if st.button("Analyze Flight"):
    if flight == "" or departure == "":
        st.warning("Please enter all details")
    else:
        state = {
            "flight": flight,
            "departure": departure
        }

        with st.spinner("Analyzing flight..."):
            result = graph.invoke(state)

        st.subheader("Agent Analysis")

        st.write("Weather:", result.get("weather"))
        st.write("Traffic:", result.get("traffic"))
        st.write("Flight Status:", result.get("flight_status"))
        st.write("Gate Status:", result.get("gate"))

        st.subheader("AI Recommendation")

        st.markdown(result.get("decision"))