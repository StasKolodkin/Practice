from selenium import webdriver
import pandas

url = 'https://coinmarketcap.com/'

class Coin:
    full_name = ""
    price = ""
    market_cap = ""

driver = webdriver.Chrome(executable_path="C:\\Users\\User\\Downloads\\dr\\chromedriver.exe")
driver.get(url)
driver.execute_script("window.scrollTo(0,1500);")
coins = []
coins_rows = driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')[0:25]
for coin_row in coins_rows:

    new_coin = Coin()
    new_coin.full_name = coin_row.find_elements_by_tag_name('p')[1].text
    new_coin.price = coin_row.find_elements_by_tag_name('span')[2].text
    new_coin.market_cap = coin_row.find_elements_by_tag_name('span')[8].text

    coins.append(new_coin)

driver.__exit__()
df = pandas.DataFrame([vars(coin) for coin in coins])
df.index = df.index + 1
df.to_csv('parsedData.csv', sep=';')
print(df)

def search_coin(coin_name: str):
    search_results = df[df.eq(coin_name).any(1)]
    if(not search_results.empty):
        return search_results
    else:
        return 'Not found'

while True:
    print('Input coin name to get info from dataframe >>', end=" ")
    print(search_coin(str(input())))
