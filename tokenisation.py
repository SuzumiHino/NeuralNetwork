import re
# import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from nltk.stem.snowball import SnowballStemmer
from sklearn.metrics import classification_report # scikit_learn
import stop_words
import pymorphy2

# df_2019_comment = pd.read_csv(
# 	'user_comments_with_target.csv',
# 	sep=';', encoding='cp1251', low_memory=False
# )
# df_2020_comment = pd.read_csv(
# 	'isu_2020.csv', sep=';', encoding='cp1251', low_memory=False
# )
#
# df_2019_comment = df_2019_comment[['user_comments', 'target']].dropna()
# df_2020_comment = df_2020_comment[['user_comments']].dropna()
#
# df_2019_comment = df_2019_comment[df_2019_comment['target'].isin(['0', '1'])]
# df_2019_comment['target'] = df_2019_comment['target'].astype(int)
# df_2019_comment = df_2019_comment.drop_duplicates('user_comments')
# df_2019_comment = df_2019_comment[
# 	df_2019_comment['user_comments'].apply(lambda x:len(x) > 2)]
# df_2019_comment = df_2019_comment.sort_values('target').reset_index(drop=True)
#
# df_2020_comment = df_2020_comment.drop_duplicates('user_comments')
# df_2020_comment = df_2020_comment[
# 	df_2020_comment['user_comments'].apply(lambda x:len(x) > 2)]
# df_2020_comment = df_2020_comment.reset_index(drop=True)

def stemmer_func(language: str):
	"""
		Function support languages:
			Arabic, Danish, Dutch, English, Finnish, French, German, Hungarian,
			Italian, Norwegian, Porter, Portuguese, Romanian, Russian, Spanish,
			Swedish
	"""
	stemmer = SnowballStemmer(language)
	stop_words_ru = stop_words.get_stop_words(language)
	pm = pymorphy2.MorphAnalyzer()

def clear_txt(txt: str) -> str:
	txt = txt.lower()
	txt = re.sub('[/+_!@#$A-Za-z0-9\n.,:()""«»;-]', ' ', txt)
	new_txt = ''
	for t in txt.split(' '):
		if len(t) > 0:
			new_txt = new_txt + stemmer.stem(t) + ' '
	return new_txt[:-1]
	# for w in new_txt.split(' '):
	# 	pm.parse(w)

text = (
	"текст, просто текст"
)

print(f"Исходник: \n{text}\n")
print(f"Обработанный: \n{clear_txt(txt=text)}")
