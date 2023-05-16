from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from msedge.selenium_tools import EdgeOptions, Edge

edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument('headless')
edge_options.add_argument('disable-gpu')
driver = Edge(executable_path='C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe', options=edge_options)

# Set up Selenium driver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Edge(service = Service(verbose = True))
driver.get("https://www.dwds.de/wb/Auto")

# service = Service(verbose = True)

# Find the element using the XPath
element = driver.find_element_by_xpath("/html/body/main/div[1]/div/div[1]/div[2]/div/div[9]/div")

# Get the content of the element
content = element.text

# Print the content
print(content)

# Close the Selenium driver
driver.quit()
