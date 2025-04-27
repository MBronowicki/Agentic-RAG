NO_PRE=false
DEFAULT_VIRTUAL_ENV="NO_ENV"

for arg in "$@"; do
   # If --force is passed, print a message about installing outside virtualenv
   if [ "$arg" = "--force" ]; then
       echo 'Installing outside virtual environment'
   fi

   # Check if argument is "--no-pre"
   if [ "$arg" = "--no-pre" ]; then
       NO_PRE=true
       echo 'Skipping pre-commit installation'
   fi
done

# Check if virtualenv is set
if [ -z "$VIRTUAL_ENV" ]; then
   echo 'Must specify virtualenv'
   exit 1
else
   echo "Using virtualenv: $VIRTUAL_ENV"
fi

# Upgrade pip and install pip-tools
python3 -m pip install --upgrade pip
python3 -m pip install pip-tools

# Compile the requirements and install from the pyproject.toml
python3 -m piptools compile --all-extras -o requirements.txt pyproject.toml
python3 -m pip install -r requirements.txt

# # Install pre-commit only if --no-pre flag is not set
# if ! $NO_PRE; then
#    pre-commit install
# fi
