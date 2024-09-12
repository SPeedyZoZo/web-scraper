import streamlit as st
import csv
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content
)
from parse import parse_with_ollama

st.title("AI Web Scraper")
st.text("""
        An AI Powered web scraper capable of:
        - Scraping data
        - Parsing scraped data
        - Exporting scraped data.
       
        Can handle and scrape from multiple websites simultaneously.
        """)

urls = st.text_area("Enter Website URLs (one per line): ")

if st.button("Scrape Sites"):
    url_list = urls.split('\n')
    st.session_state.all_content = []
   
    for url in url_list:
        result = scrape_website(url)
        body_content = extract_body_content(result)
        cleaned_content = clean_body_content(body_content)
        st.session_state.all_content.append(cleaned_content)
   
    st.success(f"Scraped {len(url_list)} websites")

if "all_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")
   
    if st.button("Parse Content"):
        all_results = []
        for content in st.session_state.all_content:
            dom_chunks = split_dom_content(content)
            result = parse_with_ollama(dom_chunks, parse_description)
            all_results.append(result)
       
        st.session_state.parsed_results = all_results  # Store parsed results in session state
       
        st.write("Parsed Results:")
        for i, result in enumerate(all_results, 1):
            st.write(f"Website {i}:")
            st.write(result)

def export_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['Website', 'Parsed Content'])
        for i, content in enumerate(data, 1):
            writer.writerow([f"Website {i}", content])

if st.button("Export Results"):
    if 'parsed_results' in st.session_state:
        export_to_csv(st.session_state.parsed_results, "parsed_data.csv")
        st.success("Results exported to parsed_data.csv")
    else:
        st.warning("No parsed data to export")