moving_average
==============

an implementation of integer moving average algorithm.

To use, construct a ``moving_average`` object. The template argument is the
inverse of the gain factor (only values > 1 makse sense). For each sameple,
call ``add_sample()``. To query the current estimated average, call ``mean()``.
To query the current estimated average deviation, call ``avg_deviation()``.

For more information, see `this blog post`_.

.. _`this blog post`: http://blog.libtorrent.org/2014/09/running-averages/

