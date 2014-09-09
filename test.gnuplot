
		set term png size 1200,700 small
		set ylabel "RTT (ms)"
		set xlabel "number of samples"
		set grid
		set yrange [0:*]

		set title "smoothed RTT (RFC 793)"
		set output "test.png"
		plot "out.dat" using 1:2 with steps title "RTT sample", 			"out.dat" using 1:3 with lines title "smoothed RTT", 			"out.dat" using 1:4 with lines title "average RTT", "out.dat" using 1:5 with lines title "average deviation", "out.dat" using 1:6 with lines title "deviation"

