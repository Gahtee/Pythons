from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

link = input('Qual o link do primeiro lote do seu leilão?: ')

options = Options()
options.headless = False
#options.add_argument("--window-size=1920,1200")

DRIVER_PATH = 'PONHA O LOCAL DO SEU CHROMEDRIVER AQUI'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
f= open("database.txt","w+")

driver.get(link)
sleep(5)
f.write("item|qntd|lote\n")

lotes = -1+len(driver.find_elements("xpath", '/html/body/sle-app/div/main/portal-wrapper/edital-wrapper/lote/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/span[1]/span/ul/li'))
for n in range (1, lotes+1):
    rows = len(driver.find_elements("xpath", '/html/body/sle-app/div/main/portal-wrapper/edital-wrapper/lote/div[1]/div[2]/div[2]/div/div/table/tbody/tr'))
    cols = len(driver.find_elements("xpath", '/html/body/sle-app/div/main/portal-wrapper/edital-wrapper/lote/div[1]/div[2]/div[2]/div/div/table/tbody/tr[1]/td'))
    for r in range(1, rows+1):
        for p in range(4, 0, -2):
            value = driver.find_element("xpath", "/html/body/sle-app/div/main/portal-wrapper/edital-wrapper/lote/div[1]/div[2]/div[2]/div/div/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
            f.write(value+'|')
        f.write(str(n)+"\n")
    print("Lote {} Concluído".format(n))
    driver.find_element("xpath", "/html/body/sle-app/div/main/portal-wrapper/edital-wrapper/lote/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/span[1]/button[2]/span").click()
    sleep(5)

f.close()
driver.quit()
