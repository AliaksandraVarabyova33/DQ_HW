import re

hwText = """
homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.


"""

tmpL = hwText.splitlines()
tmpL = list(filter(None, tmpL))

tmpS = ""
tmpS2 = ""

for i in tmpL:
    tmpS += i.replace('\xa0 ', "")

sentences = tmpS.split(".")
sentences = list(filter(None, sentences))

additionalSentence = ""

for i in sentences:
         additionalSentence += i.split()[-1]

print(additionalSentence)

for i in sentences:
         tmpS2 += i.lstrip().capitalize() + "."
         if tmpS2.endswith("paragraph."):
             tmpS2 += additionalSentence + '\n\xa0 '

s_new = tmpS2[:-1]

s_new_formatted = re.sub(r'(?<=[.,:])(?=[^\s])', u'\n\xa0 ', s_new)
s_final = s_new_formatted.replace(" iz", " is")

print(s_final)

print(s_final.count(" ") + s_final.count("\xa0"))
