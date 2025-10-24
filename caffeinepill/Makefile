all: caffeinepill.exe clean

caffeinepill.obj:
	cl -c caffeinepill.c

caffeinepill.res:
	rc caffeinepill.rc

caffeinepill.exe: caffeinepill.res caffeinepill.obj
	link caffeinepill.obj caffeinepill.res user32.lib gdi32.lib /out:caffeinepill.exe 

clean:
	-cmd /c del caffeinepill.obj caffeinepill.res caffeinepill.obj