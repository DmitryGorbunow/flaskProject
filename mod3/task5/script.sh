#!/bin/bash
pylint ./mod2/task3.py --output-format=json:result.json
pylint ./mod2/task3.py -ry
pylint_res=$?
echo "$pylint_res"
if [[ pylint_res -eq 0 ]]; then
  echo ‘Pylint OK’
else
  echo ‘Имеются ошибки в Pylint’
fi

python -m unittest ./mod3/task2/test_decrypt.py
unittest_res=$?
echo "$unittest_res"
if [[ unittest_res -eq 0 ]]; then
  echo ‘Unittests OK’
else
  echo ‘Имеются ошибки в unittests’
fi

echo "hello"