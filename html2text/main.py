import os
import re

# Third party
import requests
import tiktoken
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from markdownify import markdownify as md
from llama_index.core.node_parser import TokenTextSplitter


def parse_url(link: str) -> str:
    try:
        resp = requests.get(link)
        if resp.status_code != 200:
            print(f"unexpected status code when getting {link}: {resp.status_code}")
            exit(0)

        # Filter and parse HTML
        soup = BeautifulSoup(resp.text, "html.parser")
        # Update relative URLs to absolute URLs
        for a_tag in soup.find_all("a", href=True):
            a_tag["href"] = urljoin(link, a_tag["href"])
        # Remove unwanted tags like 'script', 'style', etc.
        for script in soup(["script", "style", "noscript"]):
            script.extract()
        filtered_html = str(soup)

        # Convert HTML to Markdown
        html = md(filtered_html)

        # Remove consecutive newlines and return
        return re.sub(r"\n+", "\n", html).strip()
    except Exception as e:
        print(f"Error in parse_url: {e}")
        exit(0)


# Begin execution

link = os.getenv("url")
if link is None:
    print("please provide a URL")
    exit(1)

splitter = TokenTextSplitter(
    chunk_size=20000,
    chunk_overlap=10,
    tokenizer=tiktoken.encoding_for_model("gpt-4").encode)
print(splitter.split_text(parse_url(link))[0])
