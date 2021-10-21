You work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. When each supplier has new products for your store, they give you an image and a description of each product.

Given a bunch of images and descriptions of each of the new products, you’ll:

Write a script that summarizes and processes sales data into different categories 
Upload the new products to your online store. Images and descriptions should be uploaded separately, using two different web endpoints.

Send a report back to the supplier, letting them know what you imported.
Generate a PDF using Python
Automatically send a PDF by email 

Since this process is key to your business's success, you need to make sure that it keeps running! So, you’ll also:

Run a script on your web server to monitor system health.
Send an email with an alert if the server is ever unhealthy.
Write a script to check the health status of the system 

https://googlecoursera.qwiklabs.com/focuses/52114 

1. Fetch supplier data - 12/10/2021 - DONE
    a. download the images - download_drive_file.sh
        i. sudo chmod +x ~/download_drive_file.sh
    b. ./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz
    c. tar xf ~/supplier-data.tar.gz
    d. cat ~/supplier-data/descriptions/007.txt
2. Working with supplier images 12/10/2021 - changeImage.py  - DONE
    a. sudo chmod +x ~/changeImage.py
    b. ./changeImage.py
    c.file ~/supplier-data/images/003.jpeg
3. Upload images to the web server - 12/10/2021 - example_upload.py - supplier_image_upload.py - DONE
    a. [linux-instance-IP-Address]/upload
    b. cat ~/example_upload.py
    c. sudo chmod +x ~/example_upload.py
    d. ./example_upload.py
    e. nano ~/supplier_image_upload.py
    f. sudo chmod +x ~/supplier_image_upload.py
    g. ./supplier_image_upload.py
4. Upload the descriptions - 13/10/2021
    a. run.py
    b. supplier-data/descriptions
    c. http://[linux-instance-external-IP]/fruits 
5. Generate PDF report and send the report through email - 14/10/2021
    a. reports.py
    b. report_email.py
    c. call the main method which will process the data and call the generate_report method from the reports module
6. Health check - health_check.py - 15/10/2021
    a. sudo apt install stress
    b. crontab -e