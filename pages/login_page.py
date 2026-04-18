from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = self.page.get_by_role("textbox", name="Usuário:")
        self.password_input = self.page.get_by_role("textbox", name="Senha:")
        self.login_button = self.page.get_by_role("button", name="Entrar")
        
    def login(self, username, password):
        self.page.goto("https://leogcarvalho.github.io/simulabank/login.html")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        
        
    def assert_login_successful(self):    
        expect(self.page.get_by_role("heading", name="Bem-vindo ao SimulaBank!")).to_be_visible()