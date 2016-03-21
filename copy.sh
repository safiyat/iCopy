if [ $# -ne 2 ]
then
	echo 'Only two parameters permitted.'
	exit
# else
# 	echo $1 $2
fi

SRC=$1
DEST=$2
# echo $SRC $DEST
iFS=$IFS
IFS='
'
i=1
list=`ls $SRC`
for a in
do
	# echo $a
	if [ -f $a ]
	then
		echo $a is a file
		files[$i]=$a
	else
		echo $a is a directory
	fi
done

$IFS=$iFS
