@ECHO off
echo A COLOSSAL DIRECTORY
for A in a b c d e f g h i j k l m n o p q r s t u v w x y z
do
	mkdir A
	cd A
	
	for B in a b c d e f g h i j k l m n o p q r s t u v w x y z 
	do
		mkdir B
	done
	cd ..

pause
