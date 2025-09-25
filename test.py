import os
import streamlit as st
from langchain_tavily import TavilySearch

def get_tavily_search():
    # Direct API key (you can also use st.secrets if you don’t want to expose it)
   # api_key = "tvly-d-f2PfBXNcxUjOr69r6XoJ"
    api_key ="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"

    if not api_key:
        st.error("⚠️ Tavily API key missing!")
        return None

    # TavilySearch wrapper
    search = TavilySearch(max_results=1, tavily_api_key=api_key)
    return search

def main():
    st.title("🔍 Tavily Search Agent")
    st.write("Ask me anything and I’ll search for you.")

    # Initialize search
    search = get_tavily_search()
    if not search:
        return

    # Input box
    query = st.text_input("Enter your query:")

    # Button to trigger search
    if st.button("Search") and query:
        try:
            result = search.run(query)
            st.subheader("Results:")
            st.write(result)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
