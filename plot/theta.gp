set datafile separator ","
set xrange [190:-20]
set yrange [0:200]
set xlabel "theta [deg]"
set ylabel "y [cm]"
set grid
plot "data.csv" using 1:2 with linespoints
