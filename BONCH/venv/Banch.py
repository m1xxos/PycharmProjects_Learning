from selenium import webdriver
from time import sleep

class BonchBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.messages = []
        self.messages_new = list()
        self.messages_id = []
        self.page = 1
        self.count = 0

    def login(self):
        self.driver.get('https://lk.sut.ru/cabinet/?login=no')
        sleep(2)
        email = self.driver.find_element_by_xpath('//*[@id="users"]')
        email.send_keys('bulynin.misha@gmail.com')
        password = self.driver.find_element_by_xpath('//*[@id="parole"]')
        password.send_keys('1234567')
        login_btn = self.driver.find_element_by_xpath('//*[@id="logButton"]')
        login_btn.click()


    def messages_click(self):
        sleep(2)
        messages = self.driver.find_element_by_xpath('//*[@id="menu_li_840"]')
        messages.click()

    def messages_get(self):
        sleep(2)
        messages_new = []
        message_box = self.driver.find_element_by_xpath('//*[@id="mytable"]/tbody')
        message_list = message_box.find_elements_by_tag_name('tr')
        messages = [name.find_elements_by_tag_name('a') for name in message_list]
        for name in messages:
            for name2 in name:
                messages_new.append(name2)
        self.messages.append([name.get_attribute('href') for name in messages_new])


    def next_page(self):
        page = self.page
        if self.page == 1:
            pass
        elif self.page == 2:
            page = 4
        elif self.page == 3:
            page = 4
        else:
            page = 5
        next_page = self.driver.find_element_by_xpath(f'//*[@id="table_mes"]/center/a[{page}]')
        self.page += 1
        next_page.click()
        sleep(2)


bot = BonchBot()
bot.login()
bot.messages_click()
while bot.page < 5:
    bot.messages_get()
    bot.next_page()
file = open("files.txt", "w")
for lines in bot.messages:
        print(*lines, file=file, sep='\n')

file.close()
bot.driver.close()

