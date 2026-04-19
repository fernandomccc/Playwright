from playwright.sync_api import Page, expect

class BoletosPage:
    def __init__(self, page: Page):
        self.page = page
        self.barcode = page.get_by_role("textbox", name="Código de Barras:")
        self.valor = page.get_by_role("textbox", name="Valor:")
        self.pagar_boleto_button = page.get_by_role("button", name="Pagar Boleto")

    def pagar_boleto(self, barcode, valor):
        self.barcode.fill(barcode)
        self.valor.fill(valor)
        self.pagar_boleto_button.click()
    
    def assert_boleto_pago(self):
        expect(self.page.get_by_text("A transação foi concluída com sucesso. " \
        "Você pode voltar para a página principal e continuar suas operações.")).to_be_visible()

  