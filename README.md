# Py-FOAAS-cli

A Python implementation of the simple CLI tool to interact with FOaaS (Fuck Off as a Service) API. Originally implemented in **Go** by **Palash Nigam** ([**@palash25**](https://github.com/palash25)).

Please check out the original implementation (in Go) by **Palash Nigam** ([palash25/foaas-cli](https://github.com/palash25/foaas-cli)) and please :star: star the repo.

***

<p align="center">
  <img src="https://raw.githubusercontent.com/IamRaviTejaG/py-foaas-cli/master/assets/fuck.gif" />
</p>

## Installation
```bash
git clone https://github.com/IamRaviTejaG/py-foaas-cli.git
cd py-foaas-cli
pip install .
```

## Usage
The usage is a little different from the original Go implementation. There exists only one command `fuck` with all other options.

To view the version info:
```bash
python cli.py fuck version
```

To view all the possible operations in JSON format:
```bash
python cli.py fuck operations
```
To view in simple text instead:
```bash
python cli.py fuck
```

### Known Issues
1. **ModuleNotFoundError**: Running `pip install .` doesn't work as the `fucks` folder doesn't get copied while installing. This has something to do with the `setup.py` file. Any PRs are awaited and appreciated.

***
### If you like/love this Python implementation, please do consider giving :star: :star: stars to the this repository and also to th original repository here (https://github.com/palash25/foaas-cli).
