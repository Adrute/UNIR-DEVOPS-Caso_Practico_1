echo '##### Realizamos el despliegue'
yes | sam deploy --template-file packaged.yaml --stack-name ${STACK_NAME} --no-fail-on-empty-changeset --parameter-overrides ENVIRONMENT=${ENVIRONMENT}