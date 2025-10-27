import tkinter
text1 = tkinter.Text(height=5, width=30)
text1.pack(side='left')
scrollbar1 = tkinter.Scrollbar()
scrollbar1.pack(side='right', fill='y')
#vyplní s ním celý voľný priestor v rozsahu osi y
scrollbar1.config(command=text1.yview)
#po posunutí sa posunie aj obsah text1
text1.config(yscrollcommand=scrollbar1.set)
#po posunutí obsahu text1 sa posunie aj scrollbar1
f = open('score.txt', 'r')
for riadok in f:
    text1.insert('end', riadok)
f.close()

text1.mainloop()