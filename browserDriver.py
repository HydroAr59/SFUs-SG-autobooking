from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os,datetime,calendar

class browser():

    def __init__(self):
        self.now = datetime.datetime.now()
        self.driver = webdriver.Firefox(executable_path=os.getcwd()+"\geckodriver.exe")
        self.month = self.now.month


    def cas_login(self,usern,passw):
        self.driver.get("http://roombooking.surrey.sfu.ca")
        time.sleep(2)

        login_attempt = self.driver.find_element_by_xpath("//input[@value=' Log in ']")
        login_attempt.submit()

        time.sleep(2)
        username = self.driver.find_element_by_id("username")
        password = self.driver.find_element_by_id("password")
        username.send_keys(usern)
        password.send_keys(passw)
        login_attempt2 = self.driver.find_element_by_xpath("//*[@type='submit']")
        login_attempt2.submit()

    def book_room(self,room="43",area="6",time=("7","00")):

        #Gets the date 2 weeks ahead from current day
        if (14 + self.now.day > calendar.monthrange(self.now.year, self.now.month)[1]):
            month = self.month + 1
            day = 14 + self.now.day - calendar.monthrange(self.now.year, self.now.month)[1]
        else:
            month = self.month
            day = 14 + self.now.day

        #print(self.now.hour,type(self.now.hour))
        #print(str(self.now.hour)+":00" > "23:00")

        while(True):
            print(str(self.now.hour)+":"+str(self.now.minute),str(time[0])+":"+str(time[1]), str(self.now.hour)+":"+str(self.now.minute) > str(time[0])+":"+str(time[1]) )
            if( str(self.now.hour)+":"+str(self.now.minute) > str(time[0])+":"+str(time[1]) ):
                break

        self.driver.get(
            "http://roombooking.surrey.sfu.ca/edit_entry.php?room=" + str(room) + "&area=" + str(area) + "&hour="
            + str(time[0]) + "&minute=" + str(time[1]) + "&year=2017&month=" + str(month) + "&day=" + str(day))

        brief = self.driver.find_element_by_id("name")
        brief.send_keys("a")

        endtime = self.driver.find_element_by_id("end_seconds6")
        for option in endtime.find_elements_by_tag_name('option'):
            if (option.text == str(int(time[0])+2)+":"+str(time[1])):
                option.click()
                break

        save = self.driver.find_element_by_name("save_button")
        save.submit()