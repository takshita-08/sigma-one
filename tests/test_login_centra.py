from pages.login import Login

def test_login(page):
    centra = Login(page)
    centra.load_page()
    centra.login("takshita", "Meritech@123")