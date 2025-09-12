# note bump the version before updating pypi
rm -rf dist build
twine upload dist/*
python -m build
twine upload dist/*
