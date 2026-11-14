import time

from browser import start_whatsapp
from chat_reader import get_recent_messages
from ai import generate_reply


AUTO_SEND = True
MONITOR_INTERVAL = 2
CHAT_HISTORY_LIMIT = 30


def send_reply(page, reply):

    try:
        composer = page.locator(
            '[data-testid="conversation-compose-box-input"]:visible'
        )

        if composer.count() == 0:
            composer = page.locator(
                'footer [contenteditable="true"]:visible'
            )

        if composer.count() == 0:
            print("[ERROR] Message input not found!")
            return False

        composer.last.fill(reply)
        composer.last.press("Enter")

        print("\n[Ryon] Reply sent automatically!")
        print("[Ryon]:", reply)

        return True

    except Exception as error:
        print("[ERROR] Reply sending failed:", error)
        return False


def monitor_chat(page, duration=300):

    print("\n" + "=" * 45)
    print("       RYON AI AUTO-REPLY")
    print("=" * 45)

    # Read existing conversation
    history = get_recent_messages(
        page,
        limit=CHAT_HISTORY_LIMIT
    )

    print("\nRecent conversation:")

    for msg in history:
        print(f'{msg["sender"]}: {msg["message"]}')

    # Mark existing messages as processed
    processed_messages = {
        (
            msg["metadata"],
            msg["message"],
            msg["direction"]
        )
        for msg in history
    }

    print("\nRyon is now monitoring for new messages...")

    start_time = time.monotonic()

    try:

        while time.monotonic() - start_time < duration:

            history = get_recent_messages(
                page,
                limit=CHAT_HISTORY_LIMIT
            )

            for msg in history:

                message_key = (
                    msg["metadata"],
                    msg["message"],
                    msg["direction"]
                )

                # Ignore already processed messages
                if message_key in processed_messages:
                    continue

                processed_messages.add(message_key)

                # Debug message detection
                print(
                    f"\n[DETECTION] Sender: {msg['sender']} | "
                    f"Direction: {msg['direction']} | "
                    f"Message: {msg['message']}"
                )

                # Ignore outgoing messages
                if msg["direction"] != "incoming":
                    print("[INFO] Ignoring non-incoming message.")
                    continue

                if not msg["message"].strip():
                    continue

                print("\n" + "=" * 45)
                print("NEW INCOMING MESSAGE")
                print("=" * 45)

                print("Sender:", msg["sender"])
                print("Message:", msg["message"])

                # Get updated conversation context
                current_history = get_recent_messages(
                    page,
                    limit=CHAT_HISTORY_LIMIT
                )

                print("\n[Ryon] Thinking...")

                try:
                    reply = generate_reply(current_history)

                except Exception as error:
                    print("[GEMINI ERROR]", error)
                    continue

                if not reply:
                    print("[ERROR] Gemini couldn't generate a reply.")
                    continue

                print("\nGenerated reply:")
                print(reply)

                if AUTO_SEND:
                    send_reply(page, reply)

            time.sleep(MONITOR_INTERVAL)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

    print("\nRyon monitoring session completed!")


def main():

    print("=" * 45)
    print("          RYON AI CHATBOT")
    print("=" * 45)

    playwright, context, page = start_whatsapp()

    try:

        print("\nWhatsApp connected successfully!")

        input(
            "\nOpen your desired WhatsApp conversation "
            "and press Enter..."
        )

        minutes = int(
            input("Monitoring duration (minutes): ")
        )

        if minutes <= 0:
            print("Invalid duration.")
            return

        monitor_chat(
            page,
            duration=minutes * 60
        )

    finally:

        print("\nClosing WhatsApp session...")

        context.close()
        playwright.stop()


if __name__ == "__main__":
    main()