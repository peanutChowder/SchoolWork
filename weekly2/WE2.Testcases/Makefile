now:
	make biased
	make histo

histo:
	python3 test11.py > out.11
	diff out.11 correct/test11.txt
#
	python3 test12.py > out.12
	diff out.12 correct/test12.txt
#
	python3 test13.py > out.13
	diff out.13 correct/test13.txt
#
	python3 test14.py > out.14
	diff out.14 correct/test14.txt
#
	python3 test15.py > out.15
	diff out.15 correct/test15.txt
#
	python3 test16.py > out.16
	diff out.16 correct/test16.txt
#
	python3 test17.py > out.17
	diff out.17 correct/test17.txt
#
	python3 test18.py > out.18
	diff out.18 correct/test18.txt
#
	python3 test19.py > out.19
	diff out.19 correct/test19.txt
#
	python3 test20.py > out.20
	diff out.20 correct/test20.txt

biased:
	python3 test01.py > out.01
	diff out.01 correct/test01.txt
#
	python3 test02.py > out.02
	diff out.02 correct/test02.txt
#
	python3 test03.py > out.03
	diff out.03 correct/test03.txt
#
	python3 test04.py > out.04
	diff out.04 correct/test04.txt
#
	python3 test05.py > out.05
	diff out.05 correct/test05.txt
#
	python3 test06.py > out.06
	diff out.06 correct/test06.txt
#
	python3 test07.py > out.07
	diff out.07 correct/test07.txt
#
	python3 test08.py > out.08
	diff out.08 correct/test08.txt
#
	python3 test09.py > out.09
	diff out.09 correct/test09.txt
#
	python3 test10.py > out.10
	diff out.10 correct/test10.txt

clean:
	-rm out.*
