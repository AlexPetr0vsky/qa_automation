from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.EMAIL_REG_FORM)
        email_form.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD_REG_FORM)
        password1.send_keys(password)
        password_confirm = self.browser.find_element(*LoginPageLocators.PASSWORD_REG_FORM_CONFIRM)
        password_confirm.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()

    def should_be_registered(self):
        assert "Thanks for registering!" in self.browser.find_element(*LoginPageLocators.SUCCESS_MESSAGE).text, \
            "User should be registered"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, f"URL '{current_url}' should contains 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is absent"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is absent"
