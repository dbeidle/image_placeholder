# image_placeholder
This will generate a placeholder image by calling it within a `<img />`

## Install:
Clone the repo:

```sh
git clone https://github.com/dbeidle/image_placeholder.git
```
Install the packages:
```sh
pip install -r requirements.txt
```

Run the app:
```shell 
uvicorn main:app --reload
```
or
```shell
python3 main.py
```


Required Query Strings are width and name. If you don't pass height, it will return a square image that is the same height as the width you specify.

An example call would be:
```html
<img src="http://localhost:8000/img/?width=800&height=600&name='placeholder image'" />

```

### It's as simple as that..  