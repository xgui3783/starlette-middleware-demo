# Demo of reverse order of starlette middleware

## install

```
pip install -r requirement.txt
```

## run

```sh
uvcorn app:app --port 8000
```

then

```sh
curl http://localhost:8000
```

expected output:

```sh
m0 pre
m1 pre
m1 post
m0 post
```

actual output:

```sh
m1 pre
m0 pre
m0 post
m1 post
```