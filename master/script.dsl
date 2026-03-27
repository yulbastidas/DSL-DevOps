nodo1.run("backup.sh")
nodo2.run("deploy.sh")
nodo3.run("update.sh")

grupoA.update()

deploy app1 to grupoA

parallel {
    nodo2.run("backup.sh")
    nodo3.run("update.sh")
}
