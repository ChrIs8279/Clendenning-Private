# get websites
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, unquote, urlparse, parse_qs

# summarizer
from newspaper import Article
from lexrank import LexRank
from lexrank.mappings.stopwords import STOPWORDS
from pathlib import Path
# nltk
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

# stealth
import random
import time

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
    'Mozilla/5.0 (X11; Linux x86_64)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)'
]

EXCLUDED_DOMAINS = ['wikipedia.org', 'pinterest.com', 'quora.com', 'wikihow.com', 'reddit.com']

def test_url(url):
    try:
        article=Article(url)
        article.download()
        article.parse()
        return True if len(article.text.strip()) > 100 else False
    except Exception:
        return False

def search_duckduckgo(query, num_results=3):
    search_url = f"https://html.duckduckgo.com/html/?q={query}"
    headers = {
        'User-Agent': random.choice(USER_AGENTS)
    }
    session = requests.Session()
    response = requests.get(search_url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('.result__a')

    decoded_urls = []
    valid_results = 0
    index = 0

    while valid_results < num_results and index < len(links):
        link = links[index]
        index += 1
        
        raw_url = link.get('href')
        parsed_url = urlparse(raw_url)

        if 'duckduckgo.com' in parsed_url.netloc and '/l/' in parsed_url.path:
            qs = parse_qs(parsed_url.query)
            decoded_url = unquote(qs['uddg'][0]) if 'uddg' in qs else None
        else:
            decoded_url = urljoin(search_url, raw_url)

        if decoded_url and not any(domain in decoded_url for domain in EXCLUDED_DOMAINS):
            print (f'Trying decoded URL: {decoded_url}')
            if test_url(decoded_url):
                decoded_urls.append(decoded_url)
                valid_results += 1
                print(f'✅ Valid result #{valid_results}: {decoded_url}')
            else:
                 print("❌ Failed test or invalid content.")
        time.sleep(random.uniform(1.5, 3.5))

    return decoded_urls

def extract_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return article.title, article.text, article.summary.split('\n')
    except Exception as e:
        print(f"NLP failed for {url}: {e}")
        return "Error" , "Failed to Extract", []
    
def extract_article_with_bs(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').get_text(strip=True) if soup.find('h1') else "No Title Found"


        content_divs = soup.find_all(['div', 'section'], recursive=True)
        text_blocks = []

        for div in content_divs:
            if div.get_text(strip=True) and len(div.get_text(strip=True)) > 200:
                text_blocks.append(div.get_text(" ", strip=True))

        content = "\n\n".join(text_blocks[:3]) if text_blocks else "No Content Found"
        summary = summarize_text(content) if content != "No Content Found" else ['Summary Unavailable']

        return title, content, summary
    except Exception as e:
        print(f"Failed to extract from {url}: {str(e)}")
        return "Error", "Failed to Extract", ['Summary Unavaiable']

def summarize_text(text, num_paragraphs=3, num_sentences=2):
    # Split the text into sentences
    sentences = [s.strip() for s in text.split('. ') if len(s.strip()) > 40 and '.' in s]
    
    # Process LexRank
    documents = [sentences]
    lxr = LexRank(documents, stopwords=STOPWORDS["en"])

    # Get the most important sentences
    summary_sentences = lxr.get_summary(sentences, summary_size=num_sentences, threshold=0.1)

    # Split the text into paragraphs and filter short paragraphs
    paragraphs = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 100]
    
    # Rank paragraphs based on overlap with key sentences
    ranked_paragraphs = sorted(paragraphs, key=lambda p: sum(s in p for s in summary_sentences), reverse=True)
    
    # Get the top N paragraphs
    top_paragraphs = ranked_paragraphs[:num_paragraphs]

    return summary_sentences, top_paragraphs

if __name__ == "__main__":
    query = input("Enter Your Search Keyword(s): ")
    results_url = search_duckduckgo(query)

if results_url:

    max_sites = 3

    for idx, url in enumerate(results_url, start=1):
        print(f'\n🔗 [{idx}] Trying URL: {url}')
        title, full_text, summary = extract_article(url)


        if full_text.startswith("Failed"):
            print(f"🛠️ Falling back to BeautifulSoup for {url}...")
            title, full_text, summary = extract_article_with_bs(url)
        
        if not full_text.startswith('Failed'):
            print(f"\n📰 Title: {title}\n🌐 Source: {url}\n")
            top_sentences, top_paragraphs = summarize_text(full_text)
            print("🧠 Key Sentences:\n")
            for i, sentence in enumerate(top_sentences, 1):
                print(f"{i}. {sentence}")
            print()

            print("\n📄 Top Paragraphs:\n")
            printed = set()
            for para in top_paragraphs:
                if para not in printed:
                    print(para)
                    print()
                    printed.add(para)

        else:
            print(f"❌ Could not extract content from {url}")
        print("-" * 80)

        if idx >= max_sites:
            print("🚫 Max sites reached. Stopping search...")
            time.sleep(3)
            print("Search Stopped")
            break

        cont = input("would you like to continue to the next article? (y/n)").strip().lower()
        if cont != 'y':
            print("Stopping search...")
            time.sleep(3)
            print('Search Stopped')
            break

