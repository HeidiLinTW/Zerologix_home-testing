# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# import numpy as np
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from src.BuildClass import column

PATH = "/Users/hsinyulin/chromedriver"  # chromedriver這個執行檔的所在位置

Column_Position_list = ['jss81', 'jss87', 'jss93', 'jss99', 'jss130', 'jss145']
Reaction_Position_first = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[4]/span'
Reaction_Position_middle = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[5]/span'
Reaction_Position_last = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[6]/span'
Reaction_Position_email = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[7]/span'
Reaction_Position_phone = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[8]/div[1]/div/div[2]/div/span'
Reaction_Position_ma = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[8]/div[2]/div/div/div[2]/div/span'
Reaction_Position_list = [Reaction_Position_first, Reaction_Position_middle, Reaction_Position_last,
                          Reaction_Position_email, Reaction_Position_phone, Reaction_Position_ma]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    driver = webdriver.Chrome(PATH)
    driver.get("https://acy.com/en/open-live-account")  # open the website

    driver.implicitly_wait(8)  # 讓網頁、彈跳視窗跑一下
    LanguageXPath = '//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[2]/div[1]'
    EnglishXPath = '//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]'
    driver.find_element(By.XPATH, LanguageXPath).click()  # 點開語言選單
    driver.find_element(By.XPATH, EnglishXPath).click()  # 點選English

    driver.find_element(By.CLASS_NAME, 'button').click()  # 點擊confirm

    Text = ["", "123", "Simon"]  # success
    # Text = ["Simon", "123", ""]  # fail
    # Text = ["123"]  # success
    Result = []
    for i in range(len(Text)):
        FirstName = column(driver, Column_Position_list[0], Reaction_Position_list[0], Text[i])
        Result_Text = FirstName.fill_col()
        # print('FirstName Result: '+Result_Text)
        Result.append(Result_Text)
    print('First Name')
    print(Result)

    Result = []
    for i in range(len(Text)):
        MiddleName = column(driver, Column_Position_list[1], Reaction_Position_list[1], Text[i])
        Result_Text = MiddleName.fill_col()
        # print('FirstName Result: '+Result_Text)
        Result.append(Result_Text)
    print('Middle Name')
    print(Result)

    Result = []
    for i in range(len(Text)):
        LastName = column(driver, Column_Position_list[2], Reaction_Position_list[2], Text[i])
        Result_Text = LastName.fill_col()
        # print('FirstName Result: '+Result_Text)
        Result.append(Result_Text)
    print('Last Name')
    print(Result)

    Result = []
    Text = ['', '123', '123@gmail.com']
    for i in range(len(Text)):
        Email = column(driver, Column_Position_list[3], Reaction_Position_list[3], Text[i])
        Result_Text = Email.fill_col()
        # print('FirstName Result: '+Result_Text)
        Result.append(Result_Text)
    print('Email')
    print(Result)

    Result = []
    Text = ['29290740#123', '', '(02)29202920']
    for i in range(len(Text)):
        Phone = column(driver, Column_Position_list[4], Reaction_Position_list[4], Text[i])
        Result_Text = Phone.fill_col()
        # print('FirstName Result: '+Result_Text)
        Result.append(Result_Text)
    print('Phone')
    print(Result)

    Result = []
    Text = ['@@', '', '123']
    for i in range(len(Text)):
        MA = column(driver, Column_Position_list[5], Reaction_Position_list[5], Text[i])
        Result_Text = MA.fill_col()
        # print('FirstName Result: '+Result_Text)
        Result.append(Result_Text)
    print('Mobile Authentication')
    print(Result)

    # if Result_Text != "":
    #     print('FirstName Result: '+Result_Text)
    # else:
    #     print('FirstName success')
    #
    # Text = "123"
    # MiddleName = column(driver, Column_Position_list[1], Reaction_Position_list[1], Text)
    # Result_Text = MiddleName.fill_col()
    # if Result_Text != "":
    #     print('MiddleName Result: '+Result_Text)
    # else:
    #     print('MiddleName success')

    # time.sleep(3)
    driver.quit()  # close the website



    # time.sleep(3)
    # driver.quit()  # close the website






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
