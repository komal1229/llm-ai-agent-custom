import os
import streamlit as st
from langchain_tavily import TavilySearch

def get_tavily_search():
    api_key = "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"
    if not api_key:
        st.error("⚠️ Tavily API key missing!")
        return None
    return TavilySearch(max_results=1, tavily_api_key=api_key)

def main():
    st.set_page_config(page_title="Tavily Search Agent", page_icon="🔍", layout="wide")

    # Centered Title
    st.markdown("<h1 style='text-align:center; font-size:40px;'>🔍 Tavily Search Agent</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:gray;'>Ask me anything and I’ll search for you.</p>", unsafe_allow_html=True)

    search = get_tavily_search()
    if not search:
        return

    # Stylish search box in the center
    with st.container():
        st.markdown(
            """
            <style>
            div.stTextInput > div > input {
                font-size:18px;
                padding:12px 20px;
                border-radius:25px;
                border:1px solid #ccc;
                text-align:center;
            }
            div.stButton > button {
                display:block;
                margin: 15px auto;
                background-color:#1a73e8;
                color:white;
                border-radius:20px;
                padding:10px 25px;
                font-size:16px;
                border:none;
                transition:0.3s;
            }
            div.stButton > button:hover {
                background-color:#1664c4;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

    query = st.text_input("", placeholder="Type your query here...")

    if st.button("Search") and query:
        try:
            result = search.run(query)

            st.subheader("📌 Results")
            
            if "results" in result and result["results"]:
                for idx, item in enumerate(result["results"], 1):
                    title = item.get("title", "No Title")
                    url = item.get("url", "#")
                    content = item.get("content", "No description available.")

                    st.markdown(
                        f"""
                        <div style="padding:15px; margin-bottom:15px; border-radius:12px;
                                    border:1px solid #e6e6e6; background-color:#fafafa;
                                    box-shadow: 2px 2px 8px rgba(0,0,0,0.05);">
                            <h3 style="margin:0;">
                                <a href="{url}" target="_blank" style="text-decoration:none; color:#1a73e8;">
                                    {title}
                                </a>
                            </h3>
                            <p style="color:#444; font-size:15px; line-height:1.4;">{content}</p>
                            <p style="font-size:13px; color:gray;">🔗 <a href="{url}" target="_blank">{url}</a></p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            else:
                st.warning("⚠️ No results found.")

            if result.get("follow_up_questions"):
                st.subheader("🤔 You might also ask:")
                for q in result["follow_up_questions"]:
                    st.markdown(f"- {q}")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()

