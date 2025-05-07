from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.cnblogs.com/yiruliu/p/14728088.html")
    page.screenshot(path="screenshot.png", full_page=True) # 截图
    print(page.title())
    page.wait_for_timeout(1000)
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)