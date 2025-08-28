import sys
#Comparações com python
sys.stdout.write( str(sys.argv) ) #mostra tudo
sys.stdout.write( "\n" )
sys.stdout.write(str (sys.argv[1]) )#mostra o arg 1
sys.stdout.write( "\n" )
sys.stdout.write(str (sys.argv[2]) )#mostra o arg 2 

va = int(sys.argv[1])
vb = int(sys.argv[2])
sys.stdout.write( "\nCOMPARAÇÕES LÓGICAS v.1" )
sys.stdout.write( "\nIgual? "         +str(va==vb) )
sys.stdout.write( "\nDiferente? "     +str(va!=vb) )
sys.stdout.write( "\nMaior? "         +str(va>vb)  )
sys.stdout.write( "\nMaior ou igual? "+str(va>=vb) )
sys.stdout.write( "\nMenor? "         +str(va<vb)  )
sys.stdout.write( "\nMenor ou igual? "+str(va<=vb) )

sys.stdout.write( "\n\nCOMPARAÇÕES LÓGICAS v.2" )
sys.stdout.write( "\nIgual? "         +("Sim" if va==vb else "Não") )
sys.stdout.write( "\nDiferente? "     +("Sim" if va!=vb else "Não") )
sys.stdout.write( "\nMaior? "         +("Sim" if va>vb  else "Não") )
sys.stdout.write( "\nMaior ou igual? "+("Sim" if va>=vb else "Não") )
sys.stdout.write( "\nMenor? "         +("Sim" if va<vb  else "Não") )
sys.stdout.write( "\nMenor ou igual? "+("Sim" if va<=vb else "Não") )

va = True
vb = False

sys.stdout.write( "\nA: "     +str(va) )
sys.stdout.write( "\nB: "     +str(vb) )
sys.stdout.write( "\nA E B: " +str(va and vb) )
sys.stdout.write( "\nA OU B: "+str(va or vb)  )
sys.stdout.write( "\nNOT A: " +str(not va)    )
sys.stdout.write( "\nNOT B: " +str(not vb)    )
sys.stdout.write( "\nNOT (A E B): "  +str(not(va and vb)) )
sys.stdout.write( "\nNOT (A OU B): " +str(not(va or vb))  )