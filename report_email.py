#!/usr/bin/env python3
# Define generate_email and send_email methods by importing necessary libraries.
# Use the following details to pass the parameters to emails.generate_email():

# From: automation@example.com
# To: username@example.com
# Replace username with the username given in the Connection Details Panel on the right hand side.
# Subject line: Upload Completed - Online Fruit Store
# E-mail Body: All fruits are uploaded to our website successfully. A detailed list is attached to this email.
# Attachment: Attach the path to the file processed.pdf

#!/usr/bin/env python3

import os
import datetime
import reports
import emails

# get the current time in GMT
current_date = datetime.datetime.now().strftime('%Y-%m-%d')


def generate_pdf(path):
    pdf = ""
    files = os.listdir(path)
    for file in files:
        if file.endswith(".txt"):
            with open(path + file, 'r') as f:
                inline = f.readlines()
                name = inline[0].strip()
                weight = inline[1].strip()
                pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
    return pdf


if __name__ == "__main__":
    path = "supplier-data/descriptions/"
    title = "Process Updated on " + current_date
    # generate the PDF
    package = generate_pdf(path)
    reports.generate_report("/tmp/processed.pdf", title, package)

    # prepare email
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ["USER"])
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"

    # generate email
    message = emails.generate_email(
        sender, receiver, subject, body, attachment)
    # send email
    emails.send_email(message)
