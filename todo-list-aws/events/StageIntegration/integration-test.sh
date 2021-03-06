. envStageVM/bin/activate

echo "##### Inicia la fase de tests integrados"
cd tests;

python -m unittest TestToDoIntegration.py
if [[ $? -ne 0 ]]
then
    echo "[ERROR] Algo ha salido mal durante los tests integrados."
    exit 1
fi