# image_placeholder
This will generate a placeholder image by calling it within the an `<img src="" alt="placeholder" />`

## Install:
Clone the repo:

```sh
git clone https://github.com/dbeidle/image_placeholder.git
```

```sh
pip -r pip install -r requirements.txt
```

run the app:
```sh 
uvicorn main:app --reload
```

example call would be:
Required Query Strings are width and name. If you don't pass height, it will return a square image that is the same height as the width you specify.
```html
<img src="http://localhost:8000/img/?width=800&height=600&name='placeholder image'" />

```

### It's as simple as that..  