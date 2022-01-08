from selenium import webdriver
from selenium.webdriver.common.by import By
from src.BuildClass import column

class RunTest:
    def __init__(self, driver, col_position, reaction_position, test_text):
        self.driver = driver
        self.col_pos = col_position
        self.reaction_pos = reaction_position
        self.text = test_text


    def run(self):
        # PATH = "/Users/hsinyulin/chromedriver"  # chromedriver這個執行檔的所在位置
        # driver = webdriver.Chrome(PATH)
        # driver.get(self.web)  # open the website
        #
        # driver.implicitly_wait(8)  # 讓網頁、彈跳視窗跑一下
        # LanguageXPath = '//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[2]/div[1]'
        # EnglishXPath = '//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]'
        # driver.find_element(By.XPATH, LanguageXPath).click()  # 點開語言選單
        # driver.find_element(By.XPATH, EnglishXPath).click()  # 點選English
        #
        # driver.find_element(By.CLASS_NAME, 'button').click()  # 點擊confirm

        Text = self.text
        Result = {}

        for i in range(len(Text)):
            Col = column(self.driver, self.col_pos, self.reaction_pos, Text[i])
            Result_Text = Col.fill_col()
            # print('FirstName Result: '+Result_Text)
            # Result.append(Result_Text)
            Result[Text[i]] = Result_Text

        return Result
