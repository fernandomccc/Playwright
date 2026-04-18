
def test_001_login_successful(login_page):
    login_page.login("user1", "pass1")
    login_page.assert_login_successful()
    


#pytest --headed --slowmo 1000 -k test_001_login_successful