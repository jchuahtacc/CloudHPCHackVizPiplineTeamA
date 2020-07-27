REQUIREMENTS=`find . -name "requirements.txt"`

for requirement in $REQUIREMENTS; do
	pip install -r $requirement
done
