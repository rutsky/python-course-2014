all:
	pygmentize -l pycon -f html -O full,style=pastie,encoding=utf-8 -o practice01_1_answer.html practice01_1_answer.pycon
	pygmentize -l pycon -f html -O full,style=pastie,encoding=utf-8 -o practice01_2_answer.html practice01_2_answer.pycon
	rst2html.py practice01.rst > practice01.html

clean:
	rm -f practice01.html practice01_1_answer.html practice01_2_answer.html
