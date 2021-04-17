if [ $# -eq 0 ]
  then
    echo "Please specifiy installation destination."
    exit
fi

install_folder=$1

mkdir -p "$install_folder"
cd $install_folder
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-335.0.0-linux-x86_64.tar.gz
tar xvzf google-cloud-sdk-335.0.0-linux-x86_64.tar.gz -C $install_folder
rm google-cloud-sdk-335.0.0-linux-x86_64.tar.gz
cd $install_folder/google-cloud-sdk
./install.sh
