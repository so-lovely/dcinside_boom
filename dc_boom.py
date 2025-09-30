from playwright.sync_api import sync_playwright
import time

number = [str(i) for i in range(1,10)]
hex_number = ['a','b','c','d','e','f']

def btn_request(context, page, value:str):
    try:
        context.add_cookies([
        {
            "name": "fRiP",
            "value": value,
            "domain": ".dcinside.com",
            "path": "/",
        }])
        print(f"쿠키: {value}")
        print("버튼이 나타날 때까지 대기 중...")
        button = page.wait_for_selector(
            "button.btn_recom_up",
            state="visible",
            timeout=1000
        )
        print("버튼 찾음! 클릭 시도 중...")
        button.click(force=True)
        print("클릭완료")  
    except Exception as e:
        print("버튼 클릭 실패:", e)

def main():
    print(number)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        print("test")
        url = input("추천할 게시글 URL:")
        url = url.strip()
        context = browser.new_context(
        )
        page = context.new_page()
        page.goto(url)
        page.wait_for_load_state("networkidle")
        value = "7fef8268b4826be836ea98e64e"
        temp = ""
        for h in hex_number:
            temp = value[:-1] + h
            btn_request(context, page, temp)

        for h in hex_number:
            temp = value[:3] + h + value[4:]    
            btn_request(context, page, temp)
        for i in number:
            temp = value[:-3] + i + value[-2:]
            btn_request(context, page, temp)
        for i in number:
            temp = value[:5] + i + value[6:]
            btn_request(context, page, temp)
        for h in hex_number:
            temp = value[:-7] + h + value[-6:]
            btn_request(context, page, temp)
        print("끝")
        time.sleep(5)
        browser.close()
if __name__ == "__main__":
    main()