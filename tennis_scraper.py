from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import csv


options = webdriver.ChromeOptions() 
options.add_argument("--start-maximized")
# options.add_argument("--headless")

driver = webdriver.Opera(executable_path="/Users/aldrin0n9/Documents/Python Projects/operadriver", options = options)
array = []
# for x in range(1, 501):
#     driver.get("https://www.ultimatetennisstatistics.com/rankingsTable")
    
#     time.sleep(2)
    
#     driver.find_element_by_xpath('//*[@id="rankingsTable-header"]/div/div/div[5]/div[1]/button').click()
#     driver.find_element_by_xpath('//*[@id="rankingsTable-header"]/div/div/div[5]/div[1]/ul/li[4]/a').click()
    
#     time.sleep(2)
#     html = driver.find_element_by_tag_name('html')
#     html.send_keys(Keys.END)
    
#     time.sleep(2)
    
#     driver.find_element_by_xpath('//*[@id="rankingsTable"]/tbody/tr[' + str(x) + ']/td[4]/a').click()
    
#     time.sleep(2.5)
    
#     driver.find_element_by_xpath('//*[@id="matchesPill"]').click()
    
#     time.sleep(2)
    
#     driver.find_element_by_xpath('//*[@id="matchesStats"]').click()
    
#     time.sleep(2)
    
#     serve = driver.find_element_by_xpath('//*[@id="matchesStatsOverview"]/div/div[1]/table/tbody/tr[3]/th[1]').text
    
#     time.sleep(2)
    
#     driver.find_element_by_xpath('//*[@id="matchesStatsTabs"]/li[6]/a').click()
    
#     time.sleep(2)
    
#     matches_won = driver.find_element_by_xpath('//*[@id="matchesStatsMatches"]/div/div[2]/table/tbody/tr[3]/th[1]').text
    
#     name = driver.find_element_by_xpath("/html/body/h3").text
#     temp = [[name, serve, matches_won]]
#     with open('players.csv', 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(temp)
    
#     print("Inserted" + name)
array = []
with open('players.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        array.append(row)

for x in range(1, 100):
    driver.get("https://www.ultimatetennisstatistics.com/rankingsTable")
    
    time.sleep(2)
    
    driver.find_element_by_xpath('//*[@id="rankingsTable-header"]/div/div/div[5]/div[1]/button').click()
    driver.find_element_by_xpath('//*[@id="rankingsTable-header"]/div/div/div[5]/div[1]/ul/li[4]/a').click()
    
    time.sleep(2)
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    
    time.sleep(2)
    
    driver.find_element_by_xpath('//*[@id="rankingsTable"]/tbody/tr[' + str(x) + ']/td[4]/a').click()
    
    time.sleep(2.5)
    
    driver.find_element_by_xpath('//*[@id="matchesPill"]').click()
    
    time.sleep(2)
    
    driver.find_element_by_xpath('//*[@id="matchesStats"]').click()
    
    time.sleep(2)
    
    ace = driver.find_element_by_xpath('//*[@id="matchesStatsOverview"]/div/div[1]/table/tbody/tr[1]/th[1]').text
    double_fault = driver.find_element_by_xpath('//*[@id="matchesStatsOverview"]/div/div[1]/table/tbody/tr[2]/th[1]').text
    
    time.sleep(2)
    
    driver.find_element_by_xpath('//*[@id="matchesStatsTabs"]/li[4]/a').click()
    
    time.sleep(2)
    
    return_percentage = driver.find_element_by_xpath('//*[@id="matchesStatsReturn"]/div/div[2]/table/tbody/tr[1]/th[1]').text
    
    array[x].append(ace)
    array[x].append(double_fault)
    array[x].append(return_percentage)
    
    with open('players1.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([array[x]])
    
    print("Inserted " + str(x))
# with open('players.csv', 'w', newline='') as file:
#    writer = csv.writer(file)
#    writer.writerows([['Player name', 'Serve Percentage', 'Win percentage']])

# with open('players1.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows([['Player name', 'Serve Percentage', 'Win percentage', 'Ace', 'DF', 'Return']])
