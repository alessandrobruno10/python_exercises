from rake_nltk import Rake
var = Rake()
text =input("Type in a text you want it to be scored")
var.extract_keywords_from_text(text)
keyword_extracted = var.get_ranked_phrases()
keyword_extracted_with_scores=var.get_ranked_phrases_with_scores()
print(keyword_extracted)
print(keyword_extracted_with_scores)