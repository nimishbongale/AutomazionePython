# Installation guides

1. Find your suitable chromedriver from [this link](https://chromedriver.chromium.org/downloads) and download it. 
2. Replace it with the default chromedriver already in the repo.  
3. Run the following command from your terminal to install selenium.
    ```python3
    pip install selenium
    ```
 
# How to Run 

1. Run ```python3 ResultScrapper.py```
2. If chrome shows up and says that it is being run by an automated software, then the setup was completed successfully.
3. Once prompted, enter the captcha sequence once, in the terminal. 
4. After a a min or two, once the execution is complete, you may find the results in the csv file opened.
5. To get the results in a sorted order, another code may be written, or instead of directly writing it, storing the information within a dictionary and then sorting it with a key function would also do.
6. Another simpler option would be to open the .csv file in a supporting spreadsheet application and simply sorting it based on SGPA by right clicking on the column head.
