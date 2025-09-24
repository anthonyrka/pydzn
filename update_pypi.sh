# note bump the version before updating pypi
rm -rf dist build
python -m build
twine upload dist/*
