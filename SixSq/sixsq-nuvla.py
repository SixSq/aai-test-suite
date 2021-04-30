#!/usr/local/bin/python


from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://nuvla.io/ui/
    page.goto("https://nuvla.io/ui/")

    # Go to https://nuvla.io/ui/sign-in
    page.goto("https://nuvla.io/ui/sign-in")

    # Click //div[normalize-space(.)='or sign in with:']/form[2][normalize-space(@action)='https://nuvla.io/api/session']/button/i
    page.click("//div[normalize-space(.)='or sign in with:']/form[2][normalize-space(@action)='https://nuvla.io/api/session']/button/i")
    # assert page.url == "https://ds.acc.aai.geant.org/ds/?entityID=https%3A%2F%2Fproxy.acc.aai.geant.org%2Fmetadata%2Focre-backend.xml&return=https%3A%2F%2Fproxy.acc.aai.geant.org%2Focre%2Fdisco"

    # Click //a[normalize-space(.)='Login with  GÉANT Test IdP']
    # with page.expect_navigation(url="https://idp.devtest.eduteams.org/module.php/core/loginuserpass.php?AuthState=_f482ef9fe778aace8e03e4d4e1e585afcb19267bec%3Ahttps%3A%2F%2Fidp.devtest.eduteams.org%2Fsaml2%2Fidp%2FSSOService.php%3Fspentityid%3Dhttps%253A%252F%252Fproxy.acc.aai.geant.org%252Fmetadata%252Focre-backend.xml%26RelayState%3DHzg8R8paJxxAXTcA%26cookieTime%3D1619772189"):
    with page.expect_navigation():
        page.click("//a[normalize-space(.)='Login with  GÉANT Test IdP']")

    # Click input[name="username"]
    page.click("input[name=\"username\"]")

    # Fill input[name="username"]
    page.fill("input[name=\"username\"]", "ocre-test")

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "ocre-test")

    # Click text=/.*Login.*/
    # with page.expect_navigation(url="https://nuvla.io/ui/welcome"):
    with page.expect_navigation():
        page.click("text=/.*Login.*/")

    # Click text="oidc-geant:9515e65f4…"
    # with page.expect_navigation(url="https://nuvla.io/ui/profile"):
    with page.expect_navigation():
        page.click("text=\"oidc-geant:9515e65f4…\"")

    # Click text=/.*user/6670a78f-87f7-4c64-b493-3.*/
    # with page.expect_navigation(url="https://nuvla.io/ui/api/user/6670a78f-87f7-4c64-b493-362502acc84c"):
    with page.expect_navigation():
        page.click("text=/.*user/6670a78f-87f7-4c64-b493-3.*/")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)