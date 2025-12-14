### I was getting error while using below command to install redis- 
pip install redis

Error : Fatal error in launcher: Unable to create process using '"E:\Python\student-crud-k8s-minikube\venv\Scripts\python.exe"  "E:\Python Tutorial\student-crud-k8s-minikube\venv\Scripts\pip.exe" install redis': The system cannot find the file specified.

Solution - So used below command-
/> python -m pip install redis


docker build -t student-crud:v1 .

& minikube -p minikube docker-env --shell powershell | Invoke-Expression
kubectl get svc redis
kubectl get pods
minikube service student-crud --url
kubectl exec -it redis-67f77d7484-pk8mn  -- redis-cli

kubectl create deployment redis --image=redis:7
kubectl expose deployment redis --port=6379 --name=redis


------------------
git remote add origin https://github.com/pritum/student-crud-k8s-minikube.git