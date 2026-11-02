from urllib.parse import urljoin

# A function that given the page we scraped (page_url)
# And some link that came from either href="" src="" etc.. (raw_link)
# We take in both and return the full url

def clean_url(page_url: str, raw_link: str) -> str | None:
    if not raw_link:
        return None # Consider how to handle the None in your code

    # remove whitespace
    raw_link = raw_link.strip()

    # block junk schemes often found in HTML
    # these are NOT navigational URLs
    if raw_link.startswith(("javascript:", "mailto:", "tel:", "#")):
        # This is not a link
        return None


    # resolve relative → absolute
    return urljoin(page_url, raw_link)


def getting_absolute_urls_example():

    page_url = "https://example.com/dir/page.html" # Imagine this is the page we are scraping

    links_found = [
        "/arizona.jpg",        # root-relative
        "arizona.jpg",         # relative
        "../arizona.jpg",      # directory traversal
        "https://arizona.edu", # already absolute for another page
        " javascript:void(0)"  # javascript command saying "don't do anything"
    ]

    print("\nPage URL:", page_url)
    print()

    for link in links_found:
        cleaned = clean_url(page_url, link)
        if not cleaned:
            cleaned = "This wasn't a Valid Scraped Link"
        print(f'Scraped Link: "{link}"  ->  Absolute: {cleaned}')


if __name__ == "__main__":
    getting_absolute_urls_example()