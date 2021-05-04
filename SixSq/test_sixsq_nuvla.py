import logging
from playwright.sync_api import sync_playwright


def test_sixsq_nuvla_aai(page, username, _password):
    # Go to https://nuvla.io/ui/sign-in
    nuvla = "https://nuvla.io/ui"
    nuvla_login_page = nuvla + "/sign-in"
    page.goto(nuvla_login_page)
    assert page.title().startswith("Nuvla")
    logging.info(f'Successful navigation to service at {nuvla_login_page}')

    valid_cookie = 'com.sixsq.nuvla.cookie'
    assert valid_cookie not in list(map(lambda x: x.get('name'), page.context.cookies()))
    logging.info('There are no active session cookies at the moment. Continuing with login')

    page.click("//div[normalize-space(.)='or sign in with:']/form[2][normalize-space(@action)='https://nuvla.io/api/session']/button/i")
    aai_service_url = "https://ds.acc.aai.geant.org/"
    assert page.url.startswith(aai_service_url)
    logging.info(f"Successful redirection to AAI service at {aai_service_url}")

    with page.expect_navigation():
        page.click("//a[normalize-space(.)='Login with  GÉANT Test IdP']")

    page.click("input[name=\"username\"]")
    logging.info(f'Performing login test with username "{username}"')
    page.fill("input[name=\"username\"]", username)

    page.click("input[name=\"password\"]")
    page.fill("input[name=\"password\"]", _password)

    with page.expect_navigation():
        page.click("text=/.*Login.*/")

    with page.expect_navigation():
        page.click("text=\"Dashboard\"")

    assert valid_cookie in list(map(lambda x: x.get('name'), page.context.cookies()))
    logging.info(f'Cookie {valid_cookie} is now valid. User is logged in')

    page.goto(nuvla_login_page + "/credentials")

    # logout
    page.click("div[role=\"listbox\"]")
    with page.expect_navigation():
        page.click("//div[normalize-space(.)='logout' and normalize-space(@role)='option']")

    assert page.url == nuvla_login_page

    page.close()

