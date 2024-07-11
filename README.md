### Script Description: HostUrlFinder

**Overview:**
 HostUrlFinder is a Python-based tool designed to extract and categorize links from a given URL. It is particularly useful for web information gathering and can help users get more details about a web application by analyzing the links present on a webpage. The tool categorizes links based on their file extensions and generates a report of the findings.

**Key Features:**
- Extracts all links from a webpage, not just `<a href="#">` tags.
- Identifies the extension of linked files (e.g., JavaScript, PHP, images, HTML).
- Generates a report summarizing the extracted links.
- Provides colored terminal output for better readability.

**Dependencies:**
- `urllib`: For handling URL requests.
- `BeautifulSoup`: For parsing HTML content.
- `colorama`: For colored terminal output.
- `pyfiglet`: For generating ASCII art banners.

**Usage:**
1. Clone the repository:
    ```sh
    $ git clone https://github.com/zinzied/HostsUrlsFinder.git
    $ cd HostsUrlsFinder
    ```
2. Install the required dependencies:
    ```bash
    $ sudo pip install -r requirements.txt
    ```
3. Run the tool:
    ```bash
    $ python HostsUrlFinder.py URL
    ```
    Replace `URL` with the webpage you want to extract links from.

**Script Breakdown:**

1. **Imports and Initialization:**
    - The script imports necessary libraries for handling URL requests, parsing HTML, and providing colored terminal output.
    - `colorama` is initialized to enable colored output.

2. **ASCII Art and Banner:**
    - Uses `pyfiglet` to create ASCII art for the banner.
    - The `banner` function displays the ASCII art and a legend for different link types.

3. **Usage and Start Functions:**
    - `usage` function displays how to use the script.
    - `start` function validates the input URL and calls the `report` function if the URL is valid.

4. **Link Searching Function:**
    - `searchLinks` function sends a request to the URL, parses the HTML content using BeautifulSoup, and extracts all unique links from `<a href="">` tags.
    - Handles errors gracefully and exits if an error occurs.

5. **Report Function:**
    - `report` function categorizes the extracted links based on their file extensions (e.g., JavaScript, PHP, images, HTML).
    - Generates a report and writes it to a file named `report.txt` using UTF-8 encoding to handle non-ASCII characters.
    - Provides colored terminal output for each link category.

6. **Main Execution:**
    - The script starts by calling the `start` function with command-line arguments.
    - Handles `KeyboardInterrupt` to allow graceful exit.

**Example Output:**
When run, the script will display a banner, extract links from the provided URL, categorize them, and print the categorized links to the terminal with colored output. It will also generate a `report.txt` file with the same information.

**Conclusion:**
HostsUrlsFinder is a simple yet powerful tool for extracting and categorizing links from a webpage. Its use of colored terminal output and detailed reporting makes it a valuable tool for web information gathering and analysis.
---

This description provides a comprehensive overview of the script, its features, usage, and functionality.
### Donations
If you feel like showing your love and/or appreciation for this project, then how about shouting me a coffee or Milk :)

[<img src="https://github.com/zinzied/Website-login-checker/assets/10098794/24f9935f-3637-4607-8980-06124c2d0225">](https://www.buymeacoffee.com/Zied)
