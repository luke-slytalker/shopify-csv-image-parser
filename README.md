# shopify-csv-image-parser
Recently did a project for a client where they were migrating away from Shopify onto a different platform.  
The exported CSV from Shopify includes links to product images, but it's on the Shopify CDN, so eventually those files won't be available (importing with those links does no good).

Scripted this up real quick to strip the image urls from the CSV file (and truncate any trailing ?v=a45er4eras sort of stuff that may cause issues with the download)

This script--one by one--grabs the image URL (making sure it's not just a blank entry), downloads the image, and stores it in a temp folder.
