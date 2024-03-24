arquivo=open("pagina.html","w",encoding="utf-8")
arquivo.write('<!DOCTYPE html>\n <html lang="en"> \n<head> \n<meta charset="UTF-8"> \n<meta name="viewport" content="width=device-width, initial-scale=1.0"> \n<title>Pagina Criada no Python</title> \n</head> \n<body><h1>Pagina gerada em Python</h1>\n <p>Paragarfo teste 1</p> \n<p>Paragarfo teste 2</p> \n<p>Paragarfo teste 3</p> \n<p>Paragarfo teste 4</p> \n</body> \n</html> \n')
arquivo.flush()
arquivo.close()