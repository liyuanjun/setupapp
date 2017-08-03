# setupapp
> a simple demo for Python setup test.

### environment
```bash
$ pip install docopt
```

### install
```bash
$ git clone https://github.com/amlyj/setupapp.git && cd setupapp && python setup.py install
```
### bash
```bash
[root@node1 setupapp]# setupapp 

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
    -h --help        帮助
    -v --version     版本.
    -l               列表.
    -m               say hello

[root@node1 setupapp]# setupapp -l
 1
	2
		3
			4
				5
[root@node1 setupapp]#
```
