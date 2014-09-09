#include "moving_average.hpp"
#include <fstream>
#include <random>

int main()
{
	moving_average<10> avg;

	std::fstream f("out.dat", std::ios::trunc | std::ios::out);
	std::random_device dev;
	std::mt19937 mt(dev());
	const int average = 60;
	std::normal_distribution<> nd(average, 10);

	for (int i = 0; i < 50; ++i)
	{
		int rtt = nd(mt);
		avg.add_sample(rtt);
		f << i << "\t" << rtt << "\t" << avg.mean() << "\t" << average << std::endl;
	}
}
