from playwright.sync_api import sync_playwright


def start_whatsapp():

    playwright = sync_playwright().start()

    context = playwright.chromium.launch_persistent_context(
        user_data_dir="./whatsapp_profile",
        headless=False,
        viewport={"width": 1366, "height": 768}
    )

    page = context.pages[0] if context.pages else context.new_page()

    page.goto("https://web.whatsapp.com")

    print("Waiting for WhatsApp Web...")

    input("Scan the QR code if required, then press Enter...")

    print("WhatsApp Web is ready!")

    return playwright, context, page