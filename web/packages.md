# Packages
+ Folder structure
```
	/
	--/web/
		--app.py
		--/web/src/
			--module1.py
			--module2.py
			--__init__.py
```

+ Inside `app.py`
```python
	import sys
	sys.path.append('/src')
	
	from src import module1,module2
```

+ For the modules in `/web/src` that import modules from the same folder
	+ Inside `module1.py`
		+ `from . import module2`
