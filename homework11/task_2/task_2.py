# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from time import sleep

fix_auth_site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
fix_auth_title = 'Вход в личный кабинет'
fix_sbis_site = 'https://fix-online.sbis.ru/'
fix_sbis_title = 'СБИС'
contacts_page = 'https://fix-online.sbis.ru/page/dialogs'
contacts_page_title = 'Контакты'

driver = webdriver.Chrome()  # Создаем экземпляр браузера
driver.maximize_window()  # Максимизируем окно браузера
sleep(2)
try:
    """Переходим на сайт https://fix-online.sbis.ru/"""
    driver.get(fix_sbis_site)
    sleep(3)
    assert driver.current_url == fix_auth_site, 'Открыт не тот сайт'
    assert driver.title == fix_auth_title, 'Неверный заголовок вкладки'

    """Авторизуемся"""
    user_login, user_password = 'mionina', 'qwerty555'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(5)

    """Проверяем, что открывается https://fix-online.sbis.ru/"""
    assert driver.current_url == fix_sbis_site, 'Открыт не тот сайт'
    assert driver.title == fix_sbis_title, 'Неверный заголовок вкладки'

    """Переходим в раздел 'Контакты'"""
    sections_contacts = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"]')
    sections_contacts.click()
    sleep(1)

    menu_contacts = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    assert menu_contacts.text == 'Контакты', 'Название раздела отличается от ожидаемого'
    assert menu_contacts.is_displayed(), 'Раздел не отображается в аккордеоне'
    menu_contacts.click()
    sleep(3)

    """Проверяем, что открылся раздел 'Контакты'"""
    assert driver.current_url == contacts_page, 'Открыт не тот раздел'
    assert driver.title == contacts_page_title, 'Неверный заголовок вкладки'

    """Отправляем сообщение самому себе"""
    btn_plus = driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')
    btn_plus.click()
    sleep(3)

    search_emp = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate__top-area-content input')
    search_emp.send_keys('Ионина Мария')
    sleep(3)

    person = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"][title="Ионина Мария"]')
    person.click()
    sleep(3)

    text = 'Нас учат писать автотесты на языке Python с помощью фреймворка Selenium'
    message_text = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    message_text.send_keys(text)
    send = driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
    send.click()
    sleep(3)

    """Проверяем, что сообщение появилось в реестре"""
    message = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert message.text == text, "В реестре не отображается отправленное сообщение"

    """Удаляем  отправленное сообщение"""
    action_chains = ActionChains(driver)
    action_chains.move_to_element(message)
    action_chains.perform()
    sleep(3)

    btn_delete_msg = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    btn_delete_msg.click()
    sleep(3)

    message = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert message.text != text, 'Сообщение не удалилось'
finally:
    driver.quit()
