set datafile separator ","
set xrange [-200:200]
set yrange [0:200]
set xlabel "x [cm]"
set ylabel "y [cm]"
set grid
plot "data.csv" using 3:4 with points
