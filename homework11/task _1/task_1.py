# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

sbis_site = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
tensor_site = 'https://tensor.ru/'
tensor_title = 'Тензор — IT-компания'
about_site = 'https://tensor.ru/about'
about_title = 'О компании | Тензор — IT-компания'

driver = webdriver.Chrome()  # Создаем экземпляр браузера
driver.maximize_window()  # Максимизируем окно браузера
sleep(2)
try:
    """Переходим на сайт https://sbis.ru/"""
    driver.get(sbis_site)
    sleep(2)
    assert driver.current_url == sbis_site, 'Открыт не тот сайт'
    assert driver.title == sbis_title, 'Неверный заголовок вкладки'

    """Переходим в раздел Контакты"""
    btn_contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-link[href="/contacts"]')
    assert btn_contacts.text == 'Контакты', 'Название кнопки отличается от ожидаемого'
    assert btn_contacts.is_displayed(), 'Кнопка не отображается'
    btn_contacts.click()
    sleep(2)

    """Проверяем, что действительно перешли в раздел Контакты"""
    assert 'https://sbis.ru/contacts' in driver.current_url, 'Открыт не раздел Контакты'
    assert 'СБИС Контакты' in driver.title, 'Неверный заголовок вкладки'

    """Клик по баннеру Тензор"""
    tensor_logo = driver.find_element(By.CSS_SELECTOR, '#contacts_clients .sbisru-Contacts__logo-tensor')
    tensor_logo.is_displayed(), 'Баннер Тензор не отображается'
    tensor_logo.click()
    sleep(2)

    """Переходим на сайт https://tensor.ru/"""
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == tensor_site, 'Открыт не тот сайт'
    assert driver.title == tensor_title, 'Неверный заголовок вкладки'

    """Проверяем, что есть блок новости 'Сила в людях'"""
    news_power_in_people = driver.find_element(By.CSS_SELECTOR,
                                               '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    driver.execute_script("arguments[0].scrollIntoView();",
                          driver.find_element(By.CSS_SELECTOR,
                                              '.tensor_ru-Index__block4-content.tensor_ru-Index__card'))
    sleep(2)
    assert news_power_in_people.text == 'Сила в людях', 'Название блока новостей не соответствует ожидаемому'
    news_power_in_people.is_displayed(), 'Блок новостей "Сила в людях" не отображается'

    """Клик в блоке 'Сила в людях' по кнопке 'Подробнее'"""
    btn_more = driver.find_element(By.CSS_SELECTOR, '[href="/about"].tensor_ru-link')
    assert btn_more.text == 'Подробнее', 'Название кнопки не соответствует ожидаемому'
    btn_more.is_displayed(), 'Кнопка "Подробнее" не отображается'
    btn_more.click()
    sleep(2)

    """Проверяем, что открывается https://tensor.ru/about"""
    assert driver.current_url == about_site, 'Открыт не тот сайт'
    assert driver.title == about_title, 'Неверный заголовок вкладки'
    sleep(2)
finally:
    driver.quit()
