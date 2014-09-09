import random
import math
import os

gain = 0.1
average = 60
num_samples = 50

samples = []
for i in range(0, num_samples):
	samples.append(math.floor(random.normalvariate(average, 10)))

srtt = 0
with open('rfc793-naive.dat', 'w+') as f:
	for i in range(0, num_samples):
		rtt = samples[i]
		srtt = math.floor(rtt * gain + srtt * (1.0 - gain))

		print >>f, '%d\t%f\t%f\t%f' % (i, rtt, srtt, average)

srtt = 0
with open('rfc793-init.dat', 'w+') as f:
	for i in range(0, num_samples):
		rtt = samples[i]
		if srtt == 0: srtt = rtt
		else: srtt = math.floor(rtt * gain + srtt * (1.0 - gain))

		print >>f, '%d\t%f\t%f\t%f' % (i, rtt, srtt, average)

srtt = 0
with open('rfc793-init-round.dat', 'w+') as f:
	for i in range(0, num_samples):
		rtt = samples[i]
		if srtt == 0: srtt = rtt
		else: srtt = round(rtt * gain + srtt * (1.0 - gain), 0)

		print >>f, '%d\t%f\t%f\t%f' % (i, rtt, srtt, average)

srtt = 0
g = 1
with open('rfc793-weight-round.dat', 'w+') as f:
	for i in range(0, num_samples):
		rtt = samples[i]

		if 1.0 / g < gain:
			effective_gain = gain
		else:
			effective_gain = 1.0 / g

		srtt = round(rtt * effective_gain + srtt * (1.0 - effective_gain), 0)

		print >>f, '%d\t%f\t%f\t%f\t%f' % (i, rtt, srtt, average, effective_gain)

		if 1.0 / g > gain:
			g += 1


srtt = 0
g = 1
with open('rfc793-weight-fp.dat', 'w+') as f:
	for i in range(0, num_samples):
		rtt = samples[i]

		if 1.0 / g < gain:
			effective_gain = gain
		else:
			effective_gain = 1.0 / g

		srtt = rtt * effective_gain + srtt * (1.0 - effective_gain)

		if 1.0 / g > gain:
			g += 1

		print >>f, '%d\t%f\t%f\t%f' % (i, rtt, srtt, average)

with open('moving_average.gnuplot', 'w+') as out:
	out.write('''
		set term png size 1200,700 small
		set ylabel "RTT (ms)"
		set xlabel "number of samples"
		set grid
		set yrange [0:*]

		set title "smoothed RTT (RFC 793)"
		set output "rfc_793_rto-naive.png"
		plot "rfc793-naive.dat" using 1:2 with steps title "RTT sample", \
			"rfc793-naive.dat" using 1:3 with lines title "smoothed RTT", \
			"rfc793-naive.dat" using 1:4 with lines title "average RTT"

		set title "smoothed RTT (RFC 793) with special case initialization"
		set output "rfc_793_rto-init.png"
		plot "rfc793-init.dat" using 1:2 with steps title "RTT sample", \
			"rfc793-init.dat" using 1:3 with lines title "smoothed RTT", \
			"rfc793-init.dat" using 1:4 with lines title "average RTT"

		set title "smoothed RTT (RFC 793) with special case initialization and rounding"
		set output "rfc_793_rto-init-round.png"
		plot "rfc793-init-round.dat" using 1:2 with steps title "RTT sample", \
			"rfc793-init-round.dat" using 1:3 with lines title "smoothed RTT", \
			"rfc793-init-round.dat" using 1:4 with lines title "average RTT"

		set title "smoothed RTT (RFC 793) weighted rounding"
		set output "rfc_793_rto-weight-round.png"
		plot "rfc793-weight-round.dat" using 1:2 with steps title "RTT sample", \
			"rfc793-weight-round.dat" using 1:3 with lines title "smoothed RTT", \
			"rfc793-weight-round.dat" using 1:4 with lines title "average RTT"

		set title "smoothed RTT (RFC 793) weighted floating point"
		set output "rfc_793_rto-weight-fp.png"
		plot "rfc793-weight-fp.dat" using 1:2 with steps title "RTT sample", \
			"rfc793-weight-fp.dat" using 1:3 with lines title "smoothed RTT", \
			"rfc793-weight-fp.dat" using 1:4 with lines title "average RTT"
		''')

os.system('gnuplot moving_average.gnuplot');

