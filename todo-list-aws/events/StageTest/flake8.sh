. envStageVM/bin/activate

echo '###### Prueba flake8 ######'

echo '### Prueba sobre los fuentes'
flake8 todos/*.py

echo '### Prueba sobre los tests'
flake8 tests/*.py