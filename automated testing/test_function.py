from src.RunProcessClass import RunTest
# from src.BuildClass import column
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

Column_Position_list = ['jss81', 'jss87', 'jss93', 'jss99', 'jss130', 'jss145']
Reaction_Position_first = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[4]/span'
Reaction_Position_middle = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[5]/span'
Reaction_Position_last = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[6]/span'
Reaction_Position_email = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[7]/span'
Reaction_Position_phone = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[8]/div[1]/div/div[2]/div/span'
Reaction_Position_ma = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[8]/div[2]/div/div/div[2]/div/span'
Reaction_Position_list = [Reaction_Position_first, Reaction_Position_middle, Reaction_Position_last,
                          Reaction_Position_email, Reaction_Position_phone, Reaction_Position_ma]
web_address = "https://acy.com/en/open-live-account"
PATH = "/Users/hsinyulin/chromedriver"  # chromedriver這個執行檔的所在位置

driver = webdriver.Chrome(PATH)
driver.get(web_address)  # open the website

driver.implicitly_wait(8)  # 讓網頁、彈跳視窗跑一下
LanguageXPath = '//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[2]/div[1]'
EnglishXPath = '//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]'
driver.find_element(By.XPATH, LanguageXPath).click()  # 點開語言選單
driver.find_element(By.XPATH, EnglishXPath).click()  # 點選English

driver.find_element(By.CLASS_NAME, 'button').click()  # 點擊confirm

def test_FirstName():
    # driver = webdriver.Chrome(PATH)
    # driver.get(web_address)  # open the website
    #
    # driver.implicitly_wait(8)  # 讓網頁、彈跳視窗跑一下
    # LanguageXPath = '//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[2]/div[1]'
    # EnglishXPath = '//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]'
    # driver.find_element(By.XPATH, LanguageXPath).click()  # 點開語言選單
    # driver.find_element(By.XPATH, EnglishXPath).click()  # 點選English
    #
    # driver.find_element(By.CLASS_NAME, 'button').click()  # 點擊confirm

    col_position = Column_Position_list[0]
    reaction_position = Reaction_Position_list[0]
    test_text = ["", "123", "Simon"]

    FirstName = RunTest(driver, col_position, reaction_position, test_text)
    Result = FirstName.run()


    assert Result[test_text[0]] == 'This field is required*'
    assert Result[test_text[1]] == 'Invalid first name.(max length 40)'
    assert Result[test_text[2]] == ''


def test_MiddleName():
    col_position = Column_Position_list[1]
    reaction_position = Reaction_Position_list[1]
    test_text = ["", "123", "Simon"]

    MiddleName = RunTest(driver, col_position, reaction_position, test_text)
    Result = MiddleName.run()

    assert Result[test_text[0]] == ''
    assert Result[test_text[1]] == ''
    assert Result[test_text[2]] == ''


def test_LastName():
    col_position = Column_Position_list[2]
    reaction_position = Reaction_Position_list[2]
    test_text = ["", "123", "Simon"]

    LastName = RunTest(driver, col_position, reaction_position, test_text)
    Result = LastName.run()

    assert Result[test_text[0]] == 'This field is required*'
    assert Result[test_text[1]] == 'Invalid last name.(max length 80)'
    assert Result[test_text[2]] == ''

def test_Email():
    col_position = Column_Position_list[3]
    reaction_position = Reaction_Position_list[3]
    test_text = ['', '123', '123@gmail.com']

    Email = RunTest(driver, col_position, reaction_position, test_text)
    Result = Email.run()

    assert Result[test_text[0]] == 'This field is required*'
    assert Result[test_text[1]] == 'The email format is wrong'
    assert Result[test_text[2]] == ''

def test_Phone():
    col_position = Column_Position_list[4]
    reaction_position = Reaction_Position_list[4]
    test_text = ['', '29290740#123', '(02)29202920']

    Phone = RunTest(driver, col_position, reaction_position, test_text)
    Result = Phone.run()

    assert Result[test_text[0]] == 'This field is required*'
    assert Result[test_text[1]] == 'The phone format is wrong'
    assert Result[test_text[2]] == ''

def test_MobileAuthentication():
    col_position = Column_Position_list[5]
    reaction_position = Reaction_Position_list[5]
    test_text = ['', '@@', '123']

    MA = RunTest(driver, col_position, reaction_position, test_text)
    Result = MA.run()

    assert Result[test_text[0]] == 'This field is required*'
    assert Result[test_text[1]] == 'The authentication code is wrong'
    assert Result[test_text[2]] == ''


