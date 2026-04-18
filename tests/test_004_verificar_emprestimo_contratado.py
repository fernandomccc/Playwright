def test_004_verificar_emprestimo_contratado(login_page, emprestimos_page, home_page, common_page):
    login_page.login("user1", "pass1")
    login_page.assert_login_successful()
    home_page.acessar_menu("Empréstimos")
    common_page.assert_text("Empréstimos - Empréstimos Pré-aprovados")
    emprestimos_page.selecionar_valor_emprestimo("2.000,00")
    emprestimos_page.clicar_contratar_emprestimo()
    common_page.assert_text("A transação foi concluída com sucesso. Você pode voltar para a página principal e continuar suas operações.")
    common_page.voltar_para_home()
    common_page.assert_text("Saldo atual: R$ 7.000,00")
    home_page.acessar_menu("Empréstimos")
    common_page.assert_text("Você já tem um empréstimo contratado em andamento. Novos empréstimos não estão disponíveis.")




    # pytest --headed --slowmo 400 -k test_004_verificar_emprestimo_contratado