nodo1.run("backup.sh")
nodo2.run("deploy.sh")
nodo3.run("update.sh")

nodo1.status()
nodo2.status()

grupoA.update()

deploy app1 to grupoA

parallel {
    nodo2.run("backup.sh")
    nodo3.run("update.sh")
}