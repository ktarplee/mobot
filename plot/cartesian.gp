set datafile separator ","
set xrange [-200:200]
set yrange [-50:200]
set xlabel "x [cm]"
set ylabel "y [cm]"
set grid
set isotropic
set label 1 "" at 0, 0 point pt 7 ps 2
plot "data.csv" using 3:4 with linespoints
