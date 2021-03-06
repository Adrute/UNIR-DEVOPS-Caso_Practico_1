. envStageVM/bin/activate

echo "##### Inicia la fase de tests unitarios y cobertura"
export DYNAMODB_TABLE=todoTable
cd tests;

coverage run -m unittest TestToDo.py
if [[ $? -ne 0 ]]
then
    echo "[ERROR] Algo ha salido mal durante los tests unitarios."
    exit 1
fi

coverage report -m --fail-under=80 ../todos/todoTable.py

if [[ $? -ne 0 ]]
then
    echo "[ERROR] La cobertura no puede ser inferior al 80%."
    exit 1
fi

cd ..;
