# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time

sbis_site = "https://sbis.ru/"
driver = webdriver.Chrome()

try:
    print('Перейти на https://sbis.ru/')
    driver.get(sbis_site)
    time.sleep(2)

    print('Перейти в раздел "Контакты"')
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    contacts.click()
    time.sleep(2)

    print('Найти баннер "Тензор", кликнуть по нему')
    banner = driver.find_element(By.CSS_SELECTOR, '[class="sbisru-Contacts__logo-tensor mb-12"]')
    banner.click()
    time.sleep(1)

    print('Перейти на https://tensor.ru/')
    driver.switch_to.window(driver.window_handles[1])

    print('Проверить, что есть блок новости "Сила в людях"')
    news_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    assert news_block.is_displayed(), 'Блок новости "Сила в людях" отсутствует'

    print('Перейти в этом блоке в "Подробнее" и убедиться, что открывается https://tensor.ru/about')
    about_button = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-link.tensor_ru-Index__link[href="/about"]')
    action_chains = ActionChains(driver)
    about_button.send_keys("\n")
    time.sleep(2)
    assert driver.current_url == 'https://tensor.ru/about', "Неверный адрес сайта"
finally:
    driver.quit()


