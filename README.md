# Vanilla Django 1.8.8 App

## Runs in two modes:

### With cached template loader

```
CACHED_LOADER=1 ./manage.py runserver      
```

### Without cached template loader
```
./manage.py runserver
```

## Has two views:

### `http://localhost:8000/includes/10/10`

### `http://localhost:8000/templatetags/10/10`

Both of these views render a recursively included template.

`http://localhest:8000/:renderType/:depth/:count`

`depth` is how many times the template will recurse.

`count` is how many times we render the template at the root level.

`/:renderType/100/100` will render the nested template `100 * 100` times.


No other stressors are in place here, this benchmark only measures the
overhead of rendering nested templates.


## Results

<a href="https://docs.google.com/spreadsheets/d/1iwWxPdsy4ifNH1viNFkScnYiYYAt_0JhuB9vO5c1r7Y/edit#gid=0">
  Spreadsheet of Results
</a>
