import asyncio
from playwright_stealth import Stealth
from playwright.async_api import async_playwright
CHROME_ARGS = [
    "--disable-blink-features=AutomationControlled",
    "--disable-extensions",
    "--disable-infobars",
    "--enable-automation",
    "--no-first-run",
    "--enable-webgl",
]
async def google_search_domains(keyword, useragent):
    # initialize Stealth with Playwright
    async with Stealth().use_async(async_playwright()) as p:
        # launch headless browser
        browser = await p.chromium.launch(headless=True, args=CHROME_ARGS)
        context = await browser.new_context(
            user_agent=useragent,
            locale="da-DK",
            timezone_id="Europe/Copenhagen",
            viewport={"width": 1280, "height": 800},
        )
        page = await context.new_page()
        await page.goto(f"https://www.google.com/search?q={keyword}")
        divs = await page.locator('div[data-id^="atritem-"]').all()
        domains = []
        for div in divs:
            data_id = await div.get_attribute('data-id')
            if data_id and data_id.startswith('atritem-'):
                url = data_id[len('atritem-'):]
                domain = extract_domain(url)
                if domain:
                    domains.append(domain)

        await browser.close()
        return domains
def extract_domain(url):
    # Remove protocol if present
    if url.startswith("http://"):
        url = url[len("http://"):]
    elif url.startswith("https://"):
        url = url[len("https://"):]
    # Remove 'www.' if present
    if url.startswith("www."):
        url = url[len("www."):]
    # Get domain before first '/' or '?'
    end = len(url)
    for sep in ['/', '?']:
        idx = url.find(sep)
        if idx != -1 and idx < end:
            end = idx
    return url[:end]

if __name__ == "__main__":
    keyword = "django docker postgres"
    user_agent = "Mozilla/5.0 (Linux; Android 11; sdk_gphone_x86 Build/RSR1.240422.006; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 GSA/11.13.8.21.x86"
    domains = asyncio.run(google_search_domains(keyword, user_agent))
    print("Google Search Result Domains:")
    for domain in domains:
        print("-", domain)

