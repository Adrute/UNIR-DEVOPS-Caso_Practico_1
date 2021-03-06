echo '##### Lanzamos el build'
sam build

echo '##### Empaquetamos'
sam package --template-file template.yaml --output-template-file packaged.yaml --s3-bucket ${COUNTRY}-${TEAM}-${ENVIRONMENT}-${SERVICE}-${RAND_ID}-artifacts