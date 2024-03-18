from pathlib import Path
import win32com.client
from datetime import datetime, date
import os
from config import config
from utils import sanitize_filename, log_message

def find_desired_account(accounts, account_email):
    for account in accounts:
        if account.SmtpAddress.lower() == account_email.lower():
            return account
    return None

def process_attachments(attachments, day_dir):
    for attachment in attachments:
        filename = sanitize_filename(attachment.FileName)
        attachment_path = day_dir / filename
        if not attachment_path.exists():
            attachment.SaveAsFile(str(attachment_path))
            log_message(day_dir, f"Saved attachment: {filename}")
            if filename.lower().endswith('.png'):
                os.remove(str(attachment_path))
                log_message(day_dir, f"Removed .png file: {filename}")
        else:
            log_message(day_dir, f"Attachment already exists: {filename}")

def process_email_messages(account, config):
    base_dir_path = Path(config["base_dir_path"])
    sent = account.DeliveryStore.GetDefaultFolder(5)  # Sent Items
    messages = sent.Items
    messages.Sort("[ReceivedTime]", True)  # Sort messages in descending order by received time

    for message in messages:
        received_datetime = message.ReceivedTime
        received_date = received_datetime.date()
        if received_date < date(config["start_year"], config["start_month"], 1):
            continue  # Skip emails received before the specified start date

        subject = message.Subject
        if not any(keyword.lower() in subject.lower() for keyword in config["keywords"]) or \
                any(subject.startswith(prefix) for prefix in config["ignore_prefixes"]):
            continue  # Skip emails that don't match the keyword criteria or are replies

        year_month_dir = base_dir_path / received_date.strftime("%Y-%m")
        timestamp_str = received_datetime.strftime("%Y%m%d_%H%M%S")
        day_dir = year_month_dir / f"{timestamp_str}_{sanitize_filename(subject)}"
        day_dir.mkdir(parents=True, exist_ok=True)

        process_attachments(message.Attachments, day_dir)
        log_message(day_dir, "Processed email successfully.")

def process_emails(config):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    desired_account = find_desired_account(outlook.Session.Accounts, config["account_email"])

    if desired_account is None:
        print("Account not found.")
        return

    process_email_messages(desired_account, config)
    print("Email processing complete.")

if __name__ == "__main__":
    process_emails(config)
