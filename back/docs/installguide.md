# Install guide


## (Optional) Installing WSL on Windows 10/11

Windows Subsystem for Linux (WSL) installs a Linux distro along with Windows and it's officially supported by Microsoft.

A very complete guide is available here:
[Install Linux on Windows with WSL](https://docs.microsoft.com/en-us/windows/wsl/install)

_We recommend using a Ubuntu/Debian-based distribution for development._


## Installing the tech stack

### Conda
You can either install Miniconda or Anaconda, they both come with the `conda` environment manager. A step-by-step guide can be found here: https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

Afterwards, you need to create a Python environment for Django:
```sh
conda create -n sumdjango python=3.10
```

To use it, activate it:
```sh
conda activate sumdjango
```

To go back to your standard environment, deactivate it:
```sh
conda deactivate
```

### Django
Inside the `sumdjango` environment, you need to install the requirements:
```sh
pip install -r requirements.txt
```

This will install Django and the necessary libraries. Then, let's create the database and populate with tables:
```sh
python manage.py migrate
```

In order to run the Django application:
```sh
python manage.py runserver
```

You can check that the application is working by querying an endpoint via cURL (or your browser):
```sh
curl http://localhost:8000/trading/blotter/ 
```
This should output a JSON containing a collection of trade blotters.

### NodeJS and React

A good guide for installing NVM (_Node Version Manager_) is available [here](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl#install-nvm-nodejs-and-npm).

NVM allows you to have different NodeJS versions in your machine, while also allowing for easier updates and maintenance.

Then, use the `create-react-app` script to bootstrap a new React application:
```sh
npx create-react-app sum-app
```

And you may run it by typing:
```sh
npm start
```
A more in-depth guide can be found [here](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/react-on-windows#create-your-react-app).