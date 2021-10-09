from textblob import TextBlob

spell = TextBlob("I haie goud spelling")
 
print(spell.correct())

blob = TextBlob("Comment vas-tu?")
 
print(blob.detect_language())

tran = TextBlob("Buongiorno!")
print(tran.translate(to='en'))