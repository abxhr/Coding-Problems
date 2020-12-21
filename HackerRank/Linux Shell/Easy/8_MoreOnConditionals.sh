read x
read y
read z
if [ $x -eq $y ] || [ $y -eq $z ] || [ $z -eq $x ]
    then
        if [ $((x+y)) -eq $((z*2)) ]
            then
                echo "EQUILATERAL"
            else
                echo "ISOSCELES"
        fi
    else
        echo "SCALENE"
fi