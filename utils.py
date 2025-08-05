import spacy
import fitz
import re

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text

def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    
def extract_keywords(text):
    doc = nlp(text)
    keywords = []

    for token in doc:
        if token.pos_ in ("NOUN", "PROPN", "VERB"):
            lemma = token.lemma_.lower()
            if lemma not in keywords:
                keywords.append(lemma)

    return keywords


def match_score(resume_keywords, jd_keywords):
    common_keywords = []

    for word in resume_keywords:
        if word in jd_keywords and word not in common_keywords:
            common_keywords.append(word)

    if jd_keywords:
        score = len(common_keywords) / len(jd_keywords) * 100
    else:
        score = 0

    return round(score, 2), common_keywords
