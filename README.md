# updog
A Watchdog, for Services written in python

## Roadmap
To V1
- [X] comunicate between instances (master/ slave)
- [X] Build a Postgres framework as service
- [X] Custom Resolve/Return for services
- [X] get req as service
- [X] Notify Email
- [X] Examples
- [ ] Tests
- [ ] Docs

Down the Road
- [ ] Notify Discord
- [ ] Notify Telegram
- [ ] post req as service


## test
```bash
python3 -m unittest
```
For additional information, use the -v flag
```bash
python3 -m unittest -v
```

## build and publish to pypi
```bash
python3 setup.py sdist bdist_wheel
twine upload dist/*
```

## Contribute

Contributions are welcome.
For Things to do look in the Issues and at Roadmap.
To contribute fork this repository and create a pull request.

### Setup work enviroment

```bash
pip install -r requirements.txt
```

