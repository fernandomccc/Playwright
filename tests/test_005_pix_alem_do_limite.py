def test_005_pix_alem_do_limite(login_page, pix_page, home_page, common_page):
    login_page.login("user1", "pass1")
    login_page.assert_login_successful()
    home_page.acessar_menu("Fazer Pix")
    pix_page.fazer_pix("123.456.789-00", "3001,00")
    common_page.assert_text("O valor do Pix não pode ultrapassar R$ 3.000,00. Tente novamente.")


    
    #  pytest --headed --slowmo 400 -k test_005_pix_alem_do_limite