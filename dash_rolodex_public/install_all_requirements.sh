REQUIREMENTS=`find . -name "requirements.txt"`

for requirement in $REQUIREMENTS; do
	pip3 install --user -r $requirement
done
