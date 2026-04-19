def test_006_pagar_boleto(boletos_page, login_page, home_page, common_page):
    login_page.login("user1", "pass1")
    login_page.assert_login_successful()
    home_page.acessar_menu("Pagar Boletos")
    boletos_page.pagar_boleto("12345678901234567890123456789012345678901234", "100,00")
    boletos_page.assert_boleto_pago()
    common_page.voltar_para_home()
    common_page.assert_text("4.900,00")
    home_page.acessar_menu("Ver Extrato")
    common_page.assert_text("Pagamento de boleto - R$ -100,00")
    common_page.voltar_para_home()
    

    #pytest --headed --slowmo 800 -k test_006_pagar_boleto