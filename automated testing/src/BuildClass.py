
# class Animal:
#     def __init__(self, name, food):
#         self.name = name  # 屬性
#         self.food = food
#
#     def eat(self):  # 方法
#         print("I am " + self.name + ", I eat " + self.food)
#
#
# first_animal = Animal("cat", "fish")
# first_animal.eat()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class column:
    def __init__(self, driver, column_pos, reaction_pos, test_text):
        self.driver = driver
        self.column_pos = column_pos  # class name
        self.reaction_pos = reaction_pos  # XPATH
        self.test_text = test_text


    def fill_col(self):
        col = self.driver.find_element(By.CLASS_NAME, self.column_pos)
        col.click()  # 點擊欄位
        col.clear()  # 先把欄位清空
        col.send_keys(self.test_text)

        self.driver.find_element(By.CLASS_NAME, "jss85").click()  # 隨便點擊其他地方，警告訊息才會出現
        time.sleep(0.5)

        Reaction = self.driver.find_elements(By.XPATH, self.reaction_pos)
        isReactionPresent = len(Reaction)
        ResultText = ""
        if isReactionPresent > 0:
            # print('exist')
            # Reaction = self.driver.find_element(By.XPATH, self.reaction_pos)
            ResultText = Reaction[0].text
            # print(ResultText)
        # else:
        #     print("doesn't exist")

        return ResultText
