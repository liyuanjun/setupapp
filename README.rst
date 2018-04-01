setupapp
========
a simple demo for Python setup test.


Installation
------------

.. way1::
   $ pip install setupapp
.. way2::
   $ git clone https://github.com/amlyj/setupapp.git && cd setupapp && python setup.py install


Help
----

.. cmd::
    setup commands:
        simple demo for python setup.

    Usage:
        setupapp -l
        setupapp -h | --help
        setupapp -v | --version
        setupapp -m
        setupapp -P <port>
        setupapp -H <ip>
        setupapp [-H <ip>] [-P <port>]

    Arguments:
        ip    output ip
        port  output port

    Options:
        -h --help        help.                                                                                                                                    
        -v --version     version.                                                                                                                                   
        -l               print line.                                                                                                                                   
        -m               say hello


Docs
----

    https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi


Requirement
-----------

.. env::
   $ pip install docopt


Test
----

.. cmd::
   $ setupapp -l
   1
	  2
		  3
			  4
				  5

