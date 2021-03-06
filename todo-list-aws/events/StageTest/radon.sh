. envStageVM/bin/activate

result=0

echo '###### Prueba Radon cc ######'
if [[ `radon cc todos/*.py -nc | wc -l` -ne 0 ]]
then
    echo '[ERROR] Prueba "Radon cc" de los fuentes errónea. Se deben revisar los siguientes ficheros:'
    radon cc todos/*.py -nc
    result=1
fi

if [[ `radon cc tests/*.py -nc | wc -l` -ne 0 ]]
then
    echo '[ERROR] Prueba "Radon cc" de los tests errónea. Se deben revisar los siguientes ficheros:'
    radon cc tests/*.py -nc
    result=1
fi

echo '###### Prueba Radon mi ######'
if [[ `radon mi todos/*.py -nc | wc -l` -ne 0 ]]
then
    echo '[ERROR] Prueba "Radon mi" de los fuentes errónea. Se deben revisar los siguientes ficheros:'
    radon mi todos/*.py -nc
    result=1
fi

if [[ `radon mi tests/*.py -nc | wc -l` -ne 0 ]]
then
    echo '[ERROR] Prueba "Radon mi" de los tests errónea. Se deben revisar los siguientes ficheros:'
    radon mi tests/*.py -nc
    result=1
fi

if [[ $result -ne 0 ]]
then
    exit 1
else
    echo '[INFO] Prueba Radon satisfactoria.'
fi