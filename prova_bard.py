import requests
from bs4 import BeautifulSoup

def get_opinion(url):
  """
  Connects to Llama and mines opinion from a webpage.

  Args:
    url: The URL of the webpage to mine opinion from.

  Returns:
    A string containing the mined opinion.
  """

  # Get the HTML content of the webpage.
  response = requests.get(url)
  html_content = response.content

  # Parse the HTML content.
  soup = BeautifulSoup(html_content, 'html.parser')

  # Extract the text content of the webpage.
  text_content = soup.get_text()

  # Send the text content to Llama and get the mined opinion.
  llama_response = requests.post('https://api.llama.ai/mine_opinion', json={'text': text_content})
  mined_opinion = llama_response.json()#['opinion']

  return mined_opinion

# Example usage.
mined_opinion = get_opinion('https://en.wikipedia.org/wiki/Gabriele_D%27Annunzio')
print(mined_opinion)
