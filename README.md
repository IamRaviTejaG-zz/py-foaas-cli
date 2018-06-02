# Py-FOAAS-cli

A Python implementation of the simple CLI tool to interact with FOaaS (Fuck Off as a Service) API. Originally implemented in **Go** by **Palash Nigam** ([**@palash25**](https://github.com/palash25)).

Please check out the original Go implementation by **Palash Nigam** ([palash25/foaas-cli](https://github.com/palash25/foaas-cli)) and please :star: star the repo.

***

<p align="center">
  <img src="https://github.com/IamRaviTejaG/py-foaas-cli/blob/master/assets/fuck.gif" />
</p>

## Installation
```bash
git clone https://github.com/IamRaviTejaG/py-foaas-cli.git
cd py-foaas-cli
pip install .
```

## Usage
The usage is a little different from the original Go implementation. There exists only one command `fuck` with all other options.

```
pyfoaas fuck immensity Ravi
```
Would print:
```
You can not imagine the immensity of the FUCK I do not give. - Ravi
```

To view the version info:
```bash
pyfoaas fuck version
```

To view all the possible operations in JSON format:
```bash
pyfoaas fuck operations
```
To view in simple text instead:
```bash
pyfoaas fuck
```

***
### If you like this Python implementation, please do consider giving :star: :star: stars to this repository and also to the original repository here (https://github.com/palash25/foaas-cli).
