
bld:
	rm -fr dist
	python setup.py sdist bdist_wheel
	twine check dist/*

pub_test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
