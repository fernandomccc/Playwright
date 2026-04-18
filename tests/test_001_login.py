
def test_001_login_successful(login_page):
    login_page.login("user1", "pass1")
    login_page.assert_login_successful()
    
def test_002_login_unsuccessful(login_page):
    login_page.login("user11", "pass11")
    login_page.assert_login_unsuccessful()
    


# pytest --headed --slowmo 1000 -k test_001_login_successful

# pytest --headed --slowmo 500 -k test_002_login_unsuccessful