echo "Provisioner is running ..."
sudo apt-get -y update
sudo apt-get -y install python-pip
sudo pip install virtualenv
virtualenv /home/vagrant/flask_env
source /home/vagrant/flask_env/bin/activate
pip install -r /vagrant/requirements.txt
echo "Provisioner is done."
echo " "
echo "--------------------"
echo "1. Login to box by typing:"
echo "--------------------"
echo " "
echo "vagrant ssh"
echo " "
echo " "
echo "--------------------"
echo "2. Once inside the virtualbox type:"
echo "--------------------"
echo " "
echo "cd /vagrant/; source /home/vagrant/flask_env/bin/activate"
echo " "
echo "--------------------"
echo "To run the tests you can then:"
echo "--------------------"
echo " "
echo "python tests.py"
echo " "
echo " "
echo "--------------------"
echo "To start the server you can:"
echo "--------------------"
echo " "
echo "gunicorn app:app -b 0.0.0.0:5000"
echo " "
echo "OR"
echo " "
echo "python app.py"
echo " "
echo "--------------------"
