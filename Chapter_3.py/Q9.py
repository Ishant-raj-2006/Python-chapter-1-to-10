# Wap for fill in latter template given below with name and date.
letter='''Dear <|Name
            You are selected !
            <|date|>'''
print(letter.replace("<|Name","Ishant").replace("<|date|>","19 Nov 2025"))
