#!/bin/bash
addition(){
    expr $first_number + $second_number
    echo
}
subtraction(){
    expr $first_number - $second_number
    echo
}
multiplication(){
    expr $first_number \* $second_number
    echo 
}
division(){
     if [ $second_number -eq 0 ]
     then
         echo "division by 0 is invalid"
         echo
     else 
         expr $first_number / $second_number
         echo 
     fi 
}

exit_program=0
while [ $exit_program -ne 1 ]
do
     echo "enter the numbers you want to perform operations on: "
     read first_number
     read second_number
     echo "1 - addition"
     echo "2-multiplication"
     echo "3 - division"
     echo "4 - subtraction"
     echo "5- Exit the script"
     read choice
     case $choice in
          1) addition ;; 
          2) multiplication ;;
          3) division ;;
          4) subtraction ;;
          5) exit_program=1;;
          *) echo "invalid choice entered"
      esac
done 
echo "thank you For using the calculator"
