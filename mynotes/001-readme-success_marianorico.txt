By MarianoRico

** Note new project is created in PyCharm, not at PyPi website


1. Have account at PyPi.org 
   (have already , next step) 

2. need to have installed :
    pip install setuptools wheel
    pip install twine
    pip inatll tqdm
    (have already, next step)

3. Create new PyCharm Project in new folder, eg 201-MarianoDoc

4.  a. figure out name of package eg MarianoDoc
    b. create folder called marianodoc
    c. inside marianodoc folder, create __init__.py
       in this file create functions of the package 
       eg def sayhello4():
           return "hello4"
    d back up tp 201-MarianoDoc folder, need to have 2 files:
       1. setup.py  -> name must match the folder(package) name , in this case helloworldbasic4message
       2. LICENCE.txt
       ( just copy files found here and change)


5. If this is an update, rename or remove the dist folder :
     also update version number in setup.py


6. in terminal of project 4, runn the commands:
    python setup.py bdist_wheel
    ( if successful this will create a dist folder in project 4)

7. then finally run command:
   twine upload dist/*

8. ask for username : marstab4
           password : 750850_Py&

9 . to upgrade package on computer:
    pip install --upgrade marianodoc


10. to update in pip:
          pip list --outdated 
          pip install --upgrade helloworldbasic4message





     

      

