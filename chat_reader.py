import re


def get_recent_messages(page, limit=15):

    messages = page.locator('[data-testid="msg-container"]')

    chat_area = page.locator(
        '[data-testid="conversation-panel-messages"]'
    )

    chat_box = chat_area.bounding_box()

    if not chat_box:
        print("[ERROR] Could not detect WhatsApp chat area.")
        return []

    chat_center = chat_box["x"] + (chat_box["width"] / 2)

    total = messages.count()
    history = []

    start = max(0, total - limit)

    for i in range(start, total):

        message = messages.nth(i)

        message_box = message.bounding_box()

        if not message_box:
            continue

        message_center = (
            message_box["x"] + message_box["width"] / 2
        )

        # Detect direction using horizontal position
        if message_center > chat_center:
            direction = "outgoing"
        else:
            direction = "incoming"

        # Extract message text
        text_parts = message.locator(
            '[data-testid="selectable-text"]'
        ).all_text_contents()

        message_text = " ".join(text_parts).strip()

        if not message_text:
            continue

        # Extract sender
        metadata_element = message.locator(
            '[data-pre-plain-text]'
        ).first

        metadata = ""

        if metadata_element.count() > 0:
            metadata = metadata_element.get_attribute(
                "data-pre-plain-text"
            ) or ""

        match = re.search(r'\]\s*(.*?):\s*$', metadata)

        sender = match.group(1).strip() if match else "Unknown"

        history.append({
            "sender": sender,
            "message": message_text,
            "direction": direction,
            "metadata": metadata
        })

    return history