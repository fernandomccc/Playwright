import time
def test_003_contratar_emprestimo(login_page, emprestimos_page, home_page, common_page):
    login_page.login("user1", "pass1")
    login_page.assert_login_successful()
    home_page.acessar_menu("Empréstimos")
    common_page.assert_text("Empréstimos - Empréstimos Pré-aprovados")
    emprestimos_page.selecionar_valor_emprestimo("2.000,00")
    emprestimos_page.clicar_contratar_emprestimo()
    common_page.assert_text("A transação foi concluída com sucesso. Você pode voltar para a página principal e continuar suas operações.")
    common_page.voltar_para_home()
    common_page.assert_text("Saldo atual: R$ 7.000,00")
    home_page.acessar_menu("Ver Extrato")
    common_page.assert_text("Empréstimo contratado - R$ 2000,00")

  


# pytest --headed --slowmo 400 -k test_003_contratar_emprestimo