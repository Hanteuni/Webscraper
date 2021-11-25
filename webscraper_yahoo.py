import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver as wd
import re


def csv_file_reader(file_name):
    df = pd.read_csv(file_name)
    return df


def company_statistics(company_name):
    html_text = requests.get('https://finance.yahoo.com/quote/{}/key-statistics?p={}'.
                             format(company_name, company_name)).text
    soup = BeautifulSoup(html_text, 'lxml')
    data = soup.find_all('table', class_="W(100%) Bdcl(c)")
    temp_ls = []
    statistics = {}
    for values in data:
        tables = values.find_all('tr')
        for data in tables:
            if temp_ls:
                statistics[temp_ls[0]] = temp_ls[1]
            temp_ls = []
            table = data.find_all('td')
            for x in table:
                temp_ls.append(x.text)
    return statistics


def company_history_stocks_price(company_name):
    html_text = requests.get('https://finance.yahoo.com/quote/{}/history?'
                             'period1=511056000&period2=1615161600&interval=1mo&filter=history&frequency='
                             '1mo&includeAdjustedClose=true'.format(company_name)).text
    soup = BeautifulSoup(html_text, 'lxml')
    data = soup.find('table', class_="W(100%) M(0)")
    date_ls = []
    numbers = []
    income = {}
    for tables in data:
        for table in tables:
            date_ls.append(table.text[0:12])
            temp_ls = soup.find_all("td", class_="Py(10px) Pstart(10px)")
            for i in range(0, len(temp_ls), 6):
                number = temp_ls[i].text, temp_ls[i + 1].text, \
                         temp_ls[i + 2].text, temp_ls[i + 3].text, \
                         temp_ls[i + 4].text, temp_ls[i + 5].text
                numbers.append(number)
    date_ls = date_ls[1:-1]
    for i in range(len(date_ls)):
        income[date_ls[i]] = numbers[i]
    return income


def company_balance(company_name):
    browser = wd.Chrome()
    browser.minimize_window()
    browser.implicitly_wait(3)
    browser.get("https://finance.yahoo.com/quote/{}/balance-sheet?p={}"
                .format(company_name, company_name))
    browser.find_element_by_name("agree").click()
    browser.refresh()
    browser.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[2]/button').click()
    browser.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[1]/div[2]/button').click()
    source = browser.page_source
    browser.quit()
    soup = BeautifulSoup(source, 'lxml')
    data = soup.find_all('div', class_="D(tbr) fi-row Bgc($hoverBgColor):h")
    # print(soup)
    data_ls = {}
    for line in data:
        for block in line:
            try:
                if re.match("^[a-zA-Z]+.*", block.text):
                    data_ls[block.text] = data
                else:
                    data += block.text
            except AttributeError:
                data += block
    print(data_ls)


if __name__ == '__main__':
    fname = "quotes_2.csv"
    # df = csv_file_reader(fname)
    # statistics = web_scrape_statistics(company_name="NIO")
    # income = company_history_stocks_price(company_name="NIO")
    # company_balance(company_name="NIO")
