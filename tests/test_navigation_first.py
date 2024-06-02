from pages.sbis_home_page import SbisHomePage
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_home_page import TensorHomePage
from pages.tensor_about_page import TensorAboutPage


def test_navigation_first(driver):
    sbis_home = SbisHomePage(driver)
    sbis_contacts = SbisContactsPage(driver)
    tensor_home = TensorHomePage(driver)
    tensor_about = TensorAboutPage(driver)

    driver.get("https://sbis.ru/")
    sbis_home.go_to_contacts_page()
    sbis_contacts.click_tensor_banner()
    sbis_home.switch_to_new_tab()

    assert "Сила в людях" in tensor_home.get_power_in_people().text, "Не найден заголовок 'Сила в людях'"
    tensor_home.click_more_link_in_about_block()

    assert "https://tensor.ru/about" in driver.current_url

    assert tensor_about.check_size_of_work_images() == 1, "Фотографии раздела 'Работаем' разного размера"


def test_change_region(driver):
    region = 'Камчатский край'
    sbis_home = SbisHomePage(driver)
    sbis_contacts = SbisContactsPage(driver)

    driver.get("https://sbis.ru/")
    sbis_home.go_to_contacts_page()

    contacts = sbis_contacts.take_contacts_list()
    assert len(contacts) != 0, 'Список партнеров пуст'

    sbis_contacts.click_region_banner()

    sbis_contacts.change_region()

    assert region in driver.title, 'Title страницы не изменился'
    assert '41' in driver.current_url, 'Current url не изменился'

    assert sbis_contacts.get_region_name() == region

    contacts_after_change = sbis_contacts.take_contacts_list()
    assert contacts_after_change != contacts, 'Список партнеров не изменился'



