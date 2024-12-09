from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demo.opencart.com.gr/index.php?route=account/login")
driver.maximize_window()
time.sleep(1)

# 1.Login with credentials created in Lab
edit_box=driver.find_element(By.ID,"input-email").send_keys("bindhi@gmail.com")
time.sleep(1)
edit_box=driver.find_element(By.NAME,"password").send_keys("Ch@56789")
time.sleep(1)
edit_box=driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div/form/input').click()
time.sleep(1)

# 2.Go to 'Components' tab and click
# To go to main page
edit_box=driver.find_element(By.XPATH,'//*[@id="logo"]/h1/a').click()
time.sleep(1)
# components
edit_box=driver.find_element(By.XPATH,'//*[@id="menu"]/div[2]/ul/li[3]/a').click()
time.sleep(1)

#3. Select 'Monitors'
# monitor
edit_box=driver.find_element(By.XPATH,'//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li[2]/a').click()
time.sleep(1)

#4. Select 25 from 'Show' dropdown
# select 25
edit_box=driver.find_element(By.XPATH,'//*[@id="input-limit"]/option[2]').click()
time.sleep(1)

#5. Click on 'Add to cart' for the first item
# add to cart
edit_box=driver.find_element(By.XPATH,'//*[@id="content"]/div[3]/div[1]/div/div[2]/div[2]/button[1]/i').click()
time.sleep(1)

#6.Click on 'Specification' tab
#7. Verify details present on the page
# specification
edit_box=driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[1]/ul[2]/li[2]/a').click()
time.sleep(1)

#8.Click on 'Add to Wish list' button.
#9.Verify message 'Success: You have added Apple Cinema 30" to your wish list!'
# add to wishlist
edit_box=driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/button[1]/i').click()
time.sleep(1)

#10. Enter 'Mobile' in Search'textbox.
# search box
edit_box=driver.find_element(By.NAME,"search").send_keys("Mobile")
time.sleep(1)

#11 . Click on 'Search' button
# search
edit_box=driver.find_element(By.XPATH,'//*[@id="search"]/span/button/i').click()
time.sleep(1)

#12 . Click on 'Search in product descriptions' check box
# Search in product descriptions
edit_box=driver.find_element(By.NAME,"description").click()
time.sleep(1)
# Search
edit_box=driver.find_element(By.ID,"button-search").click()
time.sleep(1)

#13 . Click on link 'HTC Touch HD' for the mobile 'HTC Touch HD'
# HTC Touch HD
edit_box=driver.find_element(By.XPATH,'//*[@id="content"]/div[3]/div[1]/div/div[2]/div[1]/h4/a').click()
time.sleep(1)

#14 . Clear '1' from 'Qty' and enter '3'
# Quantity changes to 3
edit_box=driver.find_element(By.ID,"input-quantity").clear()
edit_box=driver.find_element(By.ID,"input-quantity").send_keys("3")
time.sleep(1)

#15 . Click on 'Add to Cart' button
#16 . Verify success message 'Success: You have added HTC Touch HD to your shopping cart!'
# Add to cart
edit_box=driver.find_element(By.ID,"button-cart").click()
time.sleep(1)

#17 . Click on 'View cart' button adjacent to search button
#18 . Verify Mobile name added to the cart
# view cart
edit_box=driver.find_element(By.XPATH,'//*[@id="cart-total"]').click()
time.sleep(1)

#19 . Click on 'Checkout' button
# Check out
edit_box=driver.find_element(By.XPATH,'//*[@id="cart"]/ul/li[2]/div/p/a[2]/strong').click()
time.sleep(1)

#20 . Click on 'My Account' dropdown
# My account
edit_box=driver.find_element(By.XPATH,'//*[@id="top-links"]/ul/li[2]/a').click()
time.sleep(1)

#21 . Select 'Logout' from dropdown
#logout
edit_box=driver.find_element(By.XPATH,'//*[@id="top-links"]/ul/li[2]/ul/li[5]/a').click()
time.sleep(15)


