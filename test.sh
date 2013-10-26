echo "Starting..."

random="randomPlay"
greedy="simpleGreedy"
minimax="minimax"
albeta="alphaBeta"
script="python gamePlay.py"
command=""
file=""



command="$script"

num_of_test=$2

get_player_name()
{
    local kname
    case $1 in
        "m") kname="$minimaxi" ;;
        "a") kname="$albeta";;
        "g") kname="$greedy" ;;
        "r") kname="$random";;
        *) echo "INVALID" ;;
    esac

    echo "$kname"
}



player_one=$(get_player_name ${1:0:1})
player_two=$(get_player_name ${1:2:2})


command="$script $player_one $player_two"

echo $command

output_file=""

output_file=${player_one}_vs_${player_two}

echo $output_file

#if [ -e $output_file ]
#then
#    rm $output_file
#fi

echo " " >> $output_file

date >> $output_file

echo $num_of_test
start=1
for (( num=1; num<=$num_of_test; num++ ))
do
    echo "Running test no : $num"
    temp_file="temp_result"
    start=$(date +%s)
    eval $command > $temp_file
    end=$(date +%s)
    diff=$(( $end - $start ))
    ostring=$(tail -1 $temp_file)
    line=$ostring.....Time:$diff
    echo $line
    echo $line >> $output_file
    rm $temp_file
done

echo "Complete"
clear
more $output_file


exit











