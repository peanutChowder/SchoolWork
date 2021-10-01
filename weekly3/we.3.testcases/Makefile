### Expects freq.py to be in same directory as Makefile
test:
	python3 freq.py case1
	diff case1.out output.expected/case1.out
#
	python3 freq.py case2
	diff case2.out output.expected/case2.out
#
	python3 freq.py case3
	diff case3.out output.expected/case3.out
#
	python3 freq.py case4
	diff case4.out output.expected/case4.out
#
	python3 freq.py case5
	diff case5.out output.expected/case5.out
#
	python3 freq.py case6
	diff case6.out output.expected/case6.out
#
	python3 freq.py case7
	diff case7.out output.expected/case7.out

link:
	-ln -s input/case1 .
	-ln -s input/case2 .
	-ln -s input/case3 .
	-ln -s input/case4 .
	-ln -s input/case5 .
	-ln -s input/case6 .
	-ln -s input/case7 .

clean:
	-rm *.out
	-rm case1 case2 case3 case4 case5 case6 case7
	-make link
