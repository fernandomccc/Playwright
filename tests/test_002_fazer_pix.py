def test_002_fazer_pix(login_page, pix_page, home_page, common_page):
    login_page.login("user1", "pass1")
    login_page.assert_login_successful()
    home_page.acessar_menu("Fazer Pix")
    pix_page.fazer_pix("123.456.789-00", "10,00")
    pix_page.assert_pix_realizado()
    common_page.voltar_para_home()
    common_page.assert_text("4.990,00")
    home_page.acessar_menu("Ver Extrato")
    common_page.assert_text("Pix para 123.456.789-00 - R$ -10,00")





    #  pytest --headed --slowmo 400 -k test_002_fazer_pix