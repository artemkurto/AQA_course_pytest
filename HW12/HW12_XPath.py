from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium_ui.data.page_objects import driver


class CatalogPage:  # Каталог товарів

    def input_value_1_product_send_keys(self, value):
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//app-catalog-product-item-big[1]//input'))).send_keys(value)
        return self

    def input_value_2_product_send_keys(self, value):
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//app-catalog-product-item-big[2]//input'))).send_keys(value)
        return self

    def input_value_3_product_send_keys(self, value):
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//app-catalog-product-item-big[3]//input'))).send_keys(value)
        return self

    def input_value_4_product_send_keys(self, value):
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//app-catalog-product-item-big[4]//input'))).send_keys(value)
        return self

    def input_value_5_product_send_keys(self, value):
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//app-catalog-product-item-big[5]//input'))).send_keys(value)
        return self

    def input_value_6_product_send_keys(self, value):
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//app-catalog-product-item-big[6]//input'))).send_keys(value)
        return self

    @staticmethod
    def get_value_input_product1():
        value = int(driver.find_element(
            By.XPATH, '//app-catalog-product-item-big[1]//input').get_attribute('value'))
        return value

    @staticmethod
    def get_value_input_product2():
        value = int(driver.find_element(
            By.XPATH, '//app-catalog-product-item-big[2]//input').get_attribute('value'))
        return value

    @staticmethod
    def get_value_input_product3():
        value = int(driver.find_element(
            By.XPATH, '//app-catalog-product-item-big[3]//input').get_attribute('value'))
        return value

    @staticmethod
    def get_value_input_product4():
        value = int(driver.find_element(
            By.XPATH, '//app-catalog-product-item-big[4]//input').get_attribute('value'))
        return value

    @staticmethod
    def get_value_input_product5():
        value = int(driver.find_element(
            By.XPATH, '//app-catalog-product-item-big[5]//input').get_attribute('value'))
        return value

    @staticmethod
    def get_value_input_product6():
        value = int(driver.find_element(
            By.XPATH, '//app-catalog-product-item-big[6]//input').get_attribute('value'))
        return value

    def text_limit_value_product(self):
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[2]/div[1]/div/div/div/div[2]/span[text()="
                       "' Кількість замовленого не може перевищувати кількість доступного. ']")))
        return self

    def button_reduce_product_click(self):
        driver.find_element(
            By.XPATH, "//div[2]/div/div/div/div/div[2]/span/button/span[text()='Зменшити']").click()
        return self

    def button_order_1_click(self):
        driver.find_element(
            By.XPATH, "//app-catalog-product-item-big[1]//button/span[text()=' Замовити ']").click()
        return self

    def button_order_2_click(self):
        driver.find_element(
            By.XPATH, "//app-catalog-product-item-big[2]//button/span[text()=' Замовити ']").click()
        return self

    def button_order_3_click(self):
        driver.find_element(
            By.XPATH, "//app-catalog-product-item-big[3]//button/span[text()=' Замовити ']").click()
        return self

    def button_order_4_click(self):
        driver.find_element(
            By.XPATH, "//app-catalog-product-item-big[4]//button/span[text()=' Замовити ']").click()
        return self

    def icon_basket_click(self):
        driver.find_element(By.XPATH, "//div[@class='orders']").click()
        return self

    @staticmethod
    def get_basket_attribute():
        text = WebDriverWait(driver, 30).until(EC.presence_of_element_located((
            By.XPATH, "//app-header-orders//div[@class='text']"))).get_attribute('textContent')
        value = float(text.split()[0].replace(',', '.'))
        return value

    def button_handler_up_product2_click(self, number_of_click=1):
        for _ in range(number_of_click):
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, "//app-catalog-product-item-big[2]//span[contains (@class, 'handler-up')]"))).click()
        return self

    def button_handler_down_product2_click(self, number_of_click=1):
        for _ in range(number_of_click):
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, "//app-catalog-product-item-big[2]//span[contains (@class, 'handler-down')]")
            )).click()
        return self

    @staticmethod
    def get_available_quantity_product_1():
        text = (driver.find_element(By.XPATH, '//app-catalog-product-item-big[1]//div[4]/div[1]/div[1]/div').
                get_attribute('textContent'))
        number = int(text.split()[-1])
        return number

    @staticmethod
    def get_available_quantity_product_3():
        text = (driver.find_element(By.XPATH, '//app-catalog-product-item-big[3]//div[4]/div[1]/div[1]/div').
                get_attribute('textContent'))
        number = int(text.split()[-1])
        return number

    @staticmethod
    def get_available_quantity_product_4():
        text = (driver.find_element(By.XPATH, '//app-catalog-product-item-big[4]//div[4]/div[1]/div[1]/div').
                get_attribute('textContent'))
        number = int(text.split()[-1])
        return number

    def type_order_units_click(self):
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((
                By.XPATH, '//app-catalog-sort/div/app-select-box[1]/div/div[2]'))).click()
        return self

    def type_order_units_pieces_click(self):
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "//nz-option-item[1]/div[contains(text(), 'Штуки')]"))).click()
        return self

    def type_order_units_boxes_click(self):
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "//nz-option-item[2]/div[contains(text(), 'Коробки (кейси)')]"))).click()
        return self

    @staticmethod
    def text_dostupno_korobok():
        text = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(), 'Доступно коробок: ')]")))
        return text

    def text_zamovlennya_u_korobkah_find(self):
        driver.find_element(By.XPATH, "//div[contains(text(), 'Увага ! Замовлення у коробках')]")
        return self

    def button_display_how_list_click(self):
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//app-catalog-view/div/div[2]/button'))).click()
        return self

    def button_display_how_big_products_click(self):
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//app-catalog-view/div/div[1]/button'))).click()
        return self

    def wait_until_visible_products(self):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, '//app-catalog-content-data/div/div')))
        return self

    def wait_until_visible_products_item_small(self):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, '//app-catalog-product-item-small')))
        return self

    # Кількість товара в коробці у второго продукту
    @staticmethod
    def get_value_in_box_product2():
        value = int(driver.find_element(
            By.XPATH, '//app-catalog-product-item-big[2]//div[contains(text(),'
                      ' "Штук у коробці")]/following-sibling::div').get_attribute('textContent'))
        return value

    def open_product1_click(self):
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((
            By.XPATH, '//app-catalog-product-item-big[1]//app-image-loader'))).click()
        return self

    @staticmethod
    def get_product1_name():
        name = driver.find_element(
            By.XPATH, '//app-catalog-product-item-big[1]//p').get_attribute('textContent')
        return name

    def link_how_to_use_click_top(self):
        driver.find_element(
            By.XPATH, "//div[@class='link text' and contains(text(), 'Як користуватись?')]").click()
        return self

    def link_how_to_use_click_bottom(self):
        driver.find_element(
            By.XPATH, "//a[contains(text(), 'Як користуватись?')]").click()
        return self

    def link_rules_click(self):
        driver.find_element(
            By.XPATH, "//a[contains(text(), 'Правила користування сайтом')]").click()
        return self

    def link_delivery_click(self):
        driver.find_element(
            By.XPATH, "//a[contains(text(), 'Оплата та доставка')]").click()
        return self

    def link_refund_click(self):
        driver.find_element(
            By.XPATH, "//a[contains(text(), 'Повернення та обмін')]").click()
        return self

    def link_quality_certificates_click(self):
        driver.find_element(
            By.XPATH, "//div[@class='link ng-star-inserted' and contains(text(), 'Сертифікати якості')]").click()
        return self

    def link_trade_conditions_click(self):
        driver.find_element(
            By.XPATH, "//div[@class='link ng-star-inserted' and contains(text(), 'Торгівельні умови')]").click()
        return self

    def modal_window_trade_conditions(self):
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='ng-star-inserted' and contains(text(), 'Торгівельні умови')]")))
        return self

    def modal_window_promo_propositions(self):
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='ng-star-inserted' and contains(text(), 'Промо пропозиції')]")))
        return self

    def pagination_title1_click(self):
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, "//nz-pagination/li[@title='1']"))).click()
        return self

    def pagination_title3_click(self):
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, "//nz-pagination/li[@title='3']"))).click()
        return self

    def link_promo_proposition_click(self):
        driver.find_element(
            By.XPATH, "//div[@class='link ng-star-inserted' and contains(text(), 'Промо пропозиції')]").click()
        return self
