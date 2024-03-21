#!/bin/bash
#
# Before running this script, copy the spreadsheet into the inputs folder,
# and rename it to library-index.xlsx
#
# After running this script, check the *.log files that it has created in
# the outputs folder. Search for "warn" as well as "error".
#
# After the python scripts have all run successfully there will be a
# library-index.json file in ../src/components. Now the website can
# be built.
#
# This script assumes that a virtual environment named .venv has been
# created for the scripts directory.
# It also assumes that there are the following olders under the scripts
# directory:  inputs, outputs, logs.
#
#
VENV=.venv
#
FAILURE=1
SUCCESS=0
#
LOG_DIR=logs
INPUT_DIR=inputs
OUTPUT_DIR=outputs
LIBRARY_INDEX=inputs/library-index.xlsx
WEBSITE_SRC_PATH=../src/components

if [ ! -f $LIBRARY_INDEX ]; then
  echo "$LIBRARY_INDEX is missing, no processing can be done."
  exit $FAILURE
fi

# clear pervious outputs and log files
echo "Removing any previous $LOG_DIR/*.log files"
cd $LOG_DIR || {
  echo "Cannot change to log directory."
  exit $FAILURE
}

rm *.log
cd ..

echo "Removing any previous $OUTPUT_DIR *.csv and *.json files"
cd $OUTPUT_DIR || {
  echo "Cannot change to outputs directory."
  exit $FAILURE
}
rm *.csv
rm *.json
cd ..

#
# Input check and cleanup done. Time to start running the python scripts
#
# Activate the virtual environment
echo "Activate virtual environment $VENV"
source $VENV/bin/activate || {
  echo "Failed to activate virtual environment."
  exit $FAILURE
}

PYTHON_SCRIPT_NAME=parse-excel-file
echo "Running $PYTHON_SCRIPT_NAME.py ..."
python $PYTHON_SCRIPT_NAME.py > $LOG_DIR/$PYTHON_SCRIPT_NAME.log  || {
  echo "ERROR | $PYTHON_SCRIPT_NAME.py failed to run successfully."
  exit $FAILURE
}

PYTHON_SCRIPT_NAME=get-library-docs
echo "Running $PYTHON_SCRIPT_NAME.py (this may take quite a while)..."
python $PYTHON_SCRIPT_NAME.py > $LOG_DIR/$PYTHON_SCRIPT_NAME.log || {
  echo "ERROR | $PYTHON_SCRIPT_NAME.py failed to run successfully."
  grep "error" $LOG_DIR/$PYTHON_SCRIPT_NAME.log
  echo "View $LOG_DIR/$PYTHON_SCRIPT_NAME.log for more information."
  exit $FAILURE
}

PYTHON_SCRIPT_NAME=create-library-index
echo "Running $PYTHON_SCRIPT_NAME.py ..."
python $PYTHON_SCRIPT_NAME.py > $LOG_DIR/$PYTHON_SCRIPT_NAME.log || {
  echo "ERROR | $PYTHON_SCRIPT_NAME.py failed to run successfully."
  grep "error" $LOG_DIR/$PYTHON_SCRIPT_NAME.log
  echo "View $LOG_DIR/$PYTHON_SCRIPT_NAME.log for more information."
  exit $FAILURE
}

echo "SUCCESS | No errors but you should still check the log files for warnings."

# copy json files into website src area
echo "cp *.json files to $WEBSITE_SRC_PATH"
cp $OUTPUT_DIR/*.json $WEBSITE_SRC_PATH || {
  echo "ERROR: Failed to copy files."
  exit $FAILURE
}

echo "If all good then you are ready to build the website."
exit $SUCCESS
