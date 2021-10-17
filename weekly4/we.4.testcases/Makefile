### Expects preprocess.py to be in same directory as Makefile
test:
	python3 preprocess.py < input/case01 > case01.out
	diff case01.out output.expected/case01.expected
#
	python3 preprocess.py < input/case02 > case02.out
	diff case02.out output.expected/case02.expected
#
	python3 preprocess.py < input/case03 > case03.out
	diff case03.out output.expected/case03.expected
#
	python3 preprocess.py < input/case04 > case04.out
	diff case04.out output.expected/case04.expected
#
	python3 preprocess.py keep-digits < input/case05 > case05.out
	diff case05.out output.expected/case05.expected
#
	python3 preprocess.py keep-stops < input/case06 > case06.out
	diff case06.out output.expected/case06.expected
#
	python3 preprocess.py keep-symbols < input/case07 > case07.out
	diff case07.out output.expected/case07.expected
#
	@echo "*** Expect this to fail with message..."
	-python3 preprocess.py not-right > case08.out
	cat case08.out
# Possibly tricky tests
	python3 preprocess.py keep-symbols < input/case09 > case09.out
	diff case09.out output.expected/case09.expected
#
	python3 preprocess.py keep-symbols < input/case10 > case10.out
	diff case10.out output.expected/case10.expected
	

clean:
	-rm *.out
