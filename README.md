# docker-compose-sort

docker-compose-sort reorders the lines in `docker-compose.yml` to conform to a specific predetermined order. It's like [isort](https://pycqa.github.io/isort/) for [Docker Compose](https://docs.docker.com/compose/). Comments are preserved.

The Docker Compose order enforced by this project via `template.yaml` is inspired by the order used in [Compose file reference | Docker](https://docs.docker.com/reference/compose-file/) and [LinuxServer.io](https://www.linuxserver.io/), although neither follow a consistent order themselves.

## Installation

This package is is not yet published on [PyPI](https://pypi.org/). To install:
```
$ git clone https://github.com/k4j8/docker-compose-sort.git
$ pip install --editable docker-compose-sort/
```

Installing with `editable` above allows for easy updates like so:
```
$ cd docker-compose-sort/
$ git pull
```

## Usage

The following is given from `docker-compose-sort --help`:
```
usage: docker-compose-sort [-h] [--write] [filepath]

Opinionated sort for restructuring Docker Compose YAML sections to a standardized order. By default, output is
written to stdout.

positional arguments:
  filepath    Path to file to format

options:
  -h, --help  show this help message and exit
  --write     Edit file in-place
```

## Contributing

Feedback is welcome! Ways to contribute include:
- Suggestions to the order of arguments in Docker Compose template
- Report a bug
- Recommendations on new features
- Suggestions to improve documentation and print statement readability

Pull requests are welcome as well, but please open an issue first describing the change to ensure it will be merged if it is a new feature or significant change. When submitting PRs, please try to conform to the following style guides:
- Python code style: [PEP8](https://www.python.org/dev/peps/pep-0008/)
- Commit message formatting: [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
- Packaging: [Python Packaging User Guide](https://packaging.python.org/), [setuptools](https://setuptools.pypa.io/en/latest/index.html#)
- Release versioning: [Semantic Versioning](https://semver.org/)

## Comparison to Similar Projects

| Feature             | docker-compose-sort (this package) | [yaml-compose-sorter] | [compose_format] | [dockerComposeSort]     | [Docker Compose Linter] |
| ------------------- | ---------------------------------- | --------------------- | ---------------- | ----------------------- | ----------------------- |
| Sorting method      | ✅ YAML template                   | Defined in code       | Defined in code  | Alphabetically          | n/a                     |
| Levels of sorting   | ✅ All                             | Top level + Services  | Top 2 levels     | All, but alphabetically | n/a                     | 
| Installation method | pip                                | VS Code               | pip, Docker      | Python                  | Node.js, Docker, NPM    |

[yaml-compose-sorter]: https://github.com/SashaBusinaro/yaml-compose-sorter
[compose_format]: https://github.com/funkwerk/compose_format
[dockerComposeSort]: https://github.com/Jeshuah71/dockerComposeSort
[Docker Compose Linter]: https://github.com/zavoloklom/docker-compose-linter
