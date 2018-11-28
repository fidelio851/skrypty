#!/bin/sh

echo "Jakie dzialanie chcesz wykonac?"
echo "1) dodawanie\n2)odejmowanie\n3)mnozenie\n4)dzielenie"
read variable
read -p "Wprowadz liczby : " x y

case $variable in
     1)
          answer=$(( x + y ))
          echo $answer
          ;;
     2)
          answer=$(( x - y ))
          echo $answer
          ;;
     3)
          answer=$(( x * y ))
          echo $answer
          ;;
     4)
          answer=$(( x / y ))
          echo $answer
          ;;
     *)
          echo "Niepoprawne dzialanie"
          ;;
esac