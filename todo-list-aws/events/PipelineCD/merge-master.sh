echo "##### Clonamos el repositorio #####"

git checkout develop;
git checkout master;

echo "##### Realizamos el merge de develop a master #####"

git merge develop

if [[ $? -ne 0 ]]
then
    echo "[ERROR] Algo ha salido mal al realizar el merge hacia master."
    exit 1
fi

git push origin master

if [[ $? -ne 0 ]]
then
    echo "[ERROR] Algo ha salido mal al realizar el push a master."
    exit 1
fi