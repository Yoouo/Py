from selenium import webdriver
import re, time, sys, os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
user = 'zy0108'
pwd = 'zy731027'
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
driver = webdriver.Firefox(firefox_options=fireFoxOptions)
#driver = webdriver.Chrome()
driver.get('http://www.yfcp885.com/login')
wait = WebDriverWait(driver, 10)
TheAddList_1 = [5, 6, 7, 8, 15, 16, 17, 18]
TheAddList_2 = [9, 10, 11, 12, 19, 20, 21, 22]
TheAddList_3 = [5, 7, 9, 10, 12, 14, 16]
TheAddList_4 = [6, 8, 9, 10, 11, 13, 15]
TheAddList_5 = [3, 4, 7, 8, 11, 12, 15, 16]
TheAddList_6 = [4, 5, 6, 9, 10, 13, 14, 17]
TheAddList_7 = [10, 13, 14, 17, 18, 21, 22, 23]
start_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
qian = 1
zhong = 2
hou = 3
def LogIn():
    element_user = wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/ul/li[1]/input'))
    )
    element_user.send_keys(user)
    element_pwd = wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/ul/li[2]/input'))
    )
    element_pwd.send_keys(pwd)
    element_click = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/ul/li[3]/a[1]'))
    )
    element_click.click()
    fin_driver = wait.until(
        EC.url_to_be('http://www.yfcp885.com/index')
    )
def wait_to_be_num():
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="fn_getoPenGame"]/tbody[2]/tr[1]/td[2]/i')) #加载第一个
    )
    wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="fn_getoPenGame"]/tbody[2]/tr[2]/td[2]/i')) #加载第二个
    )
def click(x):
    time.sleep(0.3)
    driver.find_element_by_xpath(x).click()
def PrintLog(content):
    with open('D:\log\CqAddThreeStar_' + start_time + '.txt' ,'a') as f:
        f.write(content)
def GetTime():
    wait.until(
        EC.presence_of_all_elements_located((By.XPATH ,'/html/body/div/div[2]/div[1]/div[2]/em'))
    )
    time.sleep(1)
    os.system('cls')
    Time = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/em').text
    if len(Time) != 8:
        sys.exit()
    sys.stdout.write('新疆和值3  :' + Time + '\n')
    sys.stdout.flush()
    if Time == '00:00:01':
        time.sleep(4)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/span').click()
    return int(Time[-5] + Time[-4]) * 60 + int(Time[-2] + Time[-1])
def waitTime(nowTime ,l ,h = 230):
    while True:
        if nowTime > l and nowTime < h:
            return nowTime
        else:
            if nowTime == 230:
                driver.refresh()
            nowTime = GetTime()
def EitherBuyList(method):
    EitherList = [0, 0, 0, 0, 0, 0, 0]
    wait_to_be_num()
    WinningNum = re.compile('class="numbers">(.*?)<').findall(driver.page_source)
    for i in range(1, 8):
        BuyFlag = True
        if i == 1:
            TheAddList = TheAddList_1
        elif i == 2:
            TheAddList = TheAddList_2
        elif i == 3:
            TheAddList = TheAddList_3
        elif i == 4:
            TheAddList = TheAddList_4
        elif i == 5:
            TheAddList = TheAddList_5
        elif i == 6:
            TheAddList = TheAddList_6
        elif i == 7:
            TheAddList = TheAddList_7
        for j in range(7):
            if AddNum(WinningNum[j], method) in TheAddList:
                BuyFlag = False
                break
        if BuyFlag:
            EitherList[i - 1] = 1
    return EitherList
def AddNum(x, method):
    TheAdd = 0
    if method == qian:
        for i in range(0, 5, 2):
            TheAdd += int(x[i])
        return TheAdd
    elif method == zhong:
        for i in range(2, 7, 2):
            TheAdd += int(x[i])
        return TheAdd
    elif method == hou:
        for i in range(4, 9, 2):
            TheAdd += int(x[i])
        return TheAdd
def Operation(method, order):
    print("第" + str(order) + "组符合")
    PrintLog("第" + str(order) + "组符合\n")
    print("\a")
    method_xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[' + str(method + 3) + ']'
    method = wait.until(
        EC.presence_of_element_located((By.XPATH, method_xpath))
    )
    method.click()
    method_child = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[2]/li[2]/div/a[1]'))
    )
    method_child.click()
    if order == 1:
        TheAddList = TheAddList_1
        percent = '36'
    elif order == 2:
        TheAddList = TheAddList_2
        percent = '36'
    elif order == 3:
        TheAddList = TheAddList_3
        percent = '36'
    elif order == 4:
        TheAddList = TheAddList_4
        percent = '31'
    elif order == 5:
        TheAddList = TheAddList_5
        percent = '36'
    elif order == 6:
        TheAddList = TheAddList_6
        percent = '36'
    elif order == 7:
        TheAddList = TheAddList_7
        percent = '36'
    for i in TheAddList:
        position_xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/ul/li/div/div/a[' + str(i) + ']'
        click(position_xpath)
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/p/select/option[3]')
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/a')
    click('/html/body/div/div[2]/div[2]/div[1]/div[2]/div[3]/p/label[2]')
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/ul/li[3]')
    time.sleep(1)
    try:
        click('/html/body/div[2]/div[2]/div/div/div[2]/span')
    except: pass
    week_num = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[1]/tbody/tr[3]/td/input'))
    )
    week_num.send_keys(Keys.CONTROL + 'a')
    week_num.send_keys('8')
    rate = wait.until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[2]/tbody/tr[2]/td/input[2]'))
    )
    rate.send_keys(Keys.CONTROL + 'a')
    rate.send_keys(percent)
    #times = wait.until(
    #    EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[3]/table[1]/tbody/tr[4]/td/input'))
    #)
    #times.send_keys(Keys.CONTROL + 'a')
    #times.send_keys('2')
    click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/div[1]/a')
def Buy(order):
    money_xpath = '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[2]/p/em[2]'
    wait.until(
        EC.presence_of_all_elements_located((By.XPATH ,money_xpath))
    )
    money = driver.find_element_by_xpath(money_xpath).text
    if order == 1:
        x = '64.80'
    elif order == 2:
        x = '64.80'
    elif order == 3:
        x = '64.00'
    elif order == 4:
        x = '66.40'
    elif order == 5:
        x = '64.00'
    elif order == 6:
        x = '65.60'
    elif order == 7:
        x = '65.60'
    if money == x:
        click('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/a')
        click('/html/body/div[2]/div[2]/div/div/div[2]/span[2]')
        sure_last = wait.until(
            EC.element_to_be_clickable((By.XPATH ,'/html/body/div[2]/div[2]/div/div/div[2]/span'))
        )
        sure_last.click()
        time.sleep(1)
def main():
    LogIn()
    while True:
        try:
            url = 'http://www.yfcp885.com/lottery/SSC/1001'
            driver.get(url)
            nowTime = waitTime(GetTime(), 200)
            if nowTime > 200:
                for i in range(1, 4):
                    if i == 1:
                        print("----前三----")
                        PrintLog("----前三----\n")
                    elif i == 2:
                        print("----中三----")
                        PrintLog("----中三----\n")
                    elif i == 3:
                        print("----后三----")
                        PrintLog("----后三----\n")
                    EitherList = EitherBuyList(i)
                    for j in range(1, 8):
                        if EitherList[j - 1]:
                            Operation(i, j)
                            Buy(j)
                        else:
                            print("第" + str(j) + "组不符合")
            PrintLog("\n")
            time.sleep(30)
        except Exception as e:
            time.sleep(40)
if __name__ == '__main__':
    main()