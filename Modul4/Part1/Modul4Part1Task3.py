import re
text = input()
sentences = re.split(r'[.?!]+',text)
for sentence in sentences:
    sentences = [s for s in sentences if s.strip()]
print(f"Количество предложений: {len(sentences)}")