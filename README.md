# Project_WebScrapper
  A Python-based web scraping application that collects product information, including categories, titles, and prices, from a specified website. It utilizes Selenium for browser automation, BeautifulSoup for parsing HTML content, and Pandas for data handling.
## The technologies used
      Backend tools:
        1. Python: The primary programming language for building the scraper.
        2. Selenium: Automates browser interactions to dynamically load web content.
        3. BeautifulSoup: Parses HTML and extracts required data elements.
        4. Pandas: Structures and manages extracted data into a tabular format.

      Environment and Development Tools:
        1. Python Virtual Environment: Ensures isolated dependency management and avoids conflicts with system-wide libraries.
        2. pip: Python's package manager used to install dependencies.
        3. Microsoft Visual Studio Code: The IDE used for coding and debugging.

## How to run the project
  ### Clone the repository
      git clone https://github.com/username/webscraper-project.git
  ### Create and activate the virtual object
      - Create a virtual object using the following command:
            python -m venv myenv
      - Activate the virtual object:
          (1) For Windows:
              myenv\Scripts\activate
          (2) For Mac/Linux:
              source myenv/bin/activate
  ### Install the dependencies
      pip install -r requirements.txt
  ### Run the script
      python WebScrapper.py ( in Visual Studio Code terminal or the code editor you may use)
  ### Check output
      Data will be stored in an Excel file that will be named HackedData
## Testing
  I verified the data manually by checking the excel file and the info that was shown in the terminal to be the same
