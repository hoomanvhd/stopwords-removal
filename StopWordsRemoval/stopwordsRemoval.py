
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import glob, os


Speechpath = "/home/hoomanvhd/Desktop/VideoSample/Video1/VideoTextReadByLine/*.txt"

SpeechTextList = []

counter = 1
for SpeechTextFile in sorted(glob.glob(Speechpath)):
    SpeechEXT = os.path.splitext(SpeechTextFile)
    SpeechTextList.append(SpeechTextFile)


SpeechText = []

for Speech in SpeechTextList:
    with open(Speech, "r") as Speechfile:
        reader = Speechfile.read()
    SpeechText.append(reader)

cnt = 1


stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
for sentence in SpeechText:
    textTokenize = word_tokenize(sentence)
    textClean = [words for words in textTokenize if words not in stop_words]
    print(textClean)

    # if textClean==[]:
    #     a = str(cnt)
    #     os.remove("/home/hoomanvhd/Desktop/VideoSample/TEST2/VideoTextReadByLine/" + a + ".txt")

    cnt += 1


