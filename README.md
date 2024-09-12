# web-scraper
AI Powered web scraper

To get this to work, you must install all dependencies in `requirements.txt` with this command:
`pip install -r requirements.txt`

These are the steps for Windows, other operating systems have not been tested so may follow different steps:

You must download `chromedriver.exe` and `ollama` from online.
Place the `chromedriver.exe` file in your directory.
In a terminal window, perform `ollama pull mistral` to obtain the ollama model.
[
    If you want to use a different model, first, pull that model with `ollama pull <model>`.
    Then go to `parse.py` and change the model in quotes:
        `model = OllamaLLM(model="mistral")`
    to another model. 
]

To run the web app, open a terminal window. Navigate to this directory, type `streamlit run main.py` and a window should open up with the app.
Then type the desired website to scrape, and then type the prompt you would like to parse based on the scraped data.

## Extensions:
1. After parsing the data, it can then be exported to a CSV file: `parsed_data.csv` for usage elsewhere. This overwrites everytime you choose to export data.

Inspired by TechWithTim's YouTube video on this project.

