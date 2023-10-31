#!/bin/bash

SWAGGER_CODEGEN="./swagger-codegen-cli.jar"

java --version
if [ "$?" -ne 0 ]; then
  echo "Please install java to run this script (apt install java)"
  exit 1;
fi

if [ -f $SWAGGER_CODEGEN ]; then
  echo "$SWAGGER_CODEGEN found and using it"
else
  wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.44/swagger-codegen-cli-3.0.44.jar -O $SWAGGER_CODEGEN
fi

java -jar $SWAGGER_CODEGEN generate -i "https://onedata.org/api/21.02.3/onezone/swagger.json" -l python -o "onezone_client" -c "./onezone.conf" -v
java -jar $SWAGGER_CODEGEN generate -i "https://onedata.org/api/21.02.3/oneprovider/swagger.json" -l python -o "oneprovider_client" -c "./oneprovider.conf" -v
java -jar $SWAGGER_CODEGEN generate -i "https://onedata.org/api/21.02.3/onepanel/swagger.json" -l python -o "onepanel_client" -c "./onepanel.conf" -v