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
```html
<img src="http://localhost:8000/img/?width=800&height=600&name='placeholder image'" />

```

### It's as simple as that..  