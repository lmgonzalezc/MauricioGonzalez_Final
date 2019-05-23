GonzalezMauricio_final_15.pdf: datos.dat plot.py
	python plot.py

%.dat : a.out
	./a.out 

a.out: xyt.cpp
	g++ xyt.cpp

  
  
  
          
