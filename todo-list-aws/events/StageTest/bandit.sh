. envStageVM/bin/activate

echo '###### Prueba Bandit ######'
echo '### Prueba sobre los fuentes'
bandit todos/*.py

echo '### Prueba sobre los tests'
bandit tests/*.py