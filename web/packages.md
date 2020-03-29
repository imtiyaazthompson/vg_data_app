# Packages
```python
	import sys
	sys.path.append('/src')
	
	from src import module1,module2
```

+ For the modules in `/src` that import modules from the same folder
	+ `import src.dependent_module as dependent_module`
